import threading

lock = threading.Lock()

def inner():
    with lock:
        print("Inner")

def outer():
    with lock:
        print("Outer")
        inner()

outer()
