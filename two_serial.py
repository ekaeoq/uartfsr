import serial
import struct

# serial_port = '/dev/ttyUSB0'  
serial_port = '/dev/tty.usbserial-110'
baud_rate = 115200

ser = serial.Serial(serial_port, baud_rate)

try:
    while True:
        data = ser.read(2)
        
        if len(data) == 2:
            value = struct.unpack('>H', data)[0]
            
            print(f"Received value: {value}")
        else:
            print("Incomplete data received")

except KeyboardInterrupt:
    print("Program terminated by user")
finally:
    ser.close()
    print("Serial port closed")
