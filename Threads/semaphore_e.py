import threading
import time

sem = threading.Semaphore(3)

def worker(i):
    print(f"Worker {i} waiting")

    with sem:
        print(f"Worker {i} entered")
        time.sleep(3)
        print(f"Worker {i} leaving")

threads = []

for i in range(10):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
