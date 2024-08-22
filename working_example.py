import serial
import struct
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

serial_port = '/dev/tty.usbserial-130'
#serial_port = '/dev/tty.usbserial-2130'
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

def calculate_weight(sensor_value):
    #return sensor_value-3095/0.172
    return max(0, (sensor_value - 3121.9) / 0.4114)


def animate(i):
    value = read_sensor()
    if value is not None:
        current_time = time.time() - start_time
        x_data.append(current_time)
        y_data.append(value)
        weight = calculate_weight(value)
        weight_data.append(weight)
        
        # Update the lines with all data
        line_sensor.set_data(x_data, y_data)
        line_weight.set_data(x_data, weight_data)
        
        # Adjust x-axis to show last 10 seconds of data
        ax1.set_xlim(max(0, current_time - 10), current_time)
        ax2.set_xlim(max(0, current_time - 10), current_time)
        
        # Adjust y-axis to fit all visible data
        visible_y = [y for x, y in zip(x_data, y_data) if current_time - 10 <= x <= current_time]
        visible_weight = [w for x, w in zip(x_data, weight_data) if current_time - 10 <= x <= current_time]
        if visible_y:
            ax1.set_ylim(3100, max(visible_y) + 10)  # Start from 3100 as that's close to the minimum sensor value
        if visible_weight:
            ax2.set_ylim(0, max(max(visible_weight) + 10, 100))  # Ensure we always show at least 0-100g range
        
        # Print current values to console
        print(f"\rTime: {current_time:.2f}s | Sensor: {value} | Weight: {weight:.2f}g", end="", flush=True)
        
    return line_sensor, line_weight

# Get user input for duration
duration = get_duration()

ser = serial.Serial(serial_port, baud_rate)

try:
    # Start live plotting
    print(f"Capturing and live plotting data for {duration} seconds...")
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    line_sensor, = ax1.plot([], [], lw=2, label='Sensor Value')
    line_weight, = ax2.plot([], [], lw=2, color='r', label='Calculated Weight (g)')
    
    ax1.set_title('Live FSR Sensor Readings')
    ax1.set_ylabel('Sensor Value')
    ax1.legend()
    
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Weight (g)')
    ax2.legend()
    
    # Ensure weight graph always starts from 0
    ax2.set_ylim(0, 100)
    
    x_data, y_data, weight_data = [], [], []
    start_time = time.time()
    ani = FuncAnimation(fig, animate, interval=50, blit=False)
    
    # Live plotting for the duration specified
    plt.show(block=False)
    plt.pause(duration)
    
    # After live plotting, close the live plot window
    plt.close(fig)
    
    # Plot the full data after capturing is done
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    ax1.plot(x_data, y_data, label='Sensor Value')
    ax2.plot(x_data, weight_data, color='r', label='Calculated Weight (g)')
    
    ax1.set_title(f'FSR Sensor Readings ({duration} seconds)')
    ax1.set_ylabel('Sensor Value')
    ax1.set_ylim(3100, max(y_data) + 10)
    ax1.legend()
    
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Weight (g)')
    ax2.set_ylim(0, max(max(weight_data) + 10, 100))  # Ensure we show all data and at least 0-100g range
    ax2.legend()
    
    plt.tight_layout()
    plt.show()

except KeyboardInterrupt:
    print("\nProgram terminated by user")
finally:
    ser.close()
    print("\nSerial port closed")

