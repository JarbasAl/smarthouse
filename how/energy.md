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

Live View for energy usage, monitor which devices are consuming energy right 

![live_energy_view.gif](live_energy_view.gif)


# Estimating costs

using [PowerCalc](https://homeassistant-powercalc.readthedocs.io/en/latest/quick-start.html) and [PowerGuess](https://github.com/OpenJarbas/powerguess)

## Fixed costs

For each always on device not connected to a sensor we can estimate a fixed cost, measure the consumption once and then create a sensor

- zigbee repeater 1 - 0.4W -> always on
- zigbee repeater 2 - 0.4W -> always on

## Batteries

Phones - the companion home assistant app usually provides the battery power (W) and state (charging/discharging), this can be used to estimate input/output energy and add the battery to Home Assistant
Laptops - run [PowerGuess](https://github.com/OpenJarbas/powerguess), a linux utility that will also report battery power (W) and state (charging/discharging), this can be used to estimate input/output energy and add the battery to Home Assistant
RaspberryPi - can be considered a fixed cost, connected to a smart plug, or run [PowerGuess](https://github.com/OpenJarbas/powerguess) to provide an estimate

![Peek 2023-11-11 02-49](https://github.com/OpenJarbas/powerguess/assets/33701864/ea76cf33-8c6a-4de7-bc51-e38a9a6359e6)
