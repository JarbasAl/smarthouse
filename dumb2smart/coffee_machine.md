# Coffee Machine

## Menu

- How it works
  - [Lights](./lights.md)
  - [Occupancy](./occupancy.md)
- Dumb2Smart
  - [Microwave](./dumb2smart/microwave.md)

## Requirements:
- Smart Switch: 1

## Features:
- power monitoring
- usage monitoring
- energy saving
- inventory tracking

![img_1.png](img_1.png)

### Energy Saving

- when usage stops for X minutes -> turn off smart plug

### Usage - binary sensor

detect power usage from smart plug, above a certain value we know machine is in use

![img_2.png](img_2.png)


### Usage Monitoring - State sensor

![img.png](img.png)

- turn on smart plug -> heating
- after 40 seconds -> ready
- on usage -> coffee
- on no usage -> ready

### Inventory

when state changes to coffee -> deduct 1 coffee from inventory

update timestamp of last coffee

