import threading
import time
counter = 0

def increment():
    global counter

    for _ in range(10000):
        temp = counter
        time.sleep(0)

        temp +=1
        counter = temp


threads = []

for i in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)

for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)
