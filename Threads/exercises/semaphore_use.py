import threading
import time

allowed_user = threading.Semaphore(3)
inside_lock = threading.Lock()
inside = 0
def worker(x):
    global inside

    print(f"worker {x} waiting")

    with allowed_user:

        with inside_lock:
            print(f"worker {x} enterd | inside = {inside}")
            inside +=1

        time.sleep(2)

        with inside_lock:
            inside -=1
            print(f"Worker {x} leaving | inside= { inside}")



threads = []
for i in range(10):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
