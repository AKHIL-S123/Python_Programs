class Student:
    def __init__(self):
        self.data={}

    def add(self,id,name,age,grade):
        self.data[id]= {
            'id':id,
            'name' : name,
            'age'  : age,
            'grade' : grade
        }
        print(f"created student ID is {id}: {self.data[id]}")


    def show(self,id):
        if id in self.data:
            return self.data[id]
        else:
            return None
    def show_by_name(self,name):
        if name in [student['name'] for student in self.data.values()]:
            return [student for student in self.data.values() if student['name'] == name]
        else:
            return None
        
    def update(self,id,name=0,age=0,grade=0):
        if id in self.data:
            data=self.data[id]
            if id is not None:
                self.data["id"]=id
            if name is not None:
                self.data["name"]=name
            if age is not None:
                self.data["age"]=age
            if grade is not None:
                self.data["grade"]=grade
            print(f"updated student information{self.data[id]},")
        else:
            print(f"id {id} not found")

    def Delete(self,id):
        if id in self.data:
            del self.data[id]
            print(f"student id {id} is deleted ")
        else:
            print(f"id{id} not found")
    def show_all(self):
            print("all student")
            for i in self.data.values():
                print(i)
    
  
                
        


    




s=Student()


while True:
    print("1.Add a new student")
    print("2.Display student")
    print("3.Update a new student")
    print("4.Delete new student")
    print("5.Display student information by name")
    print("7.display all the values in dict:")

    choice=int(input("Enter your choice :\n"))

    if choice==1:
        id=int(input("Enter the student id :"))
        name=input("Enter the student name :")
        age=int(input("Enter the student age :"))
        grade=input("Enter the grade:")
        s.add(id,name,age,grade)

    elif choice==2:
        id=int(input("Enter the student Id :"))
        get_data=s.show(id)
        if get_data is not None:
            print(f"Entered student id is {id}:{get_data}")
        else:
            print(f"student {id} not found")

    elif choice==3:
        id=int(input("Enter the student id :"))
        name=input("Enter the student name :")
        age=int(input("Enter the student age :"))
        grade=input("Enter the grade:")
        s.update(id,name,age,grade)

    elif choice==4:
        id=int(input("Enter the id:"))
        s.Delete(id)
        
    elif choice==5:
        name=input("Enter the  student name:")
        get_data=s.show_by_name(name)
        if get_data is not None:
            print(f'Entered student information is {get_data}')
        else:
            print(f'{name} is not found')

    elif choice ==6:
        print("exit")
    elif choice==7:
        s.show_all()
    else:
        print("Invalid option")