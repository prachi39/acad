#1
import numpy as np
n=np.random.random((10,1))
print(n)
print(np.mean(n,dtype=np.float64))

#2
import numpy as np
n=np.random.random((20,1))
print(n)
print(np.var(n))
print(np.std(n))

#3
import numpy as np
a=np.random.random((10,20))
b=np.random.random((20,25))
print(a)
print("\n")
print(b)
print("\n")
matrix_mul=np.matmul(a,b)
print(matrix_mul)

#4
import numpy as np
a=np.random.random(10,1)
print(a)

def func(x):
    return(1/(1+np.exp((-x))))
result=np.apply_along_axis(func,0,a)
print(result)

