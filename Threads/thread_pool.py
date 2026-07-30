from concurrent.futures import ThreadPoolExecutor
import time

def work(x):
    print(f"Starting {x}")
    time.sleep(2)
    print(f"Finished {x}")

with ThreadPoolExecutor(max_workers=3) as executor:

    for i in range(10):
        future = executor.submit(work, i) #future.done() .result() .exception()
