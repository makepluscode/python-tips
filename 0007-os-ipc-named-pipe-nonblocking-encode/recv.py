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
                buffer = os.read(self.fp_fifo, 128)
                strbuf = buffer.decode()
                for i in range(len(strbuf)):
                    if strbuf[i]=='$':
                        #print('remain=%d' % len(strbuf[i:]))
                        print('value1=' + strbuf[i+2:i+6])
                        print('value2=' + strbuf[i+7:i+11])
                        print('value3=' + strbuf[i+12:i+16])

            except OSError as err:
                #print(err.errno)
                pass

recv = Recviever()
recv.start()
