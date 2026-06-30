#Question no 3:-
class student:
  
    def __init__(self,name,roll_no):
     self.name=name
     self.roll_no=roll_no
     self.marks_list=[]
    
    def add_marks(self,marks):
      try:
       marks=int(marks)
       
       if(marks < 0 or marks > 100):
          raise ValueError("marks should be betweem 1 to 200")
       self.marks_list.append(marks)

      except ValueError as e:
        print("invalid marks:",e)

    def get_average(self):
      try:
       if(len(self.marks_list) == 0):
         raise ValueError("no marks available")
       else:
        self.average=sum(self.marks_list)/len(self.marks_list)
      except ValueError as e:
        print(e)


    def display_info(self):
       print("name=",self.name)
       print("roll_no=",self.roll_no)
       print("marks_list=",self.marks_list)
       print("Average=",self.average)
  
   
name=input("Enter your name:")
roll_no=input("Enter your roll no:")
s1=student(name,roll_no)
for i in range(5):
  mark=int(input("Enter your marks:"))
  s1.add_marks(mark)
s1.get_average()
s1.display_info()   
          
          
       