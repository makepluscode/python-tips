import threading
from threading import Lock

lock = Lock()
 
def sum(low, high):
    total = 0
    with lock:
        print("1")
        print("2")
        print("3")
        print("4")
        print("5")
        print("6")
        print("7")
        print("8")
        print("9")
        print("10")

t = threading.Thread(target=sum, args=(1, 2))
t.start()

with lock:
    print("11")
    print("12")
    print("13")
