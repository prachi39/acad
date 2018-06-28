#1
try:
 a=3
 if a<4:
     a=a/(a-3)
except ZeroDivisionError:     #ZeroDivisionError
    print("num is div by 0")
else:
     print(a)

#2
try:
 l=[1,2,3]
 print(l[3])
except IndexError:             #IndexError
    print("index does not exist")

#3
try:
    raise NameError("Hi There")
except NameError:
    print("An Exception")

#4
def AbyB(a,b):
    try:
        c=((a+b)/(a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
AbyB(2.0,3.0)
AbyB(3.0,3.0)

#5

#ImportError
try:
    import prachi
except ImportError:
    print("prachi does not exist")

#IndexError
try:
    a=[1,2,3]
    print(a[3])
except IndexError:
    print("incorrect index")

#ValueError
try:
   int("key")
except ValueError:
    print("key is invalid int value")

#6

class AgeTooSmallError(Exception):
    pass
try:
    a=int(input("enter age"))
    if(a>18):
     raise AgeTooSmallError
except AgeTooSmallError:
    print(" eligible")
while(a<18):
     print("not eligible")
     a=int(input("enter age "))








