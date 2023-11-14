# Corredores

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


ligações corredor 1:
- [sala](./sala.md)
- [cozinha](./cozinha.md)

ligações corredor 2:
- exterior
- [corredor 1](./corredores.md)
- [mancave](./mancave.md)
- [escritorio](./escritorio.md)
- [corredor 3](./corredores.md)

ligações corredor 3:
- [corredor 2](./corredores.md)
- [quarto](./quarto.md)
- [quarto hugo](./quarto_hugo.md)
- [wc](./wc.md)


## B.O.M

![switch](https://www.zigbee2mqtt.io/images/devices/TS0011_switch_module.jpg) 
![switch](https://www.zigbee2mqtt.io/images/devices/TS0011_switch_module.jpg) 
![switch](https://www.zigbee2mqtt.io/images/devices/TS0011_switch_module.jpg)
![repeater](https://www.zigbee2mqtt.io/images/devices/TS0207_repeater.jpg) 
![zth2](https://www.zigbee2mqtt.io/images/devices/ZTH02.jpg)
![pir](https://www.zigbee2mqtt.io/images/devices/IH012-RT01.jpg)
![pir](https://www.zigbee2mqtt.io/images/devices/IH012-RT01.jpg)
![pir](https://www.zigbee2mqtt.io/images/devices/IH012-RT01.jpg)

### Corredor 1

- PIR: 1
  - [IH012-RT01](https://www.zigbee2mqtt.io/devices/IH012-RT01.html#tuya-ih012-rt01)
- Light Switch: 1
  - [switch TS0011](https://www.zigbee2mqtt.io/devices/TS0011_switch_module.html#tuya-ts0011_switch_module) 1 times 7 W lamps

### Corredor 2

- PIR: 1
  - [IH012-RT01](https://www.zigbee2mqtt.io/devices/IH012-RT01.html#tuya-ih012-rt01) 
- Temperature: 1
  - [ZTH02](https://www.zigbee2mqtt.io/devices/ZTH02.html#tuya-zth02)
- Light Switch: 1
  - [switch TS0011](https://www.zigbee2mqtt.io/devices/TS0011_switch_module.html#tuya-ts0011_switch_module) 3 times 7 W lamps
- ZigBee Repeater: 1
  - [zigbee repeater TS0207](https://www.zigbee2mqtt.io/devices/TS0207_repeater.html) Hallway - 0.4W -> always on

### Corredor 3

- PIR: 1
  - [IH012-RT01](https://www.zigbee2mqtt.io/devices/IH012-RT01.html#tuya-ih012-rt01) 
- Light Switch: 1
  - [switch TS0011](https://www.zigbee2mqtt.io/devices/TS0011_switch_module.html#tuya-ts0011_switch_module) 3 times 7 W lamps


## Automations

- if `PIR movement` changes to **ON** **+** is night time **+** hallways not sleeping-> turn on lights
- if `PIR movement` changes to **OFF** for 5 minutes -> turn off lights

