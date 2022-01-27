from matplotlib import pyplot

filename = 'eric.csv'
x_val = []
y_val = []

with open(filename, 'r') as f:
    while True:
        raw_data = f.readline()
#       Next line obtained from: https://stackoverflow.com/questions/53919299/python-how-to-properly-use-readline-and-readlines
        if not raw_data: break
        data = raw_data.split(',')
        if data[0].strip() == '' or data[1].strip() == '':
            continue
        elif data[0].strip().isalpha() == True or data[1].strip().isalpha() == True:
             continue
        else:
            x_val.append(float(data[0].strip()))
            y_val.append(float(data[1].strip())) 
    pyplot.plot(x_val, y_val)
    pyplot.xlabel('x-axis')
    pyplot.ylabel('y-axis')
    pyplot.show()