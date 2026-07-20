import threading
import time
import random

def worker(X):

    print(f"{threading.current_thread().name} Task {X} started")
    time.sleep(random.randint(1,5))
    print(f"Taks {X} finished")


t1 = threading.Thread(target=worker, args=(1,))
t2 = threading.Thread(target=worker, args=(2,))
t3 = threading.Thread(target=worker, args=(3,))
t4 = threading.Thread(target=worker, args=(4,))
t5 = threading.Thread(target=worker, args=(5,))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()


print("All tasks completed.")
