import threading
import time

def work():
    print("Working....")
    time.sleep(2)
    print("Finished")

t = threading.Thread(target=work)
t.start()
print("Main Finished")
