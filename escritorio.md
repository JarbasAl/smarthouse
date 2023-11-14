# Escritorio

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
- [corredor 2](./corredores.md)

## B.O.M

![switch](https://www.zigbee2mqtt.io/images/devices/TS0012_switch_module.jpg) 
![switch](https://www.zigbee2mqtt.io/images/devices/TS0011_switch_module.jpg)
![imagem](https://www.zigbee2mqtt.io/images/devices/TS011F_plug_1.jpg)
![zth2](https://www.zigbee2mqtt.io/images/devices/ZTH02.jpg)
![zth2](https://www.zigbee2mqtt.io/images/devices/ZTH02.jpg)
![pir](https://www.zigbee2mqtt.io/images/devices/IH012-RT01.jpg)
![pir](https://www.zigbee2mqtt.io/images/devices/IH012-RT01.jpg)
![contact](https://www.zigbee2mqtt.io/images/devices/TS0203.jpg)
![contact](https://www.zigbee2mqtt.io/images/devices/TS0203.jpg)
![contact](https://www.zigbee2mqtt.io/images/devices/TS0203.jpg)

- PIR: 2
  - [IH012-RT01](https://www.zigbee2mqtt.io/devices/IH012-RT01.html#tuya-ih012-rt01)
  - [IH012-RT01](https://www.zigbee2mqtt.io/devices/IH012-RT01.html#tuya-ih012-rt01) - desk
- Temperature: 1
  - [ZTH02](https://www.zigbee2mqtt.io/devices/ZTH02.html#tuya-zth02)
- Light Switch: 2
  - [switch TS0012](https://www.zigbee2mqtt.io/devices/TS0012_switch_module.html#tuya-ts0012_switch_module) left - 3 times 7 W lamps
  - [switch TS0012](https://www.zigbee2mqtt.io/devices/TS0012_switch_module.html#tuya-ts0012_switch_module) right - 3 times 7 W lamps
- Smart Plugs: 1
  - [plug ts011f](https://www.zigbee2mqtt.io/devices/TS011F_plug_1.html#tuya-ts011f_plug_1) - Stereo


Armarios;
- Light Switch: 1
  - [switch TS0011](https://www.zigbee2mqtt.io/devices/TS0012_switch_module.html#tuya-ts0011_switch_module) closet - 1 times ? W lamps
- Door Contact: 1
  - [TS0203](https://www.zigbee2mqtt.io/devices/TS0203.html#tuya-ts0203) - closet

Janelas:
- Window Contact: 2
  - [TS0203](https://www.zigbee2mqtt.io/devices/TS0203.html#tuya-ts0203) - window left
  - [TS0203](https://www.zigbee2mqtt.io/devices/TS0203.html#tuya-ts0203) - window right
- Temperature: 1  (peripitos)
  - [ZTH02](https://www.zigbee2mqtt.io/devices/ZTH02.html#tuya-zth02)

## Automations

- if `occupancy` changes to **ON** **+** is night time **+** not sleeping -> turn on lights
- if `occupancy` changes to **OFF** -> turn off lights

`occupancy` is explained [here](./how/occupancy.md)
