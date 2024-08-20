import pandas as pd
import numpy as np

# Data for equally distributed weight method
data_distributed = {
    'Time (s)': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    '0g': [3120, 3119, 3118, 3127, 3119, 3120, 3120, 3120, 3120, 3120],
    '250g': [3138, 3137, 3139, 3139, 3139, 3138, 3137, 3138, 3137, 3138],
    '500g': [3180, 3177, 3179, 3179, 3184, 3183, 3184, 3179, 3184, 3183],
    '750g': [3248, 3238, 3238, 3237, 3245, 3245, 3245, 3243, 3239, 3245],
}

df_distributed = pd.DataFrame(data_distributed)

# Calculate standard deviation for each weight
std_distributed = df_distributed[['0g', '250g', '500g', '750g']].std()
print("Standard Deviation for Equally Distributed Weight Method:")
print(std_distributed)

# Data for finger measurement method
data_finger = {
    'Received Value': [3123, 3125, 3120, 3122, 3120, 3122, 3120, 3120, 3122, 3125,
                       3229, 3231, 3228, 3227, 3231, 3230, 3232, 3230, 3227, 3234,
                       3319, 3324, 3328, 3327, 3331, 3329, 3329, 3334, 3331, 3238,
                       3434, 3439, 3414, 3419, 3435, 3435, 3428, 3435, 3426, 3439],
    'Weight': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               249, 249, 248, 254, 257, 260, 259, 250, 242, 263,
               486, 494, 499, 495, 505, 492, 516, 511, 516, 522,
               731, 765, 713, 752, 761, 745, 730, 763, 741, 762],
}

df_finger = pd.DataFrame(data_finger)

# Function to calculate standard deviation for each weight group
def calculate_std_for_group(df, target_weight_range):
    group = df[(df['Weight'] >= target_weight_range[0]) & (df['Weight'] <= target_weight_range[1])]
    return group['Received Value'].std()

# Define the target weight ranges (0g, 250g, 500g, 750g)
weight_ranges = [(0, 0), (240, 260), (480, 520), (730, 770)]
std_finger = {}

for i, weight_range in enumerate(weight_ranges):
    std_finger[f'{np.mean(weight_range)}g'] = calculate_std_for_group(df_finger, weight_range)

print("\nStandard Deviation for Finger Measurement Method:")
print(std_finger)

