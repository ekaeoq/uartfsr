# Short Comparative Analysis of Human Touch and Centered Weight Measurements on an FSR402 Sensor
## About FSR402 (Force Sensing Resistor)
As suggested by its name, an FSR sensor reacts to force. More precisely, it acts as a "resistor" that changes its resistance when force is applied. The more force applied, the less resistance it exhibits.<br>


This sensor is not precise and is not intended for use in precise applications. It primarily works well with human touch, with an error margin of about 5% to 25%, when doing repeated tests though, it's closer to
15% - 25%.

0g
(base) ekaeo@es-MacBook-Pro:TOUCHCAP_sensor/uartfsr ‹main›$ python3 uarttest.py
Received value: 3119
Received value: 3120
Received value: 3120
Received value: 3119
Received value: 3118
Received value: 3127
Received value: 3119
Received value: 3120
Received value: 3120
Received value: 3120
Received value: 3120
Received value: 3120
^CProgram terminated by user
Serial port closed
250g
(base) ekaeo@es-MacBook-Pro:TOUCHCAP_sensor/uartfsr ‹main›$ python3 uarttest.py
Received value: 3133
Received value: 3136
Received value: 3135
Received value: 3139
Received value: 3137
Received value: 3140
Received value: 3136
Received value: 3135
Received value: 3142
Received value: 3137
Received value: 3136
Received value: 3138
Received value: 3138
Received value: 3131
Received value: 3138
Received value: 3138
Received value: 3138
Received value: 3117
Received value: 3138
Received value: 3138
Received value: 3137
Received value: 3139
Received value: 3139
Received value: 3139
Received value: 3138
Received value: 3137
Received value: 3138
Received value: 3137
Received value: 3138
^CProgram terminated by user
Serial port closed
500g
(base) ekaeo@es-MacBook-Pro:TOUCHCAP_sensor/uartfsr ‹main›$ python3 uarttest.py
Received value: 3179
Received value: 3180
Received value: 3178
Received value: 3175
Received value: 3173
Received value: 3181
Received value: 3179
Received value: 3182
Received value: 3180
Received value: 3177
Received value: 3179
Received value: 3179
Received value: 3184
Received value: 3183
Received value: 3184
Received value: 3179
Received value: 3184
Received value: 3183
^CProgram terminated by user
Serial port closed

