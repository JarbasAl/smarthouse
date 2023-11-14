# Sala

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
- [corredor 1](./corredores.md)
- [ManCave](./mancave.md)


## B.O.M

![switch](https://www.zigbee2mqtt.io/images/devices/TS0012_switch_module.jpg) 
![switch](https://www.zigbee2mqtt.io/images/devices/TS0012_switch_module.jpg) 
![hs100](https://github.com/JarbasAl/smarthouse/assets/33701864/3d4ff7ec-bcb5-47aa-9445-e024a4e34725)
![imagem](https://www.zigbee2mqtt.io/images/devices/TS011F_plug_1.jpg)
![zth2](https://www.zigbee2mqtt.io/images/devices/ZTH02.jpg)
![zth2](https://www.zigbee2mqtt.io/images/devices/ZTH02.jpg)
![pir](https://www.zigbee2mqtt.io/images/devices/IH012-RT01.jpg)
![pir](https://www.zigbee2mqtt.io/images/devices/IH012-RT01.jpg)
![contact](https://www.zigbee2mqtt.io/images/devices/TS0203.jpg)
![contact](https://www.zigbee2mqtt.io/images/devices/TS0203.jpg)


![imagem](https://github.com/JarbasAl/smarthouse/assets/33701864/d24afd4f-9da1-49ef-b683-4665ede887f1)
![imagem](https://github.com/JarbasAl/smarthouse/assets/33701864/59d84c1b-16ef-4f25-a1a7-d327a15b70ac)
![imagem](https://github.com/JarbasAl/smarthouse/assets/33701864/95c89b35-edb0-457d-8df5-bd5d244b3358)
![imagem](https://github.com/JarbasAl/smarthouse/assets/33701864/e9dd71b6-b3ac-449e-a19e-7aa1ed7bbcad)
![imagem](https://github.com/JarbasAl/smarthouse/assets/33701864/62c315ed-65bf-4302-91b3-6e4a24187e1a)
![imagem](https://github.com/JarbasAl/smarthouse/assets/33701864/7453829d-2774-4741-9ab6-ca361fbd542d)




### IOT

- PIR: 2
  - [IH012-RT01](https://www.zigbee2mqtt.io/devices/IH012-RT01.html#tuya-ih012-rt01) - entrance
  - [IH012-RT01](https://www.zigbee2mqtt.io/devices/IH012-RT01.html#tuya-ih012-rt01) - couch
- Temperature: 1
  - [ZTH02](https://www.zigbee2mqtt.io/devices/ZTH02.html#tuya-zth02)
- Light Switch: 4
  - [switch TS0012](https://www.zigbee2mqtt.io/devices/TS0012_switch_module.html#tuya-ts0012_switch_module) tv - 3 times 7 W lamps
  - [switch TS0012](https://www.zigbee2mqtt.io/devices/TS0012_switch_module.html#tuya-ts0012_switch_module) meio - 3 times 7 W lamps
  - [switch TS0012](https://www.zigbee2mqtt.io/devices/TS0012_switch_module.html#tuya-ts0012_switch_module) mesa - 3 times 7 W lamps
  - [switch TS0012](https://www.zigbee2mqtt.io/devices/TS0012_switch_module.html#tuya-ts0012_switch_module) quadros - 2 times ? W lamps
- Smart Bulb: 1
  - [plug tplink HS100](https://www.tp-link.com/pt/home-networking/smart-plug/hs100/) - 2 times ? W lamps
- Smart Plugs: 1 
  - [plug TS011F](https://www.zigbee2mqtt.io/devices/TS011F_plug_1.html#tuya-ts011f_plug_1) - TV / Stereo
- Led Strip: 1 (espelho)
- HVAC: 1
- IR Control: 1  (TV, HVAC)
- Smart TV: 1
  - Hisense  - 80 - 120W
- Zigbee Relays: 1
  - [Sonoff](https://pt.aliexpress.com/item/1005003606832844.html) (MiniPC)
- Media Players: 3
  - [MiniPC U500-H](https://www.minisforum.com/Public/upload/files/2019-08-30/5d688d3e252e5.pdf) (DLNA audio / Spotify)
  - Smart TV  (DLNA video + audio)
  - [RCA Bluetooth](https://pt.aliexpress.com/item/1005005917337257.html) adapter  (Bluetooth Speaker)
- Remotes
  - [MX3 Air Mouse](https://pt.aliexpress.com/item/1005002652549274.html) - USB remote AirMouse and Keyboard (MiniPC)
- Microphone: 1
  - [MX3](https://pt.aliexpress.com/item/1005002652549274.html) - via MiniPC
- Audio Output: 2
  - Stereo - cassette + Bluetooth (MiniPC)
  - TV - DLNA + HDMI (MiniPC)
    
Janelas:
  - Window Contact: 2
    - [TS0203](https://www.zigbee2mqtt.io/devices/TS0203.html#tuya-ts0203) - window left
    - [TS0203](https://www.zigbee2mqtt.io/devices/TS0203.html#tuya-ts0203) - window right
  - Temperature: 1 (exterior)
    - [ZTH02](https://www.zigbee2mqtt.io/devices/ZTH02.html#tuya-zth02)

### Software

- [MiniPC U500-H](https://www.minisforum.com/Public/upload/files/2019-08-30/5d688d3e252e5.pdf)
  - [Manjaro Linux](https://manjaro.org/) - Base Operating System
  - Firefox - Youtube / Netflix
    - [Sponsorblock](https://addons.mozilla.org/pt-PT/firefox/addon/sponsorblock/)
    - [UBlock Origin](https://addons.mozilla.org/pt-PT/firefox/addon/ublock-origin)
  - [ovos-docker](https://openvoiceos.github.io/ovos-docker/) - Voice Assistant
  - [HomeAssistant](https://www.home-assistant.io) - Home Assistant
  - [Zigbee2MQTT](https://www.zigbee2mqtt.io/) - Zigbee control hub 
  - [HiveMind](https://jarbashivemind.github.io/HiveMind-community-docs/) - Notify via Home Assistant
  - [ovos-PHAL-sensors](https://github.com/OpenVoiceOS/ovos-PHAL-sensors) - MiniPC sensors in Home Assistant
  - [PowerGuess](https://github.com/OpenJarbas/powerguess) - MiniPC power consumption in Home Assistant
  - [Spotifyd](https://github.com/Spotifyd/spotifyd) . accepts audio streaming from spotify
  - [UPMPDCli](https://www.lesbonscomptes.com/upmpdcli/) - accepts audio streaming via DLNA
  - [MiniDLNA](https://wiki.archlinux.org/title/ReadyMedia) - exposes files for streaming via DLNA

