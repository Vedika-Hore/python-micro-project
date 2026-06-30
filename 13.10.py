#Question no 10:-
import numpy as np

num=int(input("Enter How many numbers want to generate:"))
arr=np.random.randint(1,101,size=num)
print(arr)

print("mean=",np.mean(arr))
print("median=",np.median(arr))
print("Standard deviation=",np.std(arr))
print("Minimum=",np.min(arr))
print("maximum=",np.max(arr))

rows=int(np.sqrt(num))
if rows * rows == num:
   matrix=arr.reshape(rows,rows)
   print("2d Array:",matrix)
   print("Row-wise sum",np.sum(matrix,axis=1))
else:
   print("cannot reshape into 2D array")
