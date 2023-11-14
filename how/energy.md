# Energy Monitoring


## Menu

- [Home](../readme.md)
- How it works
  - [Software](software.md)
  - [Lights](lights.md)
  - [Occupancy](occupancy.md)
  - [Energy Monitoring](energy.md)
- Dumb2Smart
  - [Microwave](../dumb2smart/microwave.md)
  - [Coffee Machine](../dumb2smart/coffee_machine.md)

# Live Energy View

Live View for energy usage, monitor which devices are consuming energy real time

![live_energy_view.gif](live_energy_view.gif)


# Estimating costs

using [PowerCalc](https://homeassistant-powercalc.readthedocs.io/en/latest/quick-start.html) and [PowerGuess](https://github.com/OpenJarbas/powerguess)

## Switchs with Lights

When we have a switch in home assistant we can estimate power usage based on when devices are on, 
[PowerCalc](https://homeassistant-powercalc.readthedocs.io/en/latest/quick-start.html) makes this simple to do

![imagem](https://github.com/JarbasAl/smarthouse/assets/33701864/33d2cb24-bb8b-4c47-8e34-f6f65a035994)

### Hallways

B.O.M.

![switch](https://www.zigbee2mqtt.io/images/devices/TS0011_switch_module.jpg) 
![switch](https://www.zigbee2mqtt.io/images/devices/TS0011_switch_module.jpg) 
![switch](https://www.zigbee2mqtt.io/images/devices/TS0011_switch_module.jpg) 

- [switch TS0011](https://www.zigbee2mqtt.io/devices/TS0011_switch_module.html#tuya-ts0011_switch_module) cozinha - 1 times 7 W lamps
- [switch TS0011](https://www.zigbee2mqtt.io/devices/TS0011_switch_module.html#tuya-ts0011_switch_module) entrada - 3 times 7 W lamps
- [switch TS0011](https://www.zigbee2mqtt.io/devices/TS0011_switch_module.html#tuya-ts0011_switch_module) quartos - 3 times ? W lamps

### WC

B.O.M.

![switch TS0011](https://www.zigbee2mqtt.io/images/devices/TS0011_switch_module.jpg) 
![switch TS0011](https://www.zigbee2mqtt.io/images/devices/TS0011_switch_module.jpg) 


- [switch TS0011](https://www.zigbee2mqtt.io/devices/TS0011_switch_module.html#tuya-ts0011_switch_module) - 1 times ? W lamps
- [switch TS0011](https://www.zigbee2mqtt.io/devices/TS0011_switch_module.html#tuya-ts0011_switch_module) espelho - 1 times ? W lamps

### Kitchen

B.O.M.

![switch](https://www.zigbee2mqtt.io/images/devices/TS0011_switch_module.jpg) 
![switch](https://www.zigbee2mqtt.io/images/devices/TS0012_switch_module.jpg) 
![switch](https://www.zigbee2mqtt.io/images/devices/TS0011_switch_module.jpg) 

- [switch TS0011](https://www.zigbee2mqtt.io/devices/TS0011_switch_module.html#tuya-ts0011_switch_module) cozinha - 1 times ? W lamps
- [switch TS0012](https://www.zigbee2mqtt.io/devices/TS0012_switch_module.html#tuya-ts0012_switch_module) cozinha 2 - 1 times ? W lamps   ( + 1 unused gang)
- [switch TS0011](https://www.zigbee2mqtt.io/devices/TS0011_switch_module.html#tuya-ts0011_switch_module) dispensa - 1 times ? W lamps
- [switch TS0012](https://www.zigbee2mqtt.io/devices/TS0012_switch_module.html#tuya-ts0012_switch_module) marquise - 1 times ? W lamps   ( + 1 unused gang)

### Living Room

B.O.M.

![switch](https://www.zigbee2mqtt.io/images/devices/TS0012_switch_module.jpg) 
![switch](https://www.zigbee2mqtt.io/images/devices/TS0012_switch_module.jpg) 
![switch](https://www.zigbee2mqtt.io/images/devices/TS0012_switch_module.jpg) 
![switch](https://www.zigbee2mqtt.io/images/devices/TS0012_switch_module.jpg) 

- [switch TS0012](https://www.zigbee2mqtt.io/devices/TS0012_switch_module.html#tuya-ts0012_switch_module) tv - 3 times 7 W lamps
- [switch TS0012](https://www.zigbee2mqtt.io/devices/TS0012_switch_module.html#tuya-ts0012_switch_module) meio - 3 times 7 W lamps
- [switch TS0012](https://www.zigbee2mqtt.io/devices/TS0012_switch_module.html#tuya-ts0012_switch_module) mesa - 3 times 7 W lamps
- [switch TS0012](https://www.zigbee2mqtt.io/devices/TS0012_switch_module.html#tuya-ts0012_switch_module) quadros - 2 times ? W lamps
- plug 1 - 2 times ? W lamps

  
## Fixed costs

For each always on device not connected to a sensor we can estimate a fixed cost, measure the consumption once and then create a sensor

- [zigbee repeater TS0207](https://www.zigbee2mqtt.io/devices/TS0207_repeater.html) Hallway - 0.4W -> always on
- [zigbee repeater TS0207](https://www.zigbee2mqtt.io/devices/TS0207_repeater.html) WC - 0.4W -> always on

B.O.M.

![repeater](https://www.zigbee2mqtt.io/images/devices/TS0207_repeater.jpg) 
![repeater](https://www.zigbee2mqtt.io/images/devices/TS0207_repeater.jpg)


## Linux Devices
- MiniPC - can be considered a fixed cost, connected to a smart plug, or run [PowerGuess](https://github.com/OpenJarbas/powerguess) to provide an estimate
- RaspberryPi - can be considered a fixed cost, connected to a smart plug, or run [PowerGuess](https://github.com/OpenJarbas/powerguess) to provide an estimate
  
## Batteries

- Phones - the companion home assistant app usually provides the battery power (W) and state (charging/discharging), this can be used to estimate input/output energy and add the battery to Home Assistant
- Laptops - run [PowerGuess](https://github.com/OpenJarbas/powerguess), a linux utility that will also report battery power (W) and state (charging/discharging), this can be used to estimate input/output energy and add the battery to Home Assistant

![Peek 2023-11-11 02-49](https://github.com/OpenJarbas/powerguess/assets/33701864/ea76cf33-8c6a-4de7-bc51-e38a9a6359e6)
