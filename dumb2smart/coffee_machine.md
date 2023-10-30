# Coffee Machine

![img_1.png](img_1.png)

# Usage - binary sensor

detect power usage from smart plug, above a certain value we know machine is in use

![img_2.png](img_2.png)


# State sensor

![img.png](img.png)

- turn on smart plug -> heating
- after 40 seconds -> ready
- on usage -> coffee
- on no usage -> ready
- after 2 minutes of no usage -> turn off smart plug


# Inventory

when state changes to coffee -> deduct 1 coffee from inventory

update timestamp of last coffee

