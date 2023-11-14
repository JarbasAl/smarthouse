# Quarto


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
- [corredor 3](./corredores.md)


## B.O.M

![imagem](https://github.com/JarbasAl/smarthouse/assets/33701864/593af74a-a260-41a5-a778-47e495379cb6)
![switch](https://www.zigbee2mqtt.io/images/devices/TS0012_switch_module.jpg) 
![switch](https://www.zigbee2mqtt.io/images/devices/TS0011_switch_module.jpg) 
![hs100](https://github.com/JarbasAl/smarthouse/assets/33701864/3d4ff7ec-bcb5-47aa-9445-e024a4e34725)
![zth2](https://www.zigbee2mqtt.io/images/devices/ZTH02.jpg)
![zth2](https://www.zigbee2mqtt.io/images/devices/ZTH02.jpg)
![pir](https://www.zigbee2mqtt.io/images/devices/IH012-RT01.jpg)
![contact](https://www.zigbee2mqtt.io/images/devices/TS0203.jpg)
![contact](https://www.zigbee2mqtt.io/images/devices/TS0203.jpg)
![contact](https://www.zigbee2mqtt.io/images/devices/TS0203.jpg)
![button](https://www.zigbee2mqtt.io/images/devices/IH-K663.jpg)

![imagem](https://github.com/JarbasAl/smarthouse/assets/33701864/d24afd4f-9da1-49ef-b683-4665ede887f1)
![imagem](https://github.com/JarbasAl/smarthouse/assets/33701864/50346f0a-e1f8-4ee0-a419-1e65b2e1627d)
![imagem](https://github.com/JarbasAl/smarthouse/assets/33701864/8f8f7a9c-e560-4652-9d3b-784fe844c4df)
![imagem](https://github.com/JarbasAl/smarthouse/assets/33701864/154a1e93-34b0-4408-8ab8-77c51683be78)



- PIR: 1   (TODO - 2)
  - [IH012-RT01](https://www.zigbee2mqtt.io/devices/IH012-RT01.html#tuya-ih012-rt01) - bed
- Temperature: 1
  - [ZTH02](https://www.zigbee2mqtt.io/devices/ZTH02.html#tuya-zth02)
- Light Switch: 2
  - [switch TS0012](https://www.zigbee2mqtt.io/devices/TS0012_switch_module.html#tuya-ts0012_switch_module) left - 3 times 7 W lamps
  - [switch TS0012](https://www.zigbee2mqtt.io/devices/TS0012_switch_module.html#tuya-ts0012_switch_module) right - 3 times 7 W lamps
- Smart Bulb: 1
  - [plug tplink HS100](https://www.tp-link.com/pt/home-networking/smart-plug/hs100/) - 1 times ? W lamps
- Media Players: 2
  - Raspberry pi 4  (HDMI 1 / Spotify)
  - Chromecast  (HDMI 2)
- HVAC: 1
  - [Baxi Anori R32](https://www.baxi.pt/produtos/ar-condicionado/um-compartimento/anori-mono-r32)
- Smart Button: 1
  - [IH-K663](https://www.zigbee2mqtt.io/devices/IH-K663.html#tuya-ih-k663) - desk lamp / house sleep (double click)
- Dumb TV: 1
  - Hisense - 80 - 120 W
- Remotes
  - [I8X plus](https://pt.aliexpress.com/item/1005001933350602.html) - USB remote Mouse and Keyboard (Raspberry pi 4)
- Audio Output: 1
  - TV - HDMI (Chromecast / Raspberry pi 4)
 
Armarios;
  - Light Switch: 1
    - [switch TS0011](https://www.zigbee2mqtt.io/devices/TS0012_switch_module.html#tuya-ts0011_switch_module) armario - 1 times ? W lamps
  - Door Contact: 1
    - [TS0203](https://www.zigbee2mqtt.io/devices/TS0203.html#tuya-ts0203) - closet

Janelas:
  - Window Contact: 2
    - [TS0203](https://www.zigbee2mqtt.io/devices/TS0203.html#tuya-ts0203) - window left
    - [TS0203](https://www.zigbee2mqtt.io/devices/TS0203.html#tuya-ts0203) - window right
  - Temperature: 1 (exterior)
    - [ZTH02](https://www.zigbee2mqtt.io/devices/ZTH02.html#tuya-zth02)

### Software
- Raspberry pi 4
  - [manjaro arm](https://manjaro.org/download/#ARM) - Base Operating System
  - [HiveMind](https://jarbashivemind.github.io/HiveMind-community-docs/) - Notify via Home Assistant
  - [ovos-PHAL-sensors](https://github.com/OpenVoiceOS/ovos-PHAL-sensors) - RPI sensors in Home Assistant
  - [PowerGuess](https://github.com/OpenJarbas/powerguess) - fake power consumption in Home Assistant
  - [Spotifyd](https://github.com/Spotifyd/spotifyd) . accepts audio streaming from spotify
 
## Automations

- if `occupancy` changes to **ON** **+** is `night_time` **+ NOT** `sleeping` **+** `lights off` -> `turn on` smart plug (candeeiro == light)
- if `occupancy` changes to **OFF** -> `turn off` lights + `turn off` smart plug (candeeiro == light)
- if `house_sleep` changes to **ON** -> `turn off` lights
- if `button_click` -> `toogle` candeeiro
- if `button_double_click` -> `toogle` house_sleep

`occupancy` is explained [here](./how/occupancy.md)
    
