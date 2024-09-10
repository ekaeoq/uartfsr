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
            <th>Sensor Values</th>
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
- Resulting in a <b>average</b> of: 3121.9

### Measurement 2: ~250g

<table>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/1e0fb42f-4274-4027-a58d-48fbb0baf89a" alt="Measurement 2 Graph" style="width: 600px;">
    </td>
    <td>
      <table>
        <thead>
          <tr>
            <th>Sensor Values</th>
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
- Resulting in a <b>average</b> of: 3229.9

### Measurement 3: ~500g

<table>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/d7e6476f-0b87-42c3-b6bb-4f56d2f850d2" alt="Measurement 3 Graph" style="width: 600px;">
    </td>
    <td>
      <table>
        <thead>
          <tr>
            <th>Sensor Values</th>
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
- Resulting in a <b>average</b> of: 3319

### Measurement 4: ~750g

<table>
  <tr>
    <td>
        <img src="https://github.com/user-attachments/assets/97193a1d-c43d-4551-b1bc-fc05bccfa2da" alt="Measurement 4 Graph" style="width: 600px;">
    </td>
    <td>
      <table>
        <thead>
          <tr>
            <th>Sensor Values</th>
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
- Resulting in a <b>average</b> of: 3430.4





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
For the first method(equally distirbuted weight) we simply apply the fomrula over the given measurement, where with the second(finger placed directly on sensor) we calculte the standard diviation over a set of given ranges, that we must do simply because of the nature of how we place our finger on the sensor, it is also very hard to account for the already mentioned active surface, rather it's hard to determine what exact surface of the finer is being placed on top of the active area, taking all that into consideration, honestly with the sensors predetermined error, those values are negliable

##### Example:
Let's calculate the standard deviation for the fixed weight of 250g as well as for the range of 240-260g
- Equally distributed weight:
  
    ${Mean} = \frac{3138 + 3137 + 3139 + 3139 + 3139 + 3138 + 3137 + 3138 + 3137 + 3138}{10} = 3138$
    
    ${Variance} = \frac{(3138 - 3138)^2 + (3137 - 3138)^2 + (3139 - 3138)^2 + \dots + (3138 - 3138)^2}{10}$
    
    ${Variance} = \frac{(0)^2 + (-1)^2 + (1)^2 + (1)^2 + (1)^2 + (0)^2 + (-1)^2 + (0)^2 + (-1)^2 + (0)^2}{10} = \frac{6}{10} = 0.6$
    
    ${Standard Deviation} = \sqrt{\text{Variance}} = \sqrt{0.6} \approx 0.775$

</br>

- Finger placed directly on sensor:
  
    ${Mean} = \frac{3228 + 3229 + 3230 + 3231 + 3234 + 3227 + 3227 + 3231 + 3232 + 3230}{10} \approx 3230$
    
    ${Variance} = \frac{(3228 - 3230)^2 + (3229 - 3230)^2 + (3230 - 3230)^2 + \dots + (3230 - 3230)^2}{10}$
    
    ${Variance} = \frac{(-2)^2 + (-1)^2 + (0)^2 + (1)^2 + (4)^2 + (-3)^2 + (-3)^2 + (1)^2 + (2)^2 + (0)^2}{10} = \frac{45}{10} = 4.5$
    
    ${Standard Deviation} = \sqrt{\text{Variance}} = \sqrt{4.5} \approx 2.12$

We repeat the process for each set of values and get all the standard deviation values, the values slightly deviate from the ones calculated with a python script, due to rounding up
#### Standard deviation for all sets of measurements:

- Standard Deviation for Equally Distributed Weight Method:

    <b>0 g:</b>     2.451757
    
    <b>250 g:</b>     0.816497
    
    <b>500 g:</b>     2.658320
    
    <b>750 g:</b>     3.917199

- Standard Deviation for Finger Measurement Method:

    <b>0 g:</b>  1.9692073983655907
    
    <b>240 - 260 g:</b>  1.8104634152000358
    
    <b>480 - 520 g:</b>  4.387482193696061
    
    <b>730 - 770 g:</b>  6.610177338350647



### Pearson correlation coefficient
Coincidentally enough, I already calcualted the standard deviation for both sets before stumbilig upon the idea for [Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) that was found while browsing [stackoverflow](https://stackoverflow.com/questions/47402209/how-to-find-correlation-between-two-values)

Simply put, Pearson correlation coefficient is a way of determining **how** linear 2 sets of data are, using this simple python script we calucated the correlation between our 2 sets of data for both methods used:

 ```Python
import numpy as np

def pearson_correlation(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sqrt(np.sum((x - x_mean)**2) * np.sum((y - y_mean)**2))
    
    correlation = numerator / denominator
    return correlation

x = [3120.3, 3138.0, 3181.2, 3242.3]
y = [0, 250, 500, 750]

result = pearson_correlation(x, y)
print(f"Pearson correlation coefficient: {result}")
```

From what I've read, there's a certain threshold to determine what makes a system linear, usually that would be deviations less than 0.05, meaning our system shouldn't have a pearson's coefficient lower than 95. That threshold can obviously vary system to system, the same way any system is obviously less or more linear.

In our case, we end up with these values:
- Equally distributed weight
  
    Pearson correlation coefficient: 0.9728523094748889
  
- Finger placed directly on sensor
  
    Pearson correlation coefficient: 0.9991485447127495

### Conclusion and Results

Based on everything provided thus far, the reasults we got were surprisingly better than expected, or at the very least better than the 5 - 25 % we were expecting, obviously we shouldn't take Pearson's correlation at face value, because taking the mean of mean for data ranges isn't the most accurate practice, which is highlighted in standard deviations for the said method. Another thing that we can notice is, that the error becomes progressively bigger as we increase that force, while it is nowhere explicity stated in the FSR402 Guide, we can clearly see that the more force we apply the harder it become for the sensor to distinguish those chagnes, inevertably making it less accurate, chat-gpt best described this as:

"In summary, while the document doesn't directly state that the sensor gets less accurate with higher forces, the described saturation effect suggests that the sensor becomes less responsive and potentially less reliable in distinguishing between different high forces. This could be interpreted as a form of reduced accuracy at higher force levels."

##### Unexpected issue
One issue that arried that I did not think of before hand, is that we have different values for the same weight between the 2 methods. While the equally distributed weight method proved more accurate and consistent, with lower standard deviation, it created a dilemma. This method, though precise, doesn't really reflect the sensor's intended use for human touch. Creating different sensor values for the same weight. The difficulty in achieving equally distributed weight with a finger also explains the higher sensor values in finger-based measurements. 

We've come to a point where, despite the equally distributed method's superior accuracy, we must prioritize the finger-based method for practical applications to better represent the sensor's intended use. Notably, accuracy decreased as applied weight increased, particularly for the finger-based method, suggesting consistent pressure distribution becomes more challenging with higher weights. In conclusion, while equally distributed weight testing provided more consistent results, the finger-based method remains crucial for real-world applications of the FSR402 sensor. Future work could explore improving finger-based measurement techniques or developing hybrid approaches that balance accuracy with practical usability.

All this, to say, that the limit to how accurate this whole comparisson is, comes down to how accurate my scale was.

- This is all wrong:D, or at least I should've taken the resistor value approach, where pull-down resistor is being taking into account when doing measurements, another thing that I've noticed when rewiring the circuit, although being very logical, I didn't think it would affect the circuit that significantly, but more wire == higher resistance:O
  
## Re-do
Any case values we've gotten would've been scaled anyhow, so that's not that cruicial, of course this is more about the approach rather than the values itself, because the value we get from the sensor is the only one that not constant, after calculating the pull-downresistance:

```Python
float R_fsr = R_fixed * (V_in / V_out - 1);
```
I've come to find out that the raw values pretty much correspond with those of the resistance(this probably just me being dumb but thats probably the shit sensor gives us in the first place so bruh), anyyyways, we have higer values when no force is being applied, as we should, we have lower resistance, and most importantly we have right about 1k ohms of resistance right at the 1000g mark, so this would probably work pretty well, even without any calibration, anyways, this is our new starting point 

<img width="798" alt="Screenshot 2024-09-04 at 19 30 02" src="https://github.com/user-attachments/assets/11bdd16b-51d3-4c2b-803b-914b97b6c8ed">

Calculating out output voltage also corresponds with this graph:
- example:
    based on this fomrula:
  
     $$V_{OUT} = \frac{R_M \cdot V}{R_M + R_{FSR}}$$
  
    - $V_{OUT} = \frac{10000 \cdot V3.3}{10000 + 3200\ohm}$
    &nbsp;&nbsp; $V_{OUT} = 2.5V $

    - $V_{OUT} = \frac{10000 \cdot V3.3}{10000 + 1100\ohm}$
    &nbsp;&nbsp; $V_{OUT} = 2.99V $

    - $V_{OUT} = \frac{10000 \cdot V3.3}{10000 + 10\ohm}$
    &nbsp;&nbsp; $V_{OUT} = 3.29V $

### Measurement 1: ~250g

<table>
  <tr>
    <td>
        <img src="https://github.com/user-attachments/assets/ba120c94-1ea1-44a3-8d72-0df2fdf33a72" alt="Measurement 4 Graph" style="width: 600px;">
    </td>
    <td>
      <table>
        <thead>
          <tr>
            <th>Sensor Values</th>
            <th>Weight</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>2721.3</td><td>247g</td></tr>
          <tr><td>2725.2</td><td>248g</td></tr>
          <tr><td>2717.3</td><td>249g</td></tr>
          <tr><td>2713.4</td><td>250g</td></tr>
          <tr><td>2749.0</td><td>241g</td></tr>
          <tr><td>2725.2</td><td>250g</td></tr>
          <tr><td>2721.3</td><td>251g</td></tr>
          <tr><td>2713.4</td><td>256g</td></tr>
          <tr><td>2725.2</td><td>253g</td></tr>
          <tr><td>2723.4</td><td>249g</td></tr>
          <tr><td>2693.4</td><td>260g</td></tr>
          <tr><td>2713.4</td><td>251g</td></tr>
          <tr><td>2721.3</td><td>248g</td></tr>
          <tr><td>2705.5</td><td>253g</td></tr>
          <tr><td>2717.3</td><td>248g</td></tr>
          <tr><td>2713.4</td><td>248g</td></tr>
          <tr><td>2713.4</td><td>251g</td></tr>
          <tr><td>2689.8</td><td>253g</td></tr>
          <tr><td>2717.9</td><td>249g</td></tr>
          <tr><td>2713.2</td><td>248g</td></tr>
        </tbody>
      </table>
    </td>
  </tr>
</table>

- Resulting in a <b>average</b> of: 2716.67

### Measurement 2: ~500g

<table>
  <tr>
    <td>
        <img src="https://github.com/user-attachments/assets/927f70a7-841f-4f10-a886-152b440b5485" alt="Measurement 4 Graph" style="width: 600px;">
    </td>
    <td>
      <table>
        <thead>
          <tr>
            <th>Sensor Values</th>
            <th>Weight</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>2338.0</td><td>481g</td></tr>
          <tr><td>2323.0</td><td>487g</td></tr>
          <tr><td>2345.5</td><td>477g</td></tr>
          <tr><td>2308.3</td><td>495g</td></tr>
          <tr><td>2309.3</td><td>491g</td></tr>
          <tr><td>2323.2</td><td>479g</td></tr>
          <tr><td>2300.9</td><td>491g</td></tr>
          <tr><td>2289.9</td><td>500g</td></tr>
          <tr><td>2271.5</td><td>506g</td></tr>
          <tr><td>2267.8</td><td>499g</td></tr>
          <tr><td>2300.0</td><td>494g</td></tr>
          <tr><td>2267.8</td><td>500g</td></tr>
          <tr><td>2267.8</td><td>490g</td></tr>
          <tr><td>2271.5</td><td>493g</td></tr>
          <tr><td>2220.2</td><td>523g</td></tr>
          <tr><td>2234.4</td><td>519g</td></tr>
          <tr><td>2249.4</td><td>512g</td></tr>
          <tr><td>2264.1</td><td>517g</td></tr>
          <tr><td>2267.8</td><td>507g</td></tr>
          <tr><td>2271.5</td><td>497g</td></tr>
        </tbody>
      </table>
    </td>
  </tr>
</table>

- Resulting in a <b>average</b> of: 2284.60


### Measurement 3: ~750g

<table>
  <tr>
    <td>
        <img src="https://github.com/user-attachments/assets/b1ca4116-3c72-439f-b138-01490c8ce2ee" alt="Measurement 4 Graph" style="width: 600px;">
    </td>
    <td>
      <table>
        <thead>
          <tr>
            <th>Sensor Values</th>
            <th>Weight</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>1845.5</td><td>720g</td></tr>
          <tr><td>1818.1</td><td>725g</td></tr>
          <tr><td>1804.5</td><td>727g</td></tr>
          <tr><td>1710.0</td><td>789g</td></tr>
          <tr><td>1693.3</td><td>769g</td></tr>
          <tr><td>1703.3</td><td>740g</td></tr>
          <tr><td>1743.6</td><td>726g</td></tr>
          <tr><td>1736.8</td><td>736g</td></tr>
          <tr><td>1716.7</td><td>734g</td></tr>
          <tr><td>1689.9</td><td>749g</td></tr>
          <tr><td>1696.4</td><td>741g</td></tr>
          <tr><td>1656.7</td><td>750g</td></tr>
          <tr><td>1646.7</td><td>765g</td></tr>
          <tr><td>1703.3</td><td>746g</td></tr>
          <tr><td>1740.2</td><td>719g</td></tr>
          <tr><td>1730.1</td><td>726g</td></tr>
          <tr><td>1686.6</td><td>745g</td></tr>
          <tr><td>1696.6</td><td>734g</td></tr>
          <tr><td>1666.0</td><td>738g</td></tr>
          <tr><td>1636.7</td><td>742g</td></tr>
        </tbody>
      </table>
    </td>
  </tr>
</table>

- Resulting in a <b>average</b> of: 1716.05

  The results were just as good as we anticipated, in the grand scheme of things, still better than we anticipated, there’s a clear distinction between resistance values and force applied ans their correlation is not inversely proportional as god intended!!!

#### Standard deviation for all measurements:

- 250g weight range (240g - 260g): 12.20
- 500g weight range (480g - 520g): 27.13
- 750g weight range (730g - 770g): 28.34

These results are obviously worse than what we had previously, but still very acceptable

#### Calculating the slope

$$\text{Slope} = \frac{750g - 500g}{\text{Resistance at 750g} - \text{Resistance at 500g}}$$



$$\text{Slope} = \frac{750g - 500g}{1721.92 - 2284.60} = \frac{-562.68}{250g} = -2.25072$$


### Calculating our error


$$\text{Error in Weight} = \frac{\text{Error in Resistance}}{\text{Slope}} = \frac{28.34}{-2.25072} \approx -12.59 \text{ grams}$$


### Least Squares Regression: Step-by-Step Explanation

#### **Given Data Points:**

$$(x_1, y_1) = (2716.67, 0)$$

$$(x_2, y_2) = (2284.60, 500)$$ 

$$(x_3, y_3) = (1696.60, 750)$$

Where $x$ is the sensor value and $y$ is the weight in grams.

---

### **Step 1: Calculate Means**

- The mean of the $x$-values $\bar{x}$ and the mean of the $y$-values $\bar{y}$ are calculated as follows:


$$\bar{x} = \frac{x_1 + x_2 + x_3}{3} = \frac{2716.67 + 2284.60 + 1696.60}{3} = 2232.62$$

$$\bar{y} = \frac{y_1 + y_2 + y_3}{3} = \frac{0 + 500 + 750}{3} = 416.67$$

---

### **Step 2: Calculate Sums for the Slope**

To calculate the slope, we first need to compute the sums for $\Sigma(x - \bar{x})(y - \bar{y})$ and $\Sigma(x - \bar{x})^2 \$.

#### Calculate $(x - \bar{x})(y - \bar{y})$ for each point:

- For $(x_1, y_1)$:

$$(x_1 - \bar{x})(y_1 - \bar{y}) = (2716.67 - 2232.62)(0 - 416.67) = -201,649.69$$

- For $(x_2, y_2)$:

$$(x_2 - \bar{x})(y_2 - \bar{y}) = (2284.60 - 2232.62)(500 - 416.67) = 4,333.15$$

- For $(x_3, y_3)$:

$$(x_3 - \bar{x})(y_3 - \bar{y}) = (1696.60 - 2232.62)(750 - 416.67) = -178,653.46$$

- The sum is:

$$\Sigma(x - \bar{x})(y - \bar{y}) = -201,649.69 + 4,333.15 - 178,653.46 = -375,970.00$$

#### Calculate $(x - \bar{x})^2$ for each point:

- For $(x_1)$:

$$(x_1 - \bar{x})^2 = (2716.67 - 2232.62)^2 = 234,082.25$$

- For $(x_2)$:

$$(x_2 - \bar{x})^2 = (2284.60 - 2232.62)^2 = 2,704.04$$

- For $(x_3)$:

$$(x_3 - \bar{x})^2 = (1696.60 - 2232.62)^2 = 287,524.00$$

- The sum is:

$$\Sigma(x - \bar{x})^2 = 234,082.25 + 2,704.04 + 287,524.00 = 524,310.29$$


---

### **Step 3: Calculate the Slope ( $m$ )**

- Now, we can compute the slope using the formula:

$$m = \frac{\Sigma(x - \bar{x})(y - \bar{y})}{\Sigma(x - \bar{x})^2}$$


- Substitute the values:

$$m = \frac{-375,970.00}{524,310.29} = -0.7171$$


---

### **Step 4: Calculate the y-intercept ( $b$ )**

- The y-intercept is calculated using the formula:

$$b = \bar{y} - m\bar{x}$$

- Substitute the values:

$$b = 416.67 - (-0.7171 \times 2232.62) = 416.67 + 1601.18 = 2017.85$$


---

### **Step 5: Form the Linear Regression Equation**

- Finally, we can write the equation of the line:

$$y = mx + b$$

- Substitute the values of $m$ and $b$:

$$y = -0.7171x + 2017.85$$


---

This equation represents the line of best fit for the given data points.

![Figure_graph](https://github.com/user-attachments/assets/91082c43-716c-449d-8b1a-3e754f6286d5)
![Figure_together](https://github.com/user-attachments/assets/2d0ce133-67ef-4821-bd23-ce8dc850b7ee)







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
![Figure_3](https://github.com/user-attachments/assets/b1ca4116-3c72-439f-b138-01490c8ce2ee)
![Figure_2](https://github.com/user-attachments/assets/927f70a7-841f-4f10-a886-152b440b5485)
![Figure_1](https://github.com/user-attachments/assets/ba120c94-1ea1-44a3-8d72-0df2fdf33a72)




