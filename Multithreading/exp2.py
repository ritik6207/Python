# Thread Scheduling
'''
Python provides basic thread scheduling capabilities through the 'threading.Timer' class and the 'sched' module.

sched module for scheduling tasks and the threading.Timer class for delayed execution of functions.
'''
import sched
import threading
import time
from datetime import datetime


# Scheduling Threads using the Timer Class

def scheduled_event(name, start):
    now = time.time()
    elapsed = int(start - now)
    print(f"{name} is scheduled to run in {elapsed} seconds.")

# Start Time
start = time.time()
print("START: ", time.ctime(start))

t1 = threading.Timer(3, scheduled_event, args=("EVENT_1", start))
t2 = threading.Timer(2, scheduled_event, args=("EVENT_2", start))

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print("END: ", time.ctime(end))


print("\n\n")
# Scheduling Threads using the sched Module
'''
The scheduler() class is defined in the sched module is used to create a scheduler object.
Syntax: scheduler(timefunc=time.monotonic, delayfunc=time.sleep)

# methods defined in scheduler class 
scheduler.enter(delay, priority, action, argument=(), kwargs={}) − Events can be scheduled to run after a delay, or at a specific time. To schedule them with a delay, enter() method is used.
scheduler.cancel(event) − Remove the event from the queue. If the event is not an event currently in the queue, this method will raise a ValueError.
scheduler.run(blocking=True) − Run all scheduled events.
'''

scheduler = sched.scheduler(time.time, time.sleep)

def schedule_event(name, start):
    now = time.time()
    elapsed = int(start - now)
    print(f"{name} is scheduled to run in {elapsed} seconds.")
start = time.time()
print("START: ", time.ctime(start))
scheduler.enter(2, 1, schedule_event, ("EVENT_1", start))
scheduler.enter(5, 3, schedule_event, ("EVENT_2", start))

scheduler.run()

end = time.time()
print("END: ", time.ctime(end))

print("\n\n")


def addition(a,b):
   print("Performing Addition : ", datetime.now())
   print("Time : ", time.monotonic())
   print("Result {}+{} =".format(a, b), a+b)

s = sched.scheduler()

print("Start Time : ", datetime.now())

event1 = s.enter(4, 1, addition, argument = (5,6))
print("Event Created : ", event1)
s.run()
print("End Time : ", datetime.now())