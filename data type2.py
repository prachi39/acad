#tuple

#1
tup=("prachi",3.14,4)
len(tup)
print(len(tup))

#2
tup=("abc","to","zara","a")
a=max(tup)
b=min(tup)
print(a,b)

#3
tup=[2,4,5,6,7]
i=0
mul=1
for i in range(len(tup)):
 mul=mul*tup[i]
print(mul)

#set
#1
a=set([1,2,4,3])
b=set([2,3,5])
print(a.difference(b))
print(b.difference(a))
print(a.intersection(b))

#dictionary
#1
import operator
d={}
count=0
while count<10:
    name=input("enter your name:")
    marks=input("enter your mark out of 100:")
    if name not in d:
        d[name]=marks
        count=count+1
print(d)

#2
sorted_d=sorted(d.items(),key=operator.itemgetter(0))
print('sorted marks are:',sorted_d)

#3
def count(strl):
    dict={}
    for n in strl:
        keys= dict.keys()
        if n in keys:
           dict[n] +=1
        else:
           dict[n]=1
    return dict
print(count('Mississippi'))


