## House Tree View


               WC da Dii
                  |
           Escritorio da Dii
                  |
              Marquise
                  |
              Cozinha
                 |
             Corredor 1
             |        |
           Sala    Corredor 2
                  |     |        |
            ManCave  Escritorio  Corredor 3
                                 |    |     |
                                WC   Quarto Quarto Hugo




## Occupancy

create a sensor for each room
```
  - trigger:
    - platform: event
      event_type: people_sala_update
    binary_sensor:
      - name: "people_in_sala"
        state: "{{ trigger.event.data.state }}"
        icon: "mdi:home-account"
        device_class: "occupancy"
```
`
![imagem](https://user-images.githubusercontent.com/33701864/278898711-c8c6ec8c-7868-4ebf-86b1-805d486d1fcd.png)

### PIR based occupancy detection

create automations to set the state of sensors created above
```
event: people_escritorio_update
event_data:
  state: "on"
```

automations overview


               WC da Dii <- people_wc_dii_update:ON + people_escritorio_dii_update:OFF
                  |
           Escritorio da Dii <- people_escritorio_dii_update:ON + people_wc_dii_update:OFF + people_marquise_update:OFF
                  |
              Marquise  <- people_marquise_update:ON + people_escritorio_dii_update:OFF + people_kitchen_update:OFF
                  |
              Cozinha <- people_kitchen_update:ON + people_marquise_update:OFF
                 |
             Corredor 1   <- people_sala_update:OFF + people_kitchen_update:OFF
             |        |
           Sala       |   <- people_sala_update:ON
                 Corredor 2 <- people_mancave_update:OFF + people_escritorio_update:OFF
                  |     |      |
            ManCave     |      | <- people_mancave_update:ON
                  Escritorio   | <- people_escritorio_update:ON
                               Corredor 3 <- people_wc_update:OFF + people_quarto_update:OFF + people_quarto_hugo_update:OFF
                                 |  |     |
                                WC  |     | <- people_wc_update:ON
                                   Quarto |  <- people_quarto_update:ON
                                          Quarto Hugo <- people_quarto_hugo_update:ON


Extra occupancy sensors -> people_XXX_update:ON

- window state changes
- light turned on
- closet door open
- electrodomestic usage detected (coffee machine, microwave, fridge door...)
- media playback detected (chromecast, spotify...)
