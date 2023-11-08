import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Thread pool executor will help you to schedule multiple tasks.

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

time1 = time.perf_counter()
# #normal code
func(4)
func(2)
func(1)
time2 = time.perf_counter()
print(time2-time1)

# same code using threads
time3 = time.perf_counter()
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
time4 = time.perf_counter()
print(time4-time3)


def pooling_demo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func, 3)
        future2 = executor.submit(func, 2)
        future3 = executor.submit(func, 4)
        print(future1.result())
        print(future2.result())
        print(future3.result())



pooling_demo()

