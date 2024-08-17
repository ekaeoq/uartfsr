import serial
import struct
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

serial_port = '/dev/tty.usbserial-110'
baud_rate = 115200

def get_duration():
    while True:
        try:
            duration = int(input("Enter the duration of data capture in seconds (default 60): ") or "60")
            if duration > 0:
                return duration
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")

def read_sensor():
    data = ser.read(2)
    if len(data) == 2:
        return struct.unpack('>H', data)[0]
    return None

def animate(i):
    value = read_sensor()
    if value is not None:
        x_data.append(time.time() - start_time)
        y_data.append(value)
        
        # Keep only the last 100 points
        x_data_display = x_data[-100:]
        y_data_display = y_data[-100:]
        
        line.set_data(x_data_display, y_data_display)
        ax.relim()
        ax.autoscale_view()
    return line,

# Get user input for duration
duration = get_duration()

ser = serial.Serial(serial_port, baud_rate)

try:
    # Capture data for specified duration
    print(f"Capturing data for {duration} seconds...")
    x_data, y_data = [], []
    start_time = time.time()
    while time.time() - start_time < duration:
        value = read_sensor()
        if value is not None:
            x_data.append(time.time() - start_time)
            y_data.append(value)
    
    # Plot the captured data
    plt.figure(figsize=(10, 6))
    plt.plot(x_data, y_data)
    plt.title(f'FSR Sensor Readings ({duration} seconds)')
    plt.xlabel('Time (s)')
    plt.ylabel('Sensor Value')
    plt.show()

    # Start live plotting
    print("Starting live plotting. Close the window to stop.")
    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)
    ax.set_ylim(0, 4095)  # Set y-axis limits for 12-bit values
    ax.set_xlim(0, 10)  # Start with 10 seconds visible
    ax.set_title('Live FSR Sensor Readings')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Sensor Value')
    
    x_data, y_data = [], []
    start_time = time.time()

    ani = FuncAnimation(fig, animate, frames=200, interval=50, blit=True)
    plt.show()

except KeyboardInterrupt:
    print("Program terminated by user")
finally:
    ser.close()
    print("Serial port closed")
