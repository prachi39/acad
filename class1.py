#1
class Animal:
    def animal_attribute(self):
        print('dog')
class Tiger(Animal):
        print('lion')
b=Tiger()
b.animal_attribute()

#2
class A:
    def f(self):
        return self.g()
    def g (self):
        return 'A'
class B(A):
    def g(self):
        return 'B'
a=A()
b=B()
print (a.f(),b.f())
print (a.g(),b.g())
#OUTPUT= A B A B

#3
class Cop:
    def __init__(self,name,age,work,experience,designation):
        self.n = name
        self.a = age
        self.w = work
        self.e = experience
        self.d = designation
    def add(self):
       print("add details of cop")
    def display(self):
        print(self.n)
        print(self.a)
        print(self.w)
        print(self.e)
        print(self.d)
    def update(self,name,age,work,experience,designation):
        self.n = name
        self.a = age
        self.w = work
        self.e = experience
        self.d = designation
        print(self.n)
        print(self.a)
        print(self.w)
        print(self.e)
        print(self.d)

class Mission(Cop):
    def add_mission_details(self):
        print("mission details")
c=Mission('ABC','34','RT','15','IUI')
c.add()
c.display()
c.update('SDS','24','gfg','12','tty')

#4
class Shape():
    def __init__(self,length,breadth):
         self.l=length
         self.b=breadth

class Rectangle(Shape):
    def area(self):
        area=self.l*self.b
        print("area of rectangle:",area)
class Square(Rectangle):
    def area1(self):
        area1=self.l*self.l
        print("area of Square:",area1)
a=Square(3,4)
a.area()
a.area1()

