import concurrent.futures
import time
from threading import Event
from typing import List

from ovos_PHAL_sensors.base import Sensor, BusSensor
from ovos_PHAL_sensors.loggers import HomeAssistantUpdater, MessageBusLogger
from ovos_config import Configuration
from ovos_plugin_manager.templates.phal import PHALPlugin

from my_inventory.inventory import Inventory
from my_inventory.prices import HipermercadosPortugal


class InventorySensors:

    def __init__(self, hipermercados=True, inventory=True):
        self.hiper = hipermercados
        self.inventory = inventory

        self._readings = {}
        self._ts = {}
        self._workers = 6

    @classmethod
    def bind(cls, name, ha_url, ha_token, bus=None, disable_bus=False, disable_ha=False):
        Sensor.device_name = name

        # setup home assistant
        if not ha_token or not ha_url:  # check HA plugin config
            cfg = Configuration().get("PHAL", {}).get(
                "ovos-PHAL-plugin-homeassistant", {})
            if "api_key" in cfg and not ha_token:
                ha_token = cfg["api_key"]
            if "host" in cfg and not ha_url:
                ha_url = cfg["host"]

        if ha_url and ha_token:
            HomeAssistantUpdater.ha_url = ha_url
            HomeAssistantUpdater.ha_token = ha_token
            if not disable_ha:
                Sensor.bind_logger(HomeAssistantUpdater)

        # connect messagebus
        if bus:
            cls.bus = bus
            BusSensor.bind(bus)
            MessageBusLogger.bus = bus
            if not disable_bus:
                Sensor.bind_logger(MessageBusLogger)

    @property
    def sensors(self) -> List[Sensor]:
        sensors = []

        if self.hiper:
            sensors += HipermercadosPortugal()._sensors
        if self.inventory:
            sensors += Inventory()._sensors
        return sensors

    def _parallel_readings(self, do_reading):
        results = {}

        # do the work in parallel instead of sequentially
        with concurrent.futures.ThreadPoolExecutor(max_workers=self._workers) as executor:

            matchers = {}
            # create a unique wrapper for each worker with their arguments
            for sensor in self.sensors:
                if sensor._thread_safe:
                    def do_thing(u=sensor):
                        return do_reading(u)

                    matchers[sensor.unique_id] = do_thing

            # Start the operations and mark each future with its source
            future_to_source = {
                executor.submit(func): device_id
                for device_id, func in matchers.items()
            }

            # retrieve results as they come
            for future in concurrent.futures.as_completed(future_to_source):
                future.result()

        # do sequential read for non thread safe sensors
        for sensor in self.sensors:
            if not sensor._thread_safe:
                do_reading(sensor)
        return results

    def update(self):

        def get_reading(sensor):
            if sensor.unique_id not in self._readings:
                self._readings[sensor.unique_id] = sensor.value
                self._ts[sensor.unique_id] = time.time()
                old = None
            else:
                if sensor._once:
                    # print("skipping", sensor.unique_id)
                    return  # doesnt change
                if sensor._slow and time.time() - self._ts[sensor.unique_id] < 15 * 60:
                    # print("skipping", sensor.unique_id)
                    return  # track timestamp and do once/hour
                old = self._readings[sensor.unique_id]

            if old is None or old != sensor.value:
                try:
                    sensor.sensor_update()
                    self._ts[sensor.unique_id] = time.time()
                except Exception as e:
                    print(e)

        self._parallel_readings(get_reading)


class InventoryPlugin(PHALPlugin):
    def __init__(self, bus, name="phal_inventory", config=None):
        self.running = False
        self.sleep = 5
        super().__init__(bus, name, config or {})

    def initialize(self):
        self.ha_url = self.config.get("ha_host")
        self.ha_token = self.config.get("ha_token")
        self.sleep = self.config.get("time_between_checks", 5)
        InventorySensors.bind(self.name, self.ha_url, self.ha_token, self.bus,
                              disable_bus=self.config.get("disable_bus", False),
                              disable_ha=self.config.get("disable_ha", False))
        self.device = InventorySensors(
            inventory=self.config.get("inventory", True),
            hipermercados=self.config.get("hipermercados", True))

    def run(self):
        self.initialize()
        self.running = True
        while self.running:
            self.device.update()
            Event().wait(self.sleep)


if __name__ == "__main__":
    from ovos_utils.messagebus import FakeBus
    from ovos_utils import wait_for_exit_signal

    config = {
        "ha_host": "http://192.168.1.8:8123",
        "ha_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2NGZmODYxY2M3ZDE0ZDZmODQ5MTMxNDgwODAyMmRmMiIsImlhdCI6MTY5ODM3ODk3NSwiZXhwIjoyMDEzNzM4OTc1fQ.PKPbyAw5dYPxZaLexy_Ed_U3OYRJeZI4DOKPljmE3Ow"
    }
    sensor = InventoryPlugin(bus=FakeBus(), config=config)
    wait_for_exit_signal()
