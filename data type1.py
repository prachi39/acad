#1
n=int(input("enter a list"))
l=[]
l.append(n)
print(l)

#2
list=["google","apple","facebook","microsoft","tesla"]
list.append(l)
print(list)

#3
l=[1,2,5,8,8]
l.count(8)
print(l.count(8))

#4
l=[6,4,7,2,3,1]
l.sort()
print(l)

#5
a=[1,3,6]
b=[2,5]
c=a+b
c.sort()
print(c)

#6
stack=["mango","apple"]
print(stack)
stack.append("orange")
print(stack)
print(stack.pop())
print (stack)

from collections import deque
queue=deque(["mango","apple"])
print(queue)
queue.append("orange")
print(queue)
print(queue.popleft())
print(queue)

