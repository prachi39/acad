import threading
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run(self):
        time.sleep(5)
        print("value send",self.h)

thread1=mythread(1)
thread1.start()


#2
import threading
from threading import Thread
import time
class mythread(threading.Thread):

    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        print("no is",self.h)
        time.sleep(1)
for i in range(10):
 thread1=mythread(1)
 thread1.start()


print("Active threads are",threading.activeCount())

#3

List=["google","apple","facebook","microsoft","tesla"]
import threading
from threading import Thread
import time
class mylist(threading.Thread):
    def __init__(self,List):
        threading.Thread.__init__(self)
        self.l=List
    def run(self):
     for i in List:
        print("display List item with a gap of 2 seconds:",i)
        time.sleep(2)
Thread1=mylist(1)
Thread1.start()

#4

import threading
from threading import Thread
import time,math
class factorial(threading.Thread):

 def __init__(self,fact):
  threading.Thread.__init__(self)
  self.f=fact
 def run(self):
     time.sleep(20)
     print(math.factorial(self.f))

thread1=factorial(4)
thread1.start()

