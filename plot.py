# Import modules required to plot.
from matplotlib import pyplot
import serial
import time

# Create a figure to plot to.
pyplot.figure(1)

# Create empty lists.
x_val = []
y_val = []
# list1 = []
# list2 = []

# Open the serial port to read from it and plot.
with serial.Serial('COM21', 115200) as f:
    f.write(b'\x03')
    f.write(b'\x04')
    if f.readline(-1) == b'raw REPL; CTRL-B to exit\r\n':
        f.write(b'\x02')
        f.write(b'\x04')
    time.sleep(0.25)
    f.write(b'0.1\r\n')
    time.sleep(1)
    f.write(b'16384\r\n')
    time.sleep(1.25)
    while True:
        raw_data = f.readline()
#       Next line obtained from: https://stackoverflow.com/questions/53919299/python-how-to-properly-use-readline-and-readlines
#         if not raw_data:
#             break
        data = raw_data.split(b',')
        print(raw_data)
        try:
            float(data[0])
            float(data[1])
        except:
            if len(data) >= 2:
                if data[0].strip() == b' ' or data[1].strip() == b' ':
                    continue
                elif data[0].strip().isalpha() == True or data[1].strip().isalpha() == True:
                    continue
#              elif len(data) <= 2:
#                  break                    
            elif b'MicroPython' in data[0]:
                break
        else:
            x_val.append(float(data[0].strip()))
            y_val.append(float(data[1].strip()))
    print('hi')
    # Plot the values read from the serial port.
    pyplot.plot(x_val, y_val)
    #pyplot.plot(list1,list2)
    # Label both axes.
    pyplot.xlabel('time [ms]')
    pyplot.ylabel('position [ticks]')
    # Show the plot.
    pyplot.show()
