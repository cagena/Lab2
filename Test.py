import serial
with serial.Serial('COM21', 115200) as f:
    f.write(b'/x04')