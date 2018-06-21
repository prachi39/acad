#1
radius=float(input("enter number"))
def area(rad):
    area=3.14*rad*rad
    return area
ar=area(radius)
print(ar)

#2
n=6
def perfect(n):
 sum=0
 for i in range(1,n):
   if(n%i==0):
     sum=sum+i
 if(sum==n):
  return True
 else:
  return False
print(perfect(n))

for i in range(1,1001):
 if(perfect(i)==True):
  print(i)

#3
def mul(n):
    for i in range(1,11):
     if(i==11):
         return(mul)
     print(n,'x',i,'=',(n*i))
mul(int(input("enter a number")))

#4
def power(a,b):
    if(b==1):
        return(a)
    else:
        return(a*power(a,b-1))
a=(int(input("enter a")))
b=(int(input("enter b")))
print(power(a,b))

#5
n=int(input("enter a number"))
dict={}
def fact(i):
    if(i==1):
     return 1
    else:
     return(i*fact(i - 1))

for i in range (1,n+1):
    dict[i]=fact(i)
print (dict)
