# Microwave

## Menu

- How it works
  - [Lights](../lights.md)
  - [Occupancy](../occupancy.md)
- Dumb2Smart
  - [Coffee Machine](./coffee_machine.md)

## Requirements:
- Smart Switch: 1
- Contact Sensor: 1

## Features:
- power monitoring
- usage monitoring
- energy saving

![img_3.png](img_3.png)

### Usage - binary sensor

detect power usage from smart plug, above a certain value we know machine is in use

![img_4.png](img_4.png)

### Usage Monitoring

![img_9.png](img_9.png)

- on door open -> save timestamp

### Energy Saving

- on door open -> turn on smart plug
- when heating stops for X minutes -> turn off smart plug

![img_8.png](img_8.png)