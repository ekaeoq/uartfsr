import serial
import struct
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

serial_port = '/dev/tty.usbserial-130'
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
        current_time = time.time() - start_time
        x_data.append(current_time)
        y_data.append(value)
        
        # Update the line with all data
        line.set_data(x_data, y_data)
        
        # Adjust x-axis to show last 10 seconds of data
        ax.set_xlim(max(0, current_time - 10), current_time)
        
        # Adjust y-axis to fit all visible data
        visible_y = [y for x, y in zip(x_data, y_data) if current_time - 10 <= x <= current_time]
        if visible_y:
            ax.set_ylim(min(visible_y) - 10, max(visible_y) + 10)
        
    return line,

# Get user input for duration
duration = get_duration()

ser = serial.Serial(serial_port, baud_rate)

try:
    # Start live plotting
    print(f"Capturing and live plotting data for {duration} seconds...")
    
    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)
    ax.set_title('Live FSR Sensor Readings')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Sensor Value')
    
    x_data, y_data = [], []
    start_time = time.time()

    ani = FuncAnimation(fig, animate, interval=50, blit=False)

    # Live plotting for the duration specified
    plt.show(block=False)
    plt.pause(duration)
    
    # After live plotting, close the live plot window
    plt.close(fig)

    # Plot the full data after capturing is done
    plt.figure(figsize=(10, 6))
    plt.plot(x_data, y_data)
    plt.title(f'FSR Sensor Readings ({duration} seconds)')
    plt.xlabel('Time (s)')
    plt.ylabel('Sensor Value')
    plt.show()

except KeyboardInterrupt:
    print("Program terminated by user")
finally:
    ser.close()
    print("Serial port closed")

