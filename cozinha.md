# Cozinha

ligações:
- [marquise](./marquise.md)
- [corredor 1](./corredores.md)


## Menu

- [Home](./readme.md)
- How it works
  - [Lights](./lights.md)
  - [Occupancy](./occupancy.md)
- Dumb2Smart
  - [Microwave](./dumb2smart/microwave.md)
  - [Coffee Machine](./dumb2smart/coffee_machine.md)
- Divisões:
  - [corredores](./corredores.md)
  - [sala](./sala.md)
  - [mancave](./mancave.md)
  - [escritorio](./escritorio.md)
  - [quarto](./quarto.md)
  - [quarto hugo](./quarto_hugo.md)
  - [wc](./wc.md)
  - [marquise](./marquise.md)
  - [Escritorio da Dii](./escritorio_dii.md)
  - [WC da Dii](./wc_dii.md)

## B.O.M

- PIR: 3
- Temperature: 1
- Light Switch: 2
- Smart Plugs: 7 (fridge | freezer | coffee | microwave | dishwasher | air fryer)
- Door Sensors: 4 (fridge | fridge_freezer | freezer | microwave)

Armarios; (dispensa)
  - Light Switch: 1  
  - Door Contact: 0 - (TODO - 1)
  - Window Contact: 0 - (TODO - 1)


## Automations

### Occupancy

when any condition triggers -> cozinha occupancy is **on**:
- fridge door open
- freezer door open
- microwave door open
- microwave heating
- coffee machine working
- PIR sensor (movement)
- lights on


![img_5.png](img_5.png)


### Lights on

when cozinha occupancy is **on**:
- if its night
- if sleep_cozinha is off
- lights on

![img_2.png](img_2.png)

#### Lights on - contadores

when **movement detected**:
- if its night
- if sleep_cozinha is off
- lights on

![img_7.png](img_7.png)

### Lights off

when cozinha occupancy is **off**:
- lights off

![img_3.png](img_3.png)

### Eletrodomesticos On

when cozinha occupancy is **on**:
- if sleep_cozinha is off
- coffee machine on
- dishwasher on

![img_6.png](img_6.png)

### Eletrodomesticos Off

when cozinha occupancy is **off**:
- coffee machine off
- microwave off

![img_4.png](img_4.png)


### Microwave

dumb2smart:
- smart plug
- limit sensor, high energy consumption threshold -> we know it is heating
- door contact sensor, track when door opens/closes

![img_10.png](img_10.png)

when microwave door is **open**:
- if microwave plug is off
- turn on microwave plug
- save timestamp

![img_8.png](img_8.png)