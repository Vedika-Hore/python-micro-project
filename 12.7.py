#Question no 7:-
class Employee:
 def __init__(self,emp_id,name,detail):
   self.emp_id=emp_id
   self.name=name
   self.detail=detail
   

 def show_details(self):
  print("Emp Id=",self.emp_id)
  print("Name=",self.name)
  print("Department=",self.detail[0])
  print("Salary=",self.detail[1])
  
employee={}
e1=Employee(101,"Anisha",("IT",50000))
e2=Employee(102,"Akshara",("HR",80000))
e3=Employee(103,"Vedika",("CS",60000))

employee[e1.emp_id]=e1
employee[e2.emp_id]=e2
employee[e3.emp_id]=e3

for key,emp in employee.items():
  emp.show_details()