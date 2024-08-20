import matplotlib.pyplot as plt
import pandas as pd

# Sample data
# Replace these lists with your actual data
time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Time in seconds
sensor_values = [3434, 3439, 3414, 3419, 3435, 3435, 3428, 3425, 3426, 3439]  # Sensor readings
force_in_grams = [731, 765, 713, 752, 761, 745, 730, 763, 741, 762]  # Force in grams

# Create a figure and a set of subplots with two y-axes
fig, ax1 = plt.subplots()

# Plot sensor values on the first y-axis
ax1.plot(time, sensor_values, 'b-', label='Sensor Value')
ax1.set_xlabel('Time (seconds)')
ax1.set_ylabel('Sensor Value', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Create a second y-axis that shares the same x-axis
ax2 = ax1.twinx()
ax2.plot(time, force_in_grams, 'r-', label='Force in Grams')
ax2.set_ylabel('Force in Grams', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Add a title
plt.title('Sensor Values and Corresponding Force Over Time')

# Show a legend
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Show the plot
plt.show()

