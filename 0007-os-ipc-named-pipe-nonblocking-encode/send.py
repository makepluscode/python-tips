# !/usr/bin/python

import os.path
import time
import threading

FIFO_FILENAME = './fifo-test'

class Sender(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        if not os.path.exists(FIFO_FILENAME):
            os.mkfifo(FIFO_FILENAME)

    def run(self):
        self.fp_fifo = os.open(FIFO_FILENAME, os.O_WRONLY)
        while True:
            if self.fp_fifo:
                print("send to fifo")
                os.write(self.fp_fifo, \
                        str.encode(
                            '$' + ','    # start \
                            '1.23' + ',' # value1 \
                            '4567' + ',' # value2 \
                            'abcd' +     # value3 \
                            '.'          # end \
                        )
                )
            time.sleep(0.1)

sender = Sender()
sender.start()
