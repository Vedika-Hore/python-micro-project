#Question no 9:-
import numpy as np
array1=np.random.randint(1,50,20)
print(array1)

matrix=array1.reshape(4,5)
print("Reshape=",matrix)
print("sum=",array1.sum())
print("mean=",array1.mean())
print("standard deviation of matrix=",array1.std())
print("maximum value in each row=",np.max(matrix,axis=1))