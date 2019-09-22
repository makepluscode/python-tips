import os.path

FIFO_FILENAME = './fifo-test'

if not os.path.exists(FIFO_FILENAME):
    os.mkfifo(FIFO_FILENAME)

if os.path.exists(FIFO_FILENAME):
    fp_fifo = open(FIFO_FILENAME, "w")
    for i in range(128):
        fp_fifo.write("Hello,MakeCode\n")
    fp_fifo.write("")