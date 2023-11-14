# ManCave

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
- [Sala](./sala.md)


## B.O.M

![switch](https://www.zigbee2mqtt.io/images/devices/TS0012_switch_module.jpg) 
![zth2](https://www.zigbee2mqtt.io/images/devices/ZTH02.jpg)
![pir](https://www.zigbee2mqtt.io/images/devices/IH012-RT01.jpg)
![contact](https://www.zigbee2mqtt.io/images/devices/TS0203.jpg)
![imagem](https://github.com/JarbasAl/smarthouse/assets/33701864/27e3892f-187d-43be-9126-c5780d415972)

- PIR: 1
  - [IH012-RT01](https://www.zigbee2mqtt.io/devices/IH012-RT01.html#tuya-ih012-rt01) 
- Temperature: 1
  - [ZTH02](https://www.zigbee2mqtt.io/devices/ZTH02.html#tuya-zth02)
- Light Switch: 2
  - [switch TS0012](https://www.zigbee2mqtt.io/devices/TS0012_switch_module.html#tuya-ts0012_switch_module) left - 2 times 7 W lamps
  - [switch TS0012](https://www.zigbee2mqtt.io/devices/TS0012_switch_module.html#tuya-ts0012_switch_module) right - 2 times 7 W lamps
- Smart Bulb: 1
  - [bulb LB130](https://www.tp-link.com/pt/home-networking/smart-bulb/lb130/) - floor lamp
- Dumb TV: 1

Janelas:
- Window Contact: 1
  - [TS0203](https://www.zigbee2mqtt.io/devices/TS0203.html#tuya-ts0203)
 
## Automations

- if `occupancy` changes to **ON** **+** is `night time` **+ NOT** `sleeping` -> `turn on` light (LB130)
- if `occupancy` changes to **OFF** -> `turn off` lights
- if `house_sleep` changes to **ON** + `occupancy` is **OFF**-> `turn off` lights

`occupancy` is explained [here](./how/occupancy.md)
