import numpy as np

def pearson_correlation(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sqrt(np.sum((x - x_mean)**2) * np.sum((y - y_mean)**2))
    
    correlation = numerator / denominator
    return correlation

# Data for the time series and measured values
time = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
weights = [0, 250, 500, 750]  # These are the fixed weights from the first dataset

# First table (baseline with specific weights)
values_baseline = np.array([
    [3120, 3138, 3180, 3248],
    [3119, 3137, 3177, 3238],
    [3118, 3139, 3179, 3238],
    [3127, 3139, 3179, 3237],
    [3119, 3139, 3184, 3245],
    [3120, 3138, 3183, 3245],
    [3120, 3137, 3184, 3245],
    [3120, 3138, 3179, 3243],
    [3120, 3137, 3184, 3239],
    [3120, 3138, 3183, 3245]
])

# Calculate Pearson correlation for each weight
for i, weight in enumerate(weights):
    correlation = pearson_correlation(values_baseline[:, i], time)
    print(f"Pearson correlation for weight {weight} g: {correlation}")

# Now, handle the new data with weight ranges
# Define midpoints for weight ranges
weights_with_ranges = [0, 250, 500, 750]  # Midpoints for the ranges: [240-260], [480-520], [730-770]

# Second table (new dataset with weight ranges)
values_with_ranges = np.array([
    [3123, 3229, 3319, 3434],
    [3125, 3231, 3324, 3439],
    [3120, 3228, 3328, 3414],
    [3122, 3227, 3327, 3419],
    [3120, 3231, 3331, 3435],
    [3122, 3230, 3329, 3435],
    [3120, 3232, 3329, 3428],
    [3120, 3230, 3334, 3435],
    [3122, 3227, 3331, 3426],
    [3125, 3234, 3238, 3439]
])

# Calculate Pearson correlation for each weight range
for i, weight in enumerate(weights_with_ranges):
    correlation = pearson_correlation(values_with_ranges[:, i], time)
    print(f"Pearson correlation for weight range {weight} g: {correlation}")

