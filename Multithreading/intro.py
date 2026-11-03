'''
# Python's standard library provides two main modules for managing threads: '_thread' and 'threading'.

# _thread is a lower level module that provides basic thread management functionality.
# threading is a higher level module that provides a more object-oriented interface to thread management.

# threading is the preferred module for most use cases as it provides a higher level of abstraction and provides additional features.
'''

# Starting New Thread using _thread module
'''
start_new_thread() function is used to start a new thread.  
    Syntax:-
        thread.start_new_thread(function, args[, kwargs] )
'''

import _thread
import time

def print_name(name, *arg):
    print(name, *arg)
name = "Ritik..."
_thread.start_new_thread(print_name, (name, 1))
_thread.start_new_thread(print_name, (name, 1, 2))
_thread.start_new_thread(print_name, (name, 1, 2, 3))

time.sleep(0.5)

print("\n\n")

# Starting New Thread using threading module
'''
The threading module provides the Thread class, which is used to create and manage threads.

Here are a few steps to start a new thread using the threading module: −

Create a function that you want the thread to execute.
Then create a Thread object using the Thread class by passing the target function and its arguments.
Call the start method on the Thread object to begin execution.
Optionally, call the join method to wait for the thread to complete before proceeding.

Syntax:-
    thread = threading.Thread(target=func, args=(arg1, arg2, ...))
'''

import threading

def print_name(name, *arg):
    print(name, *arg)
name = "Vicky..."

thread1 = threading.Thread(target=print_name, args=(name, 1))
thread2 = threading.Thread(target=print_name, args=(name, 1, 2))

thread1.start()
thread2.start()

# Waiting for threads to complete
thread1.join()
thread2.join()

print("Threads are finished... exiting")

print("\n\n")

# Synchronizing Threads

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        # Get Lock to synchronize thread
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # Free lock to release next thread
        threadLock.release()

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
print ("Exiting Main Thread")

print("\n\n")

# Multithreaded Priority Queue
'''
get() − The get() removes and returns an item from the queue.
put() − The put adds item to a queue.
qsize() − The qsize() returns the number of items that are currently in the queue.
empty() − The empty( ) returns True if queue is empty; otherwise, False.
full() − the full() returns True if queue is full; otherwise, False.
'''
import queue

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      print ("Starting " + self.name)
      process_data(self.name, self.q)
      print ("Exiting " + self.name)

def process_data(threadName, q):
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
         data = q.get()
         queueLock.release()
         print ("%s processing %s" % (threadName, data))
      else:
         queueLock.release()
         time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
   pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")