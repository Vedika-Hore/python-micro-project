#Question no 5:-
import random
import math
try:
 numbers=set()

 for i in range(10):
     num1=int(input("Enter 10 number:"))
     numbers.add(num1)

 tup=tuple(numbers)
 print(tup)

 if len(tup) >= 3:
     print("Random number=",random.sample(tup,3))
 else:
     print("Not enough numbers")

 print("Square root:",math.sqrt(sum(tup)))

except ValueError:
  print("Error:Please enter valid input")
 

