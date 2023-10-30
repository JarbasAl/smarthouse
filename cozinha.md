# Cozinha

ligações:
- [marquise](./marquise.md)
- [corredor 1](./corredores.md)

## Docs
- [Home](./readme.md)
- [Lights](./lights.md)
- [Occupancy](./occupancy.md)

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

### Lights on

quando ocupação da cozinha é **ligada**:
- Se for de noite
- se sleep da cozinha desligado
- liga luzes

![img_2.png](img_2.png)

### Lights off

quando ocupação da cozinha é **desligada**:
- deliga luzes

![img_3.png](img_3.png)

### Eletrodomesticos On

quando ocupação da cozinha é **ligada**:
- se sleep da cozinha desligado
- liga maquina de café
- liga maquina da loiça

![img_6.png](img_6.png)

### Eletrodomesticos Off

quando ocupação da cozinha é **desligada**:
- desliga maquina de café
- desliga microondas

![img_4.png](img_4.png)


### Ocupação

quando qualquer uma das condições se verifica -> ocupação da cozinha é **ligada**
- porta frigorifico aberta
- porta congelador aberta
- porta microondas aberta
- microondas em funcionamento
- maquina de cafe em funcionmento
- sensor PIR
- luz ligada


![img_5.png](img_5.png)