import threading
def worker():
    print(threading.current_thread().name)

t = threading.Thread(target=worker, name="Downloader") #pass worker not worker() this call worker immediately and return value
t.start()
