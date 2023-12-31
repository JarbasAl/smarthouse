# Marquise

## Navigation

- [Home](./readme.md)
- How it works
  - [Software](./how/software.md)
  - [Lights](./how/lights.md)
  - [Occupancy](./how/occupancy.md)
  - [Energy Monitoring](./how/energy.md)
- Dumb2Smart
  - [Microwave](./dumb2smart/microwave.md)
  - [Coffee Machine](./dumb2smart/coffee_machine.md)
  - [Shower](./dumb2smart/bath.md)

## Room Connections

ligações:
- [Escritorio da Dii](./escritorio_dii.md)
- [Cozinha](./cozinha.md)

## B.O.M

![imagem](https://github.com/JarbasAl/smarthouse/assets/33701864/ef5a673a-fb7a-417e-903f-7927a1d6c792)
![zth2](https://www.zigbee2mqtt.io/images/devices/ZTH02.jpg)
![pir](https://www.zigbee2mqtt.io/images/devices/IH012-RT01.jpg)
![contact](https://www.zigbee2mqtt.io/images/devices/TS0203.jpg)
![contact](https://www.zigbee2mqtt.io/images/devices/TS0203.jpg)
![contact](https://www.zigbee2mqtt.io/images/devices/TS0203.jpg)
![contact](https://www.zigbee2mqtt.io/images/devices/TS0203.jpg)
![contact](https://www.zigbee2mqtt.io/images/devices/TS0203.jpg)
![vibr](https://www.zigbee2mqtt.io/images/devices/TS0210.jpg)

- PIR: 1 (TODO - 2)
  - [IH012-RT01](https://www.zigbee2mqtt.io/devices/IH012-RT01.html#tuya-ih012-rt01)
- Temperature: 1
  - [ZTH02](https://www.zigbee2mqtt.io/devices/ZTH02.html#tuya-zth02)
- Window Contact: 4
  - [TS0203](https://www.zigbee2mqtt.io/devices/TS0203.html#tuya-ts0203) - window left
  - [TS0203](https://www.zigbee2mqtt.io/devices/TS0203.html#tuya-ts0203) - window right
  - [TS0203](https://www.zigbee2mqtt.io/devices/TS0203.html#tuya-ts0203) - window 2 left
  - [TS0203](https://www.zigbee2mqtt.io/devices/TS0203.html#tuya-ts0203) - window 2 right
- Light Switch: 1 (in kitchen)
- Smart Plugs: 1
  - [plug tplink HS110](https://www.tp-link.com/pt/home-networking/smart-plug/hs100/) - washing machine
- Vibration Sensors: 1 
  - [TS0210](https://www.zigbee2mqtt.io/devices/TS0210.html#tuya-ts0210) - washing machine
- Door Sensors: 1 
  - [TS0203](https://www.zigbee2mqtt.io/devices/TS0203.html#tuya-ts0203) - washing machine
 
## Automations

- if `occupancy` changes to **ON** **+** is `night time` **+ NOT** `sleeping` **+** `lights off` -> `turn on` lights
- if `occupancy` changes to **OFF** -> `turn off` lights
- if `house_sleep` changes to **ON** + `occupancy` is **OFF**-> `turn off` lights
  
`occupancy` is explained [here](./how/occupancy.md)

### Occupancy

when any condition triggers -> `occupancy` changes to **on**:
- PIR sensor (movement)
- lights turn on
- washing machine door opens
- windows open/close

`occupancy` does **NOT turn off** if:
- ...

when condition triggers **IF None of the above** -> `occupancy` changes to **off**:
- lights turn off
