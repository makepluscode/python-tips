import os
import csv
import time, datetime
import threading

from queue import Queue
from threading import Lock
from periphery import SPI

from logger import *

class RingBuffer(object):
    def __init__(self):
        self.ringbuffer = []
        self.lock = Lock()

    # the class should be a singleton
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super( RingBuffer, self).__new__(self)
            return self.instance

    def add_byte(self, byte):
        self.ringbuffer.append(byte)

    def get_byte(self, byte):
        ret = 0
        if self.get_size() > 0:
            self.ringbuffer.pop()
        else:
            ret = -1
        return ret

    def get_size(self):
        return len(self.ringbuffer)

    def clear(self):
        self.ringbuffer.clear()
