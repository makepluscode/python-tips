import os
import csv
import time, datetime
import threading

from queue import Queue
from threading import Lock

class RingBuffer:
    _instance = None

    @classmethod
    def _getInstance(cls):
        return cls._instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls._instance = cls(*args, **kargs)
        cls.instance = cls._getInstance
        return cls._instance

    def __init__(self):
        self._buffer = []
        self._lock = Lock()

    def get_instance(self):
        return self.instance

    def add_byte(self, byte):
        with self._lock:
            self._buffer.append(byte)

    def get_byte(self):
        byte = 0
        with self._lock:
            if len(self._buffer) > 0:
                byte = self._buffer.pop(0)
            else:
                byte = -1
        return byte

    def get_byte_8(self):
        byte_8 = []
        with self._lock:
            if len(self._buffer) >= 8:
                for i in range(8):
                    byte_8.append(self._buffer.pop(0))
        return byte_8

    def get_len(self):
        length = 0
        with self._lock:
            length = len(self._buffer)
        return length

    def clear(self):
        with self._lock:
            self._buffer.clear()

RingBuffer.instance().add_byte(0x1)
RingBuffer.instance().add_byte(0x2)
RingBuffer.instance().add_byte(0x3)
RingBuffer.instance().add_byte(0x4)
RingBuffer.instance().add_byte(0x5)
RingBuffer.instance().add_byte(0x6)
RingBuffer.instance().add_byte(0x7)
RingBuffer.instance().add_byte(0x8)

print(RingBuffer.instance().get_len())
print(RingBuffer.instance().get_byte())
print(RingBuffer.instance().get_len())
print(RingBuffer.instance().get_byte_8())
print(RingBuffer.instance().get_len())
