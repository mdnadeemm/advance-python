import threading
import time

def download(name):
    print(f"Downloading {name}")
    time.sleep(2)
    print(f"{name} Done")

t1 = threading.Thread(target=download, args=("File1",)) #commad is important for single element tuple
t2 = threading.Thread(target=download, args=("File2",))
t3 = threading.Thread(target=download, args=("File3",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All Downloads Complete")
