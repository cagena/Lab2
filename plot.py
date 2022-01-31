# Import modules required to plot.
from matplotlib import pyplot
import serial

# Create empty lists.
x_val = []
y_val = []

# Open the serial port to read from it and plot.
with serial.Serial('COM21', 115200) as f:
    f.write(b'\x04')
    f.write(b'0.1\r\n')
    f.write(b'16384\r\n')
    while True:
        raw_data = f.readline()
#       Next line obtained from: https://stackoverflow.com/questions/53919299/python-how-to-properly-use-readline-and-readlines
        if not raw_data: break
        data = raw_data.split(b',')
        if data[0].strip() == b'' or data[1].strip() == b'':
            continue
        elif data[0].strip().isalpha() == True or data[1].strip().isalpha() == True:
             continue
        else:
            x_val.append(float(data[0].strip()))
            y_val.append(float(data[1].strip()))
    # Plot the values read from the serial port.
    pyplot.plot(x_val, y_val)
    # Label both axes.
    pyplot.xlabel('time [ms]')
    pyplot.ylabel('position [ticks]')
    # Show the plot.
    pyplot.show()