# Thread Pool
'''
There are two-way to implementation for thread
1. ThreadPool
2. ThreadPoolExecuter
'''
import time
from multiprocessing.pool import ThreadPool


# Python ThreadPool Class
def square(number):
    sqr = number * number
    time.sleep(1)
    print("Number: {} Sqr:{}".format(number, sqr))

def cube(number):
    cub = number * number * number
    time.sleep(1)
    print("Number: {} Cube:{}".format(number, cub))
number = [1, 2, 3, 4, 5]
pool = ThreadPool(3)
pool.map(square, number)
pool.map(cube, number)
pool.close()

print("\n\n")
# Using Python ThreadPoolExecutor Class
'''
The Future Class
:- concurrent.futures.Future
result(timeout=None): This method returns the value returned by the call. If the call hasn't yet completed, then this method will wait up to timeout seconds. If the call hasn't completed in timeout seconds, then a TimeoutError will be raised. If timeout is not specified, there is no limit to the wait time.
cancel(): This method, attempt to cancel the call. If the call is currently being executed or finished running and cannot be cancelled then the method will return a boolean value False. Otherwise the call will be cancelled and the method returns True.
cancelled(): Returns True if the call was successfully cancelled.
running(): Returns True if the call is currently being executed and cannot be cancelled.
done(): Returns True if the call was successfully cancelled or finished running.
'''
'''
The ThreadPoolExecutor Class
Syntax:- concurrent.futures.ThreadPoolExecutor(max_threads)
'''
from concurrent.futures import ThreadPoolExecutor
from time import sleep
def square(numbers):
   for val in numbers:
      ret = val*val
      sleep(1)
      print("Number:{} Square:{}".format(val, ret))
def cube(numbers):
   for val in numbers:
      ret = val*val*val
      sleep(1)
      print("Number:{} Cube:{}".format(val, ret))

numbers = [1,2,3,4,5]
executor = ThreadPoolExecutor(4)
thread1 = executor.submit(square, (numbers))
thread2 = executor.submit(cube, (numbers))
print("Thread 1 executed ? :",thread1.done())
print("Thread 2 executed ? :",thread2.done())
sleep(2)
print("Thread 1 executed ? :",thread1.done())
print("Thread 2 executed ? :",thread2.done())