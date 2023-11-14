# Software

## Menu

- [Home](../readme.md)
- How it works
  - [Lights](lights.md)
  - [Occupancy](occupancy.md)
  - [Energy Monitoring](energy.md)
- Dumb2Smart
  - [Microwave](../dumb2smart/microwave.md)
  - [Coffee Machine](../dumb2smart/coffee_machine.md)


## Software Stack

- [OpenVoiceOS](https://www.openvoiceos.org) - voice assistant framework
  - [HiveMind](https://jarbashivemind.github.io/HiveMind-community-docs) - secure connections to OVOS / mesh networking
- [ovos-sensors](https://github.com/OpenVoiceOS/ovos-PHAL-sensors) - expose sensors from any linux device
- [zigbee2mqtt](https://www.zigbee2mqtt.io/) - connect zigbee devices
- [Home Assistant](https://www.home-assistant.io) - Home automation
  - [hivemind-home-assistant-notify](https://jarbashivemind.github.io/HiveMind-community-docs/homeassistant/) - make HiveMind devices speak