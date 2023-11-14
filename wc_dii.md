# WC da Dii

## Menu

- [Home](./readme.md)
- How it works
  - [Software](./how/software.md)
  - [Lights](./how/lights.md)
  - [Occupancy](./how/occupancy.md)
  - [Energy Monitoring](./how/energy.md)
- Dumb2Smart
  - [Microwave](./dumb2smart/microwave.md)
  - [Coffee Machine](./dumb2smart/coffee_machine.md)

## Ligações

ligações:
- [escritorio da Dii](./escritorio_dii.md)

## B.O.M

![switch](https://www.zigbee2mqtt.io/images/devices/TS0011_switch_module.jpg) 
![zth2](https://www.zigbee2mqtt.io/images/devices/ZTH02.jpg)
![pir](https://www.zigbee2mqtt.io/images/devices/IH012-RT01.jpg)

- PIR: 1
  - [IH012-RT01](https://www.zigbee2mqtt.io/devices/IH012-RT01.html#tuya-ih012-rt01)
- Temperature: 1
  - [ZTH02](https://www.zigbee2mqtt.io/devices/ZTH02.html#tuya-zth02)
- Light Switch: 1
  - [switch TS0011](https://www.zigbee2mqtt.io/devices/TS0012_switch_module.html#tuya-ts0011_switch_module) - 1 times ? W lamps

## Automations

- if `occupancy` changes to **ON** **+** is `night_time` **+ NOT** `sleeping` **+** `lights off` -> `turn on` lights
- if `occupancy` changes to **OFF** -> `turn off` lights
- if `house_sleep` changes to **ON** + `occupancy` is **OFF**-> `turn off` lights

`occupancy` is explained [here](./how/occupancy.md)
