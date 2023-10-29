import string

from ovos_PHAL_sensors.base import _norm

from my_inventory.inventory import InventoryItem, Inventory
from my_inventory.prices import Query, Result


def get_thing(thing):
    def constructor(self, *args, **kwargs):
        return InventoryItem(self.unique_id, *args, **kwargs)

    name = "".join(c for c in thing.title() if c not in string.punctuation + string.whitespace)
    return type(name, (InventoryItem,), {"__new__": constructor, "unique_id": _norm(thing)})


class ShoppingList:
    def __init__(self):
        self.cart = []
        self.suggestions = {}
        self.results = {}
        self.inv = Inventory()

    def search(self, query: Query, cheapest=True):
        if query.query not in self.suggestions:
            self.suggestions[query.query] = []
        if cheapest:
            res = sorted(query.search(),
                         key=lambda k: k.price_per_capacity)
        else:
            res = query.search()
        for idx, r in enumerate(res):
            self.results[r.unique_id] = r
            if idx <= 10:
                self.suggestions[query.query].append(r)
        return self.suggestions[query.query]

    def add_to_cart(self, result: Result, quantity: int = 1):
        for i in range(quantity):
            self.cart.append(result)

    def checkout(self):
        vals = {thing.unique_id: 0 for thing in self.cart}
        for thing in self.cart:
            vals[thing.unique_id] += 1
        for tid, quantity in vals.items():
            self.inv.add_item(tid, quantity)
        return vals

    @property
    def total_price(self):
        return sum(k.price for k in self.cart)


if __name__ == "__main__":

    shop = ShoppingList()
    for q in [Query("chocolate")]:
        suggestions = shop.search(q)
        for s in suggestions[:3]:
            shop.add_to_cart(s)

    print(shop.total_price, "€")
    shop.checkout()  # add to inventory

    for r in shop.results.values():
        print(r)
