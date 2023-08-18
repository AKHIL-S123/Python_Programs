class Student:
    def __init__(self):
        self.data = {}

    def add(self, id, name, age, grade):
        self.data[id] = {
            'id': id,
            'name': name,
            'age': age,
            'grade': grade
        }
        print(f"Created student Info is")
        x=self.data[id]
        dis=[]
        student_info = [f"{key}: {value}" for key, value in x.items()]
        dis.append(student_info)
        for k in  dis:
            print([", ".join(k)])
        
     
    def show(self, id):
        if id in self.data:
            return self.data[id]
        else:
            return None

    def show_by_name(self, name):
        if name in [student['name'] for student in self.data.values()]:
            return [student for student in self.data.values() if student['name'] == name]
        else:
            return None

    def update(self, id, name=None, age=None, grade=None):
        if id in self.data:
            data = self.data[id]
            if name is not None:
                data["name"] = name
            if age is not None:
                data["age"] = age
            if grade is not None:
                data["grade"] = grade
            print(f"Updated student information for ID {id}: {self.data[id]}")
        else:
            print(f"ID {id} not found")

    def Delete(self, id):
        if id in self.data:
            del self.data[id]
            print(f"Student ID {id} is deleted")
        else:
            print(f"ID {id} not found")

    def show_all(self):
        all_id=[]
        all_name=[]
        all_age=[]
        all_grade=[]
        for student in self.data.values():
          all_id.append("Id :"+str(student['id']))
          all_name.append("Name :"+student['name'])
          all_age.append("Age :"+str(student['age']))
          all_grade.append("Grade :"+str(student['grade']))
        print(all_id)
        print(all_name)
        print(all_age)
        print(all_grade)
        
          


        """all_students_info = []
          for student in self.data.values():
            student_info = [f"{key}: {value}" for key, value in student.items()]
            all_students_info.append(student_info)
        print("All students:")
        for student_info in all_students_info:
            print([", ".join(student_info)])"""




#my_list =[i for i in self.data.values()]
""" for i in self.data.values():
            for j in i:
                print(j)"""
s = Student()

while True:
    print("1. Add a new student")
    print("2. Display student")
    print("3. Update a student")
    print("4. Delete a student")
    print("5. Display student information by name")
    print("6. Exit")
    print("7. Display all student information")

    choice = int(input("Enter your choice:\n"))

    if choice == 1:
        id = int(input("Enter the student ID: "))
        name = input("Enter the student name: ")
        age = int(input("Enter the student age: "))
        grade = input("Enter the grade: ")
        s.add(id, name, age, grade)

    elif choice == 2:
        id = int(input("Enter the student ID: "))
        get_data = s.show(id)
        if get_data is not None:
            print(f"Student information for ID {id}: {get_data}")
        else:
            print(f"Student ID {id} not found")

    elif choice == 3:
        id = int(input("Enter the student ID: "))
        name = input("Enter the student name: ")
        age = int(input("Enter the student age: "))
        grade = input("Enter the grade: ")
        s.update(id, name, age, grade)

    elif choice == 4:
        id = int(input("Enter the student ID: "))
        s.Delete(id)

    elif choice == 5:
        name = input("Enter the student name: ")
        get_data = s.show_by_name(name)
        if get_data is not None:
            print(f"student information for name {name}:")
            dis=[]
            get_d=get_data[0]
            student_info = [f"{key}: {value}" for key, value in get_d.items()]
            dis.append(student_info)
            for k in  dis:
                print([", ".join(k)])

           # dis=[]
            #student_info = [f"{key}: {value}" for key, value in x.items()]
            #dis.append(student_info)
            #for k in  dis:
            #print([", ".join(k)])

        else:
            print(f"No student found with the name {name}")

    elif choice == 6: 
        print("Exiting...")
        break

    elif choice == 7:
        s.show_all()
       
    else:
        print("Invalid option")
