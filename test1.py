import serial
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configuration
port = 'COM3'  # Replace with your port
baudrate = 115200
duration = 60  # Duration in seconds
sampling_interval = 0.1  # In seconds

# Serial Connection
ser = serial.Serial(port, baudrate, timeout=1)

# Data storage
times = np.arange(0, duration, sampling_interval)
Vouts = np.zeros(len(times))
R_FSRs = np.zeros(len(times))

fig, ax = plt.subplots(2, 1, figsize=(10, 6))
ax[0].set_title('Vout over Time')
ax[0].set_xlabel('Time (s)')
ax[0].set_ylabel('Vout (V)')
ax[1].set_title('R_FSR over Time')
ax[1].set_xlabel('Time (s)')
ax[1].set_ylabel('R_FSR (Ohms)')

# Update plot with new data
def update_plot(frame):
    line = ser.readline().decode('utf-8').strip()
    try:
        if line:
            print(line)  # Debugging purpose
            # Extract data
            _, Vout, _, R_FSR = line.split()
            Vout = float(Vout[:-1])
            R_FSR = float(R_FSR)

            # Shift and update arrays
            Vouts[:-1] = Vouts[1:]
            Vouts[-1] = Vout
            R_FSRs[:-1] = R_FSRs[1:]
            R_FSRs[-1] = R_FSR

            # Update plots
            ax[0].cla()
            ax[1].cla()
            ax[0].plot(times, Vouts)
            ax[1].plot(times, R_FSRs)
    except Exception as e:
        print("Error: ", e)

ani = FuncAnimation(fig, update_plot, interval=sampling_interval * 1000)
plt.show()

ser.close()

