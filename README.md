# Short Comparative Analysis of Human Touch and Centered Weight Measurements on an FSR402 Sensor
## About FSR402 (Force Sensing Resistor)
As suggested by its name, an FSR sensor reacts to force. More precisely, it acts as a "resistor" that changes its resistance when force is applied. The more force applied, the less resistance it exhibits.<br /> 


This sensor is not precise and is not intended for use in precise applications. It primarily works well with human touch, with an error margin of about 5% to 25%, when doing repeated tests though, it's closer to
15% - 25%.
## Hypothesis:
The FSR402 sensor, which is designed for human touch, may struggle to consistently measure pressure or weight due to variations in finger surface area and force distribution. This inconsistency arises from the natural variability in human touch, what that means is that, the force sensor has issues with precisely measuring circular/uneaven surfaces, due to it's nature, making it challenging to achieve a controlled and accurate test environment. However, when using standardized weights with consistent surface contact, the sensor is likely to provide more reliable and reproducible measurements, as the distribution of pressure is more uniform and controlled.
We've already talked about measurements deviating for about 5% - 25%, we're hoping not to go over the 25% error mark, and the sensor will probably work more accurately if we apply the force equally across the acrive surface of the sensor
## How to approach measurements

As you get the sensor working, you'll initially see values that represent nothing. However, you'll notice an obvious change when pressure is applied to the sensor, resulting in higher values. To give these values meaning, we need to calibrate the sensor to a known standard. In this case, we'll compare the sensor readings to values in kilograms. As previously discussed in the hypothesis, we'll start with equally distirbuted measurement, because it will probably give us more accurate measurements.

We will approach this using three different methods: first, by applying equally distributed weight; second, by simply placing a finger on the sensor; and lastly, by using the same rubber from the first method to better distribute the finger's weight.
- ### Three separate measurement techniques:
    - Equally distributed weight
    - Finger placed directly on sensor
    - Equally distributed finger's weight

## First measurement: Equally distributed measurement

### <b>Measurement 1: 0g</b><br />
Received values: 3120, 3119, 3118, 3127, 3119, 3120, 3120, 3120, 3120, 3120

- Resulting in a <b>average</b> of: 3120.3
![Figure_1](https://github.com/user-attachments/assets/7229b94f-b077-4766-b81f-fe95ebeef32c)


### <b>Measurement 2: 250g</b><br />
Received values:3138, 3137, 3139, 3139, 3139, 3138, 3137, 3138, 3137, 3138

- Resulting in a <b>average</b> of: 3138.0
![Figure_2](https://github.com/user-attachments/assets/8bae13fd-5d5b-44db-bd09-db211684213e)


### <b>Measurement 3: 500g</b><br />
Received values:3180, 3177, 3179, 3179, 3184, 3183, 3184, 3179, 3184, 3183

- Resulting in a </b>average</b> of: 3181.2
![Figure_3](https://github.com/user-attachments/assets/00d4e78a-690f-4696-b097-6a1373135aef)


### <b>Measurement 4: 750g</b><br />
Received values: 3248, 3238, 3238, 3237, 3245, 3245, 3245, 3243, 3239, 3245

- Resulting in a <b>average</b> of: 3242.3
- Notes:
  - The measurements for 750g show greater fluctuations, likely due to instability during the measuring process or - the heavier the shitter arguement
    
![Figure_4](https://github.com/user-attachments/assets/8e55ea92-de60-4f5f-b17e-cd488af81845)

## Second measurement: Finger placed directly on sensor

### <b>Measurement 1: 0g</b><br />
Received value: 3122
Received value: 3120
Received value: 3121
Received value: 3120
Received value: 3123
Received value: 3122
Received value: 3126
Received value: 3121
Received value: 3120
Received value: 3118
Received value: 3120
Received value: 3121
Received value: 3123
Received value: 3125
Received value: 3120
Received value: 3122
Received value: 3120
Received value: 3122
Received value: 3120
Received value: 3120
Received value: 3122
Received value: 3125

### <b>Measurement 2: 250g</b><br />

Received value: 3229
Received value: 3231
Received value: 3228
Received value: 3227
Received value: 3231
Received value: 3230
Received value: 3232
Received value: 3230
Received value: 3227
Received value: 3234

### <b>Measurement 3: 500g</b><br />
Received value: 3319
Received value: 3324
Received value: 3328
Received value: 3327
Received value: 3331
Received value: 3329
Received value: 3329
Received value: 3334
Received value: 3331
Received value: 3238

### <b>Measurement 4: 750g</b><br />
Received value: 3434
Received value: 3439
Received value: 3414
Received value: 3419
Received value: 3435
Received value: 3435
Received value: 3428
Received value: 3435
Received value: 3426
Received value: 3439




### Structured Data
tu budem usporedil sve dvije(tri - ako ukljucim jos ono prst+gumica)  da vidimo kolki je deviation od svega

|**Time(in seconds)**| **0 g** | **250 g** | **500 g** | **750 g** |
|-----------|-----------|-----------|-----------|-----------|
|1          | 3120      | 3138      | 3180      | 3248      |
|2          | 3119      | 3137      | 3177      | 3238      |
|3          | 3118      | 3139      | 3179      | 3238      |
|4          | 3127      | 3139      | 3179      | 3237      |
|5          | 3119      | 3139      | 3184      | 3245      |
|6          | 3120      | 3138      | 3183      | 3245      |
|7          | 3120      | 3137      | 3184      | 3245      |
|8          | 3120      | 3138      | 3179      | 3243      |
|9          | 3120      | 3137      | 3184      | 3239      |
|10         | 3120      | 3138      | 3183      | 3245      |

Idea for [Pearson's average](https://stackoverflow.com/questions/47402209/how-to-find-correlation-between-two-values) was found while browsing [stackoverflow](https://stackoverflow.com/questions/47402209/how-to-find-correlation-between-two-values)




