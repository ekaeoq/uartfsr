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

def animate(i, x_data, y_data, line):
    data = ser.read(2)
    if len(data) == 2:
        value = struct.unpack('>H', data)[0]
        x_data.append(time.time() - start_time)
        y_data.append(value)
        
        x_data = x_data[-100:]  # Keep only the last 100 points
        y_data = y_data[-100:]  # Keep only the last 100 points
        
        line.set_data(x_data, y_data)
        ax.relim()
        ax.autoscale_view()
    return line,

# Get user input for duration
duration = get_duration()

ser = serial.Serial(serial_port, baud_rate)

try:
    # Setup the plot
    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)
    ax.set_ylim(0, 4095)  # Set y-axis limits for 12-bit values
    ax.set_xlim(0, 10)  # Start with 10 seconds visible
    ax.set_title('FSR Sensor Readings')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Sensor Value')
    
    x_data, y_data = [], []
    start_time = time.time()

    # Capture data for specified duration
    print(f"Capturing data for {duration} seconds...")
    while time.time() - start_time < duration:
        data = ser.read(2)
        if len(data) == 2:
            value = struct.unpack('>H', data)[0]
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
    print("Starting live plotting. Press Ctrl+C to stop.")
    x_data, y_data = [], []
    start_time = time.time()
    ani = FuncAnimation(fig, animate, fargs=(x_data, y_data, line), interval=50, blit=True)
    plt.show()

except KeyboardInterrupt:
    print("Program terminated by user")
finally:
    ser.close()
    print("Serial port closed")
