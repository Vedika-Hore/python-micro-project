#Question no 4:-
def student_database():
    student = {}

    while True:
        print("\n1. Add student")
        print("2. Search student by roll number")
        print("3. Display all students")
        print("4. Exit")

        try:
            choice = input("Enter your choice: ")

            if choice == "1":
                roll_no = int(input("Enter your roll no: "))
                name = input("Enter your name: ")
                marks = input("Enter your marks: ")
                age = input("Enter your age: ")

                student.update({
                    roll_no: {
                        "name": name,
                        "marks": marks,
                        "age": age
                    }
                })

                print("New student details added successfully")

            elif choice == "2":
                roll_no = int(input("Enter roll number: "))

                result = student.get(roll_no)

                if result:
                    print("Student found")
                    print(result)
                else:
                    print("Student not found")

            elif choice == "3":
                if student:
                    for roll, details in student.items():
                        print("Roll no =", roll)
                        print("Name =", details["name"])
                        print("Age =", details["age"])
                        print("Marks =", details["marks"])
                else:
                    print("No student available")

            elif choice == "4":
                print("Program ended")
                break

            else:
                print("Invalid choice")

        except ValueError:
            print("Invalid input")


student_database()