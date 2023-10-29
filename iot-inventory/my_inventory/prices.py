from dataclasses import dataclass
from typing import Tuple, List, Optional

import requests
from json_database import JsonStorageXDG
from ovos_PHAL_sensors.base import _norm
from ovos_utils import timed_lru_cache
from unidecode import unidecode

from my_inventory.inventory import InventoryItem, ItemPrice, ItemPricePerUnit, ItemPricePerCapacity,\
    ItemCapacity, ItemImage, ItemShoppingLink


@dataclass
class Result:
    hiper: str = ""
    name: str = ""
    price: float = 0.0  # eur
    price_per_unit: float = 0.0  # eur / n_items
    price_per_capacity: float = 0.0  # eur / capacity unit
    unit: str = ""
    capacity: float = 0.0
    item_capacity: float = 0.0
    image_url: str = ""
    date: str = ""
    url: str = ""
    currency: str = "€"
    n_items: int = 1

    @property
    def unique_id(self):
        return f"{_norm(self.hiper)}_{_norm(self.name)}"


# allow sensors as plugins once we have CommonIOT
class HipermercadosPortugal:
    base_url = "https://app.supersave.pt/crawler/product.php"
    hipers = ['Auchan', 'Continente', 'Minipreço', 'PingoDoce']

    def __init__(self, queries: list = None, debug=False):
        # TODO - from config
        default_queries = [
            Query("cerveja", required=["super bock"], blacklist=["sagres", "sem alcool"]),
            Query("café", required=["cápsulas"], blacklist=["máquina"]),
            Query("bife de peru", required=["bife"]),
            Query("bife de frango", required=["bife"]),
            Query("frango inteiro", blacklist=["bife"]),
            Query("douradinhos"),
            Query("leite"),
            Query("arroz"),
            Query("salsichas"),
            Query("bife de vaca", required=["bife"]),
            Query("bife de boi", required=["bife"]),
            Query("manteiga"),
            Query("cereais de chocolate", blacklist=["tablete", "barra"]),
            Query("almondegas"),
            Query("hamburger"),
            Query("pizza"),
            Query("papel higienico"),
            Query("pasta dos dentes"),
            Query("sabão"),
            Query("bolachas", required=["chocolate"], blacklist=["branco"])
        ]
        self.queries = queries or default_queries
        self.databases = {}
        self.debug = debug
        for hiper in self.hipers:
            if hiper not in self.databases:
                self.databases[hiper] = JsonStorageXDG(name=f"{hiper}_prices", subfolder="ovos_sensors")

    @property
    def sensors(self):
        sensors = []
        for hiper, db in self.databases.items():
            for sensor_name, data in db.items():
                sensor_name = _norm(sensor_name)
                sensors += [
                    InventoryItem(sensor_name, n_items=data["n_items"], device_name=hiper),
                    ItemPrice(sensor_name + "_price", price=data["price"], device_name=hiper),
                    ItemShoppingLink(sensor_name + "_buy", url=data["url"], device_name=hiper),
                    ItemImage(sensor_name + "_image", url=data["image_url"], device_name=hiper),
                    ItemCapacity(sensor_name + "_capacity", capacity=data["capacity"],
                                 device_name=hiper, unit=data["unit"]),
                    ItemPricePerUnit(sensor_name + "_price_per_unit", price=data["price_per_unit"], device_name=hiper),
                    ItemPricePerCapacity(sensor_name + "_price_per_" + data["unit"], unit=data["unit"],
                                         price=data["price_per_capacity"], device_name=hiper)
                ]
        return sensors

    def update(self, hipers=None):
        hipers = hipers or self.hipers
        for hiper in hipers:
            if hiper not in self.databases:
                self.databases[hiper] = JsonStorageXDG(name=f"{hiper}_prices", subfolder="hipermercadosPT")
        for q in self.queries:
            try:
                if isinstance(q, Query):
                    res = q.search(self)
                else:
                    res = self.search(q)
            except:
                print("rate limited, try again in a few hours")
                break

            for item in res:
                if item.hiper not in hipers:
                    continue
                self.databases[item.hiper][item.name] = item.__dict__
                yield item

        for db in self.databases.values():
            db.store()

    @staticmethod
    def _parse_price(data) -> float:
        price = data["normalPrice"].replace(",", ".").split("/")[0]
        price = "".join([c for c in price if c.isdigit() or c == "."])
        return float(price)

    def _parse_capacity(self, data, price) -> Tuple[int, float, float, str]:

        capacity = data["capacity"].lower()
        if capacity.startswith("x"):
            capacity = f"1{capacity}"
        for r in ["emb.", "garrafa", " ",
                  "aprox", "peso escorrido", "Quant. Mínima = ", "(", ")", "[", "]"]:
            capacity = capacity.replace(r, "")

        if capacity == "0":
            # try to get from name, usually means a bad parse upstream
            name = data["name"]
            if "kg" in name.lower().split():
                capacity = "".join([c for c in data["name"] if c.isdigit() or c in ["."]]) + "kg"
            else:
                raise RuntimeError("malformed result")

        # number X number unit
        if "x" in capacity:
            n, icapacity = capacity.split("x")
            n = int("".join([c for c in n if c.isdigit()]))

            unit = "".join([c for c in icapacity if not c.isdigit() and c not in ["."]])
            icapacity = float("".join([c for c in icapacity if c.isdigit() or c in ["."]]))
            capacity = round(n * icapacity, 6)
        # unit | number unit | empty
        else:
            n = 1
            unit = "".join([c for c in capacity if not c.isdigit() and c not in ["."]])
            capacity = "".join([c for c in capacity if c.isdigit() or c in ["."]])
            if not capacity and unit:
                capacity = 1
            else:
                capacity = float(capacity)
            icapacity = capacity

        if self.debug:
            print(data["name"], "###", data["capacity"])
            print("n items:", n)
            print("total price:", price, "€")
        return n, icapacity, capacity, unit

    def _standardize_units(self, icapacity, capacity, unit, price) -> Tuple[float, float, str, float]:
        target = unit
        if unit.startswith("gr"):
            unit = "g"
        if unit.lower() in ["cl", "ml"]:
            target = "l"
        elif unit.lower() in ["g"]:
            target = "kg"
        if target != unit:
            # print(unit, target)
            if target == f"k{unit}":  # g -> kg
                icapacity = icapacity / 1000
                capacity = capacity / 1000
                unit = target

            elif unit == f"m{target}":  # ml -> L
                icapacity = icapacity / 1000
                capacity = capacity / 1000
                unit = target
            elif unit == f"c{target}":  # cl -> L
                icapacity = icapacity / 100
                capacity = capacity / 100
                unit = target

        ppcapacity = round(price / capacity, 6)  # eg, price per liter
        if self.debug:
            print(f"total {unit}:", capacity)
            print(f"{unit} per item:", icapacity)
            print(f"price per {unit}:", ppcapacity, "€")
        return icapacity, capacity, unit, ppcapacity

    @classmethod
    @timed_lru_cache()
    def _do_request(cls, query):
        return requests.get(cls.base_url, params={"search": query}).json()

    def search(self, query, required=None, blacklist=None):
        data = self._do_request(query)
        required = required or []
        blacklist = blacklist or []
        for hiper, prices in data.items():

            def _norm(s):
                return unidecode(s.lower().replace(",", "."))

            if blacklist:
                prices = [v for v in prices
                          if not any(_norm(b) in _norm(v["name"]) for b in blacklist)]
            if required:
                prices = [v for v in prices
                          if all(_norm(r) in _norm(v["name"]) for r in required)]
            for p in prices:
                if not p["capacity"]:  # usually means malformed results
                    continue
                p["name"] = _norm(p["name"])
                try:
                    price = self._parse_price(p)
                    n, icapacity, capacity, unit = self._parse_capacity(p, price)
                    icapacity, capacity, unit, ppcapacity = self._standardize_units(icapacity, capacity, unit, price)
                    if self.debug:
                        print("hipermercado:", hiper, "\n")
                    yield Result(hiper=hiper,
                                 name=p["name"],
                                 price=price,
                                 price_per_unit=float(price / n),
                                 price_per_capacity=ppcapacity,
                                 capacity=capacity,
                                 url=p["productURL"],
                                 image_url=p["imageURL"],
                                 date=p["date"],
                                 unit=unit,
                                 currency="€",
                                 item_capacity=icapacity,
                                 n_items=n)

                except GeneratorExit:
                    return
                except:
                    print("## ERROR: failed to parse", p)
                    continue


class Auchan(HipermercadosPortugal):
    hipers = ['Auchan']


class Continente(HipermercadosPortugal):
    hipers = ['Continente']


class Minipreco(HipermercadosPortugal):
    hipers = ['Minipreço']


class PingoDoce(HipermercadosPortugal):
    hipers = ['PingoDoce']


@dataclass
class Query:
    query: str
    required: Optional[List[str]] = None
    blacklist: Optional[List[str]] = None
    _sensors: Optional[List] = None

    def search(self, hiper: Optional[HipermercadosPortugal] = None):
        hiper = hiper or HipermercadosPortugal()
        results = list(hiper.search(query=self.query,
                            blacklist=self.blacklist,
                            required=self.required))
        self._sensors = []
        for res in results:
            sensor_name = _norm(res.name)
            self._sensors += [
                InventoryItem(sensor_name, n_items=res.n_items, device_name=res.hiper),
                ItemPrice(sensor_name + "_price", price=res.price, device_name=res.hiper),
                ItemShoppingLink(sensor_name + "_buy", url=res.url, device_name=res.hiper),
                ItemImage(sensor_name + "_image", url=res.image_url, device_name=res.hiper),
                ItemCapacity(sensor_name + "_capacity", capacity=res.capacity, device_name=res.hiper, unit=res.unit),
                ItemPricePerUnit(sensor_name + "_price_per_unit", price=res.price_per_unit, device_name=res.hiper),
                ItemPricePerCapacity(sensor_name + "_price_per_" + res.unit, unit=res.unit,
                                     price=res.price_per_capacity, device_name=res.hiper)
            ]
        return results

    @property
    def sensors(self):
        return self._sensors


if __name__ == "__main__":
    q = Query("bolachas", required=["chocolate"], blacklist=["branco"])
    q.search()
    for s in q.sensors:
        print(s)
    exit()
    hiper = HipermercadosPortugal()

    for res in hiper.update():
        print(res)
