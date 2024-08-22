import numpy as np

def pearson_correlation(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sqrt(np.sum((x - x_mean)**2) * np.sum((y - y_mean)**2))
    
    correlation = numerator / denominator
    return correlation
#x = [3121.9, 3229.9, 3319.0, 3430.4]
x = [3120.3, 3138.0, 3181.2, 3242.3]
y = [0, 250, 500, 750]

result = pearson_correlation(x, y)
print(f"Pearson correlation coefficient: {result}")
