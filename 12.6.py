#Question no 6:-
try:
    square= lambda a:a*a
    numbers=range(1,21)

    squares=[]

    for i in numbers:
        squares.append(square(i))
    print(squares)

    print("Even Squares:")
    for a in squares:
        if a % 2==0:
            print(a)
except Exception as e:
 print(e) 