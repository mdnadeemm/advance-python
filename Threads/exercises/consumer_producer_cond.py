import threading
import time

condition = threading.Condition()
queue = []

def producer1():


    for i in range(5):
        with condition:
            queue.append(f"P1-{i}")
            condition.notify()






def producer2():

    for i in range(5):
        with condition:
            queue.append(f"P2-{i}")
            condition.notify()



def consumer1():

    while True:
        with condition:
            while not queue:
                condition.wait()
            item =queue.pop(0)
            print(f"Produced P1-{item}")

def consumer2():
    while True:
        with condition:
            while not queue:
                condition.wait()
            item =queue.pop(0)
            print(f"Produced P2-{item}")


def consumer3():
    while True:
        with condition:
            while not queue:
                condition.wait()
            item =queue.pop(0)
            print(f"Produced P3-{item}")




t1 = threading.Thread(target=producer1)
t2 = threading.Thread(target=producer2)
t3 = threading.Thread(target=consumer1)
t4 = threading.Thread(target=consumer2)
t5 = threading.Thread(target=consumer3)

threads = [t1, t2, t3, t4, t5]

for t in threads:
    t.start()

for t in threads:
    t.join()
