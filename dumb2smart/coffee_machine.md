# Coffee Machine

## Navigation

- How it works
  - [Lights](../how/lights.md)
  - [Occupancy](../how/occupancy.md)
  - [Software](../how/software.md)
- Dumb2Smart
  - [Microwave](./microwave.md)

## Requirements:

![imagem](https://www.zigbee2mqtt.io/images/devices/TS011F_plug_1.jpg)
![contact](https://www.zigbee2mqtt.io/images/devices/TS0203.jpg)
![water](https://www.zigbee2mqtt.io/images/devices/IH-K665.jpg)

- Smart Switch: 1
  - [plug ts011f](https://www.zigbee2mqtt.io/devices/TS011F_plug_1.html#tuya-ts011f_plug_1)
- Water Leak: 1
  - [IH-K665](https://www.zigbee2mqtt.io/devices/IH-K665.html#aubess-ih-k665)
- Contact Sensor: 1
  - [TS0203](https://www.zigbee2mqtt.io/devices/TS0203.html#tuya-ts0203)
  
## Features:
- power monitoring
- usage monitoring
- energy saving
- inventory tracking

![img_1.png](img_1.png)

### Energy Saving

- when usage stops for X minutes -> turn off smart plug
- when capsule holder opens -> turn on smart plug

### Heating - binary sensor

detect power usage from smart plug, above a certain value we know machine is in use

![img_2.png](img_2.png)


### Usage Monitoring - State sensor

![img_6.png](img_6.png)

### Inventory

when state changes to coffee -> deduct 1 coffee from inventory

update timestamp of last coffee

