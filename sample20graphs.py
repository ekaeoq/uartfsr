import matplotlib.pyplot as plt

# New data
samples = list(range(1, 21))  # 20 samples
sensor_values = [2721.3, 2725.2, 2717.3, 2713.4, 2749.0, 2725.2, 2721.3, 2713.4, 2725.2, 2723.4,
                 2693.4, 2713.4, 2721.3, 2705.5, 2717.3, 2713.4, 2713.4, 2689.8, 2717.9, 2713.3]  # Sensor readings
force_in_grams = [247, 248, 249, 250, 241, 250, 251, 256, 253, 249, 260, 251, 248, 253, 248, 248, 251, 253, 249, 248]  # Force in grams

# Create a figure and a set of subplots with two y-axes
fig, ax1 = plt.subplots()

# Plot sensor values on the first y-axis
ax1.plot(samples, sensor_values, 'b-', label='Resistance in Ohms')
ax1.set_xlabel('Samples (10 Hz Sampling Rate)')
ax1.set_ylabel('Resistance in Ohms', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Create a second y-axis that shares the same x-axis
ax2 = ax1.twinx()
ax2.plot(samples, force_in_grams, 'r-', label='Force in Grams')
ax2.set_ylabel('Force in Grams', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Add a title
plt.title('Resistance and Corresponding Force Over Samples')

# Show a legend
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Show the plot
plt.show()

