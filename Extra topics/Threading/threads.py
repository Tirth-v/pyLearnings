import time
import threading

# Multi tasking in python
"""
    Execution of multiple tasks at the same time.
    Two types :
    1. Process based multitasking :
        Each task is an independent program/process\
        Used in os level.
    2. Thread based multitasking :
        Each task is an independent thread(Separated part of program)
        Used in programmatic level.
"""

# Multi threading :
"""
    What is  thread : A thread is operating system object that
    executes instructions/program.
    A thread is a seperate flow of execution in program
    Thread : Represents task/ sub program.
    There always will be at least a single thread for all the programs
    which we call main thread.
    We can create as many as we want for different tasks.
    Multiple threads will run parallely so all the tasks can run at once
    Suppose for each function it takes 0.01 sec to call 
    and there are 100 functions so if we call one by one 
    it will require 1 sec but if we divide 25 calls into 4 threads
    then it will take 0.25 sec to execute(It might vary).
    Python  interpreter request OS for creating one Thread called as Main Thread.
    Any process have at least one default thread called as mian thread.
    Main Thread is created by PVM(interpreter).
    threads are python objects of threading.Thread() class.
"""
# step 1 : import thread class from thread module.
from threading import Thread
# step 2 : Create a function containing code to be executed parallely.
# class Example:
#     def  display(self):
#         for i in range(5):
#             print("Hello")
#
# e1 = Example()
# # step 3 : Create a new thread.
# t1 = Thread(target=e1.display)
# # step 4 : start a new thread.
# t1.start()
#
# for i in range(4):
#     print("Welcome")

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

