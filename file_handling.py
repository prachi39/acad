 #1
f=open("test.txt",encoding="utf8")
j=(f.readlines())
j.reverse()
n=int(input("enter a no of line u want"))
for i in range(0,n):
    print(j[i])
f.close()

#2
n="a"
f=open("test.txt",encoding="utf8")
k=f.read()
m=k.split()
print(k.count(n))

#3
with open("test.txt",encoding="utf8")as f:
    lines=f.readlines()
    with open("test2.txt","w")as f1:
      f1.writelines(lines)

#4
with open('test.txt',encoding="utf8") as f:
 with   open('test2.txt') as f1:
    for line1, line2 in zip(f, f1):
      print(line1+line2)


#5

random=ran




