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

### Measurement 1: 0g

<table>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/e3b9d70f-6f4d-42a5-a338-9fa6f00e922e" alt="Measurement 1 Graph" style="width: 600px;">
    </td>
    <td>
      <table>
        <thead>
          <tr>
            <th>Received Value</th>
            <th>Weight</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>3123</td><td>0g</td></tr>
          <tr><td>3125</td><td>0g</td></tr>
          <tr><td>3120</td><td>0g</td></tr>
          <tr><td>3122</td><td>0g</td></tr>
          <tr><td>3120</td><td>0g</td></tr>
          <tr><td>3122</td><td>0g</td></tr>
          <tr><td>3120</td><td>0g</td></tr>
          <tr><td>3120</td><td>0g</td></tr>
          <tr><td>3122</td><td>0g</td></tr>
          <tr><td>3125</td><td>0g</td></tr>
        </tbody>
      </table>
    </td>
  </tr>
</table>

### Measurement 2: 250g

<table>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/1e0fb42f-4274-4027-a58d-48fbb0baf89a" alt="Measurement 2 Graph" style="width: 600px;">
    </td>
    <td>
      <table>
        <thead>
          <tr>
            <th>Received Value</th>
            <th>Weight</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>3229</td><td>249g</td></tr>
          <tr><td>3231</td><td>249g</td></tr>
          <tr><td>3228</td><td>248g</td></tr>
          <tr><td>3227</td><td>254g</td></tr>
          <tr><td>3231</td><td>257g</td></tr>
          <tr><td>3230</td><td>260g</td></tr>
          <tr><td>3232</td><td>259g</td></tr>
          <tr><td>3230</td><td>250g</td></tr>
          <tr><td>3227</td><td>242g</td></tr>
          <tr><td>3234</td><td>263g</td></tr>
        </tbody>
      </table>
    </td>
  </tr>
</table>

### Measurement 3: 500g

<table>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/d7e6476f-0b87-42c3-b6bb-4f56d2f850d2" alt="Measurement 3 Graph" style="width: 600px;">
    </td>
    <td>
      <table>
        <thead>
          <tr>
            <th>Received Value</th>
            <th>Weight</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>3319</td><td>486g</td></tr>
          <tr><td>3324</td><td>494g</td></tr>
          <tr><td>3328</td><td>499g</td></tr>
          <tr><td>3327</td><td>495g</td></tr>
          <tr><td>3331</td><td>505g</td></tr>
          <tr><td>3329</td><td>492g</td></tr>
          <tr><td>3329</td><td>516g</td></tr>
          <tr><td>3334</td><td>511g</td></tr>
          <tr><td>3331</td><td>516g</td></tr>
          <tr><td>3238</td><td>522g</td></tr>
        </tbody>
      </table>
    </td>
  </tr>
</table>

### Measurement 4: 750g

<table>
  <tr>
    <td>
        <img src="https://github.com/user-attachments/assets/97193a1d-c43d-4551-b1bc-fc05bccfa2da" alt="Measurement 4 Graph" style="width: 600px;">
    </td>
    <td>
      <table>
        <thead>
          <tr>
            <th>Received Value</th>
            <th>Weight</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>3434</td><td>731g</td></tr>
          <tr><td>3439</td><td>765g</td></tr>
          <tr><td>3414</td><td>713g</td></tr>
          <tr><td>3419</td><td>752g</td></tr>
          <tr><td>3435</td><td>761g</td></tr>
          <tr><td>3435</td><td>745g</td></tr>
          <tr><td>3428</td><td>730g</td></tr>
          <tr><td>3435</td><td>763g</td></tr>
          <tr><td>3426</td><td>741g</td></tr>
          <tr><td>3439</td><td>762g</td></tr>
        </tbody>
      </table>
    </td>
  </tr>
</table>





## Let's compare both results

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

| Time (in seconds) | 0 g | 240 - 260 g | 480 - 520 g | 730 -770 g |
|-------------------|-----------------|------------------|------------------|------------------|
| 1                 | 3123            | 3229             | 3319             | 3434             |
| 2                 | 3125            | 3231             | 3324             | 3439             |
| 3                 | 3120            | 3228             | 3328             | 3414             |
| 4                 | 3122            | 3227             | 3327             | 3419             |
| 5                 | 3120            | 3231             | 3331             | 3435             |
| 6                 | 3122            | 3230             | 3329             | 3435             |
| 7                 | 3120            | 3232             | 3329             | 3428             |
| 8                 | 3120            | 3230             | 3334             | 3435             |
| 9                 | 3122            | 3227             | 3331             | 3426             |
| 10                | 3125            | 3234             | 3238             | 3439             |


### Initial observation

The most obvious thing we noticed from the get go is that the values for the same/similar weights are very different. That is because the finger probably surface was smaller which resulted in more force applied on a smaller surface area, in fact that is one of the requierement in the official guidelines on how ot use fsr402 sensors: 

```
Provide a consistent force distribution. FSR response is very sensitive to the distribution of the applied force. In general, this precludes the use of dead weights for characterization since exact duplication of the weight

distribution is rarely repeatable cycle-to-cycle. A consistent weight (force) distribution is more difficult to achieve than merely obtaining a consistent total applied weight (force). As long as the distribution is the same

cycle-to-cycle, then repeatability will be maintained. The use of a thin elastomer between the applied force and the FSR can help absorb error from inconsistent force distributions.
```


### Calculating the standard deviation
For the first method(equally distirbuted) we simply apply the fomrula over the given measurement, where with the second(finger menthod) we calculte the standard diviation over a set of given ranges, honestly considering the sensors predetermined error, those values are negliable


### Pearson correlation coefficient
Coincidentally enough, I already calcualted the standard deviation for both sets before stumbilig upon the Idea for [Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) that was found while browsing [stackoverflow](https://stackoverflow.com/questions/47402209/how-to-find-correlation-between-two-values)

stavi sad pearsons, to je kombinacija standardne i covariance, na kraju razlozi obadvoje

### Conclusion

Kaj se tu sad desilo je da je makar je equally distirbuted metoda bolja, tocnija i standard deviatio nje mnogo manje i dalje je tu problem da bu jednostavno krive vrijednosti pokazival za prst, jer jedinostavno nije kalibriran za taj dio, i to je tocno ono kaj  smo govoirlil na prvom djelu ovog naseg teksta, taj sensor je napravljen za prste, so probably for the sake fo getting somewhat dobre vrijednosti bumo morali uporabiti manje tocniju metdu, samo da dobimo toncije vrijednosti

another idea is that we could use, (because of lineararity), is that we use the 2nd values for ranges from 240-260 as our starting point, where we could perhaps get more accurate measurements, clearly becauase our accureacy(measured by Standard deviation) was lower as the weight increased(because using the finger to distributed weight was getting harder and harder)



## Methods used for each segment
- ### Plotting graphs

    This script was used to generate graphs 

    ```Python
    import matplotlib.pyplot as plt
    
    # Your data
    data = [3248, 3238, 3238, 3237, 3245, 3245, 3245, 3243, 3239, 3245]
    
    # Time points (assuming one value per second)
    time = list(range(1, len(data) + 1))
    
    # Create the plot
    plt.figure(figsize=(8, 4))
    plt.plot(time, data, marker='o', color='b', linestyle='-', linewidth=2, markersize=5)
    
    # Add titles and labels
    plt.title('Received Values Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Received Value')
    
    # Save the plot as an image
    plt.savefig('received_values_plot.png')
    
    # Show the plot
    plt.show()
    ```




