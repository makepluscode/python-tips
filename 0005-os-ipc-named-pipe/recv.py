import os.path

FIFO_FILENAME = './fifo-test'

if os.path.exists(FIFO_FILENAME):
    fp_fifo = open(FIFO_FILENAME, "r")
    i = 0
    while True:
        with open(FIFO_FILENAME, 'r') as fifo:
            data = fifo.read()
            line = data.split('\n')
            for str in line:
                i = i+1
                print(str + "%4d" % i)