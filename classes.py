class Complex():
 def __init__(self,real,imaginary):
  self.r=real
  self.i=imaginary
c=Complex(3,4)
print(c.r)
print(c.i)

class Apollo():
  destination="moon"
  def __init__(self):
    print("ready to launch")
  def flying(self):
    print("spaceship is flying")
  def getdestination(self):
    print("the destination is " + self.destination)
a=Apollo()
a.flying()
a.getdestination()
b=Apollo()
b.destination="mars"
b.getdestination()


