#Question no 2:-
def manage_marks():                           #function declaration
    list1 = []                                 #empty list

    try:                                       #Exception handling bolck
        for i in range(5):
            marks=int(input("Enter 5 subject marks:")) #take input marks from user
            list1.append(marks)

        average=sum(list1)/len(list1)                  #calculate average
        print("Average=",average)
        print("Highest marks=",max(list1))
        print("lowest marks=",min(list1))
        list1.sort(reverse=True)                       #sort list in descending
        print("Marks in descending order=",list1)
    
    except ValueError:                              #Exception handling block
        print("Error:Please enter valid number")
manage_marks()                                       #calling function 



