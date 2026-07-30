import threading

lock = threading.RLock() #Reentrant Lock

def inner():
    with lock:
        print("Inner")

def outer():
    with lock:            # internally use acquire() and release()
        print("Outer")
        inner()

outer()
