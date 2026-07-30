import threading
import time

pizza = False
condition = threading.Condition()
def customer():
    global pizza
    with condition:       # using lock
        while not pizza:
            print("Customer waiting...")
            condition.wait()
        print("Customer got pizza!")



def chef():
    global pizza
    with condition:
        pizza = True
        print("Pizza Ready!")
        condition.notify()


t1 = threading.Thread(target=customer)
t2 = threading.Thread(target=chef)

t1.start()
t2.start()

t1.join()
t2.join()
