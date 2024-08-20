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

