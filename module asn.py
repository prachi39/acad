#1
print("time tuple is the usage of a tuple(list of ordered items/functions) for the ordering and notation of time. "
      "the tuple used for time in python based systems can be largerly summarized by year,month,day,hour,minutes,"
      "seconds,day of the week,day of the year,and finally a DST(daylight savings time")

#2
import datetime,time
print(time.asctime(time.localtime()))
#3
print(time.strftime("%B"))
#4
print(time.strftime("%A"))
#5
d=datetime.date.today()
print(time.strftime("%d/%m/%Y"))
print(d.day)
#6
print(time.localtime())
#7
import math
x=int(input("enter a number"))
print(math.factorial(x))
#8
import math
x=int(input("enter x"))
y=int(input("enter y"))
print(math.gcd(x,y))
#9
import os
print(os.getcwd())

import os
e=os.environ
print(e)

