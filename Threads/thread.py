import 
import time

def work():
    print("Working....")
    time.sleep(2)
    print("Finished")

t = .Thread(target=work)
t.start()
print("Main Finished")
