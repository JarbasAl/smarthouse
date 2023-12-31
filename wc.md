# WC

## Navigation

- [Home](./readme.md)
- How it works
  - [Software](./how/software.md)
  - [Lights](./how/lights.md)
  - [Occupancy](./how/occupancy.md)
  - [Energy Monitoring](./how/energy.md)
  - [Inventory](./how/inventory.md)
- Dumb2Smart
  - [Microwave](./dumb2smart/microwave.md)
  - [Coffee Machine](./dumb2smart/coffee_machine.md)
  - [Shower](./dumb2smart/bath.md)

# Room Connections

ligações:
- [corredor 3](./corredores.md)

## B.O.M

![switch TS0011](https://www.zigbee2mqtt.io/images/devices/TS0011_switch_module.jpg) 
![switch TS0011](https://www.zigbee2mqtt.io/images/devices/TS0011_switch_module.jpg) 
![repeater](https://www.zigbee2mqtt.io/images/devices/TS0207_repeater.jpg)
![zth2](https://www.zigbee2mqtt.io/images/devices/ZTH02.jpg)
![pir](https://www.zigbee2mqtt.io/images/devices/IH012-RT01.jpg)
![pir](https://www.zigbee2mqtt.io/images/devices/IH012-RT01.jpg)
![contact](https://www.zigbee2mqtt.io/images/devices/TS0203.jpg)
![water](https://www.zigbee2mqtt.io/images/devices/TS0207_water_leak_detector_2.jpg)

- PIR: 2
  - [IH012-RT01](https://www.zigbee2mqtt.io/devices/IH012-RT01.html#tuya-ih012-rt01) - toilet
  - [IH012-RT01](https://www.zigbee2mqtt.io/devices/IH012-RT01.html#tuya-ih012-rt01) - bathtub
- Temperature: 1
  - [ZTH02](https://www.zigbee2mqtt.io/devices/ZTH02.html#tuya-zth02)
- Light Switch: 2
  - [switch TS0011](https://www.zigbee2mqtt.io/devices/TS0011_switch_module.html#tuya-ts0011_switch_module) - 1 times ? W lamps
  - [switch TS0011](https://www.zigbee2mqtt.io/devices/TS0011_switch_module.html#tuya-ts0011_switch_module) espelho - 1 times ? W lamps
- ZigBee Repeater: 1
  - [TS0207](https://www.zigbee2mqtt.io/devices/TS0207_repeater.html) WC - 0.4W -> always on
- Water Leak: 1
  - [TS0207](https://www.zigbee2mqtt.io/devices/TS0207_water_leak_detector_2.html#tuya-ts0207_water_leak_detector_2) - bath

Janelas:
- Window Contact: 1
  - [TS0203](https://www.zigbee2mqtt.io/devices/TS0203.html#tuya-ts0203) - window

## Automations

- if `occupancy` changes to **ON** **+** is `night_time` + **NOT** `sleeping` **+** `lights off` -> `turn on` light (espelho)
- if `occupancy` changes to **OFF** -> `turn off` lights
- if `house_sleep` changes to **ON** + `occupancy` is **OFF**-> `turn off` lights
  
`occupancy` is explained [here](./how/occupancy.md)

### Occupancy

when any condition triggers -> `occupancy` changes to **on**:
- PIR sensor (movement)
- lights turn on
- windows open/close
- water detected

`occupancy` does **NOT turn off** if:
- water detected
- bath_probability > 70%

when condition triggers **IF None of the above** -> `occupancy` changes to **off**:
- lights turn off
