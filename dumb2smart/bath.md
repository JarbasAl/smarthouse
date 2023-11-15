# Bath

![imagem](https://github.com/JarbasAl/smarthouse/assets/33701864/5aa484bf-c65c-42f8-9656-a6431de09003)

Estimate a `bath_probability` based on:
- PIR in bathtub
- Water leak in bathtub
- sudden spikers in humidity or temperature

![imagem](https://github.com/JarbasAl/smarthouse/assets/33701864/adadc84c-b2c7-4368-b105-eb8475924c17)
![imagem](https://github.com/JarbasAl/smarthouse/assets/33701864/76dbc542-03af-40cc-bc5c-fd20f2760570)

## Sensor

Template
```
{% set prob = 0.0 %}
{% if states('binary_sensor.agua_no_banho_water_leak') == "on" %}
{% set prob = prob + 0.5 %}
{% endif %}
{% if states('sensor.humidity_derivative_wc') | float >= 0.005 %}
{% set prob = prob + 0.1 %}
{% endif %}
{% if states('sensor.humidity_derivative_wc') | float >= 0.01 %}
{% set prob = prob + 0.05 %}
{% endif %}
{% if states('sensor.temperature_derivative_wc') | float >= 0.1 %}
{% set prob = prob + 0.05 %}
{% endif %}
{% if states('sensor.temperature_derivative_wc') | float >= 0.2 %}
{% set prob = prob + 0.1 %}
{% endif %}
{% if states('sensor.temperature_derivative_wc') | float >= 0.3 %}
{% set prob = prob + 0.05 %}
{% endif %}
{% if states('binary_sensor.wc_banheira_occupancy') == "on" %}
{% set prob = prob + 0.15 %}
{% endif %}
{{prob * 100}}
```

