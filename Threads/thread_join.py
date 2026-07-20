import threading
import time

def work():
    print("Working")
    time.sleep(2)
    print("Done")

t = threading.Thread(target=work)
t.start()
t.join()  # join() blocks until that thread finished/
print("Program Finished")
