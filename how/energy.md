# Energy Monitoring


## Navigation

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

# Estimating Usage

using [PowerCalc](https://homeassistant-powercalc.readthedocs.io/en/latest/quick-start.html) and [PowerGuess](https://github.com/OpenJarbas/powerguess)

## Switchs with Lights

When we have a switch in home assistant we can estimate power usage based on when devices are on, 
[PowerCalc](https://homeassistant-powercalc.readthedocs.io/en/latest/quick-start.html) makes this simple to do

![imagem](https://github.com/JarbasAl/smarthouse/assets/33701864/33d2cb24-bb8b-4c47-8e34-f6f65a035994)

## Fixed costs

For each always on device not connected to a sensor we can estimate a fixed cost, measure the consumption once and then create a sensor

## Smart Plugs

some smart plugs report live energy consumption, but they don't report the consumption of the plug itself

PowerCalc automatically detects most devices and adds a sensor for this, all plugs in this document were automatically detected

## Linux Devices

- MiniPC - can be considered a fixed cost, connected to a smart plug, or run [PowerGuess](https://github.com/OpenJarbas/powerguess) to provide an estimate
  
- RaspberryPi - can be considered a fixed cost, connected to a smart plug, or run [PowerGuess](https://github.com/OpenJarbas/powerguess) to provide an estimate
  
## Batteries

- Laptops - run [PowerGuess](https://github.com/OpenJarbas/powerguess), a linux utility that will also report battery power (W) and state (charging/discharging), this can be used to estimate input/output energy and add the battery to Home Assistant

![Peek 2023-11-11 02-49](https://github.com/OpenJarbas/powerguess/assets/33701864/ea76cf33-8c6a-4de7-bc51-e38a9a6359e6)  ![charge](https://github.com/JarbasAl/smarthouse/assets/33701864/0e6a92ed-7071-4c79-baf7-8b8ef1b832f2)

- Phones - the companion home assistant app usually provides the battery power (W) and state (charging/discharging), this can be used to estimate input/output energy and add the battery to Home Assistant

![imagem](https://github.com/JarbasAl/smarthouse/assets/33701864/ec64c3f9-797c-45e4-b7e4-200481efa782) ![imagem](https://github.com/JarbasAl/smarthouse/assets/33701864/549e074a-2fcc-4383-b000-a57eac6eeefa)



