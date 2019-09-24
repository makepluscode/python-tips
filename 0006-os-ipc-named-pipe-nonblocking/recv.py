import os.path
import time
import threading

FIFO_FILENAME = './fifo-test'

class Recviever(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        if os.path.exists(FIFO_FILENAME):
            self.fp_fifo = os.open(FIFO_FILENAME, os.O_RDONLY | os.O_NONBLOCK)

    def run(self):
        while True:
            try:
                data = os.read(self.fp_fifo, 128)
                print(data)
            except OSError as err:
                #print(err.errno)
                pass

recv = Recviever()
recv.start()
