# Student Management System

# Initialize an empty dictionary to store student records
student_records = {}

def create_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    student_records[student_id] = {'name': name, 'age': age}
    print("Student record created.")

def read_student(student_id):
    if student_id in student_records:
        student = student_records[student_id]
        print(f"Student ID: {student_id}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
    else:
        print("Student not found.")

def update_student(student_id):
    if student_id in student_records:
        name = input("Enter updated name: ")
        age = input("Enter updated age: ")
        student_records[student_id]['name'] = name
        student_records[student_id]['age'] = age
        print("Student record updated.")
    else:
        print("Student not found.")

def delete_student(student_id):
    if student_id in student_records:
        del student_records[student_id]
        print("Student record deleted.")
    else:
        print("Student not found.")

def main():
    while True:
        print("\nStudent Management System")
        print("1. Create Student")
        print("2. Read Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_student()
        elif choice == '2':
            student_id = input("Enter student ID to read: ")
            read_student(student_id)
        elif choice == '3':
            student_id = input("Enter student ID to update: ")
            update_student(student_id)
        elif choice == '4':
            student_id = input("Enter student ID to delete: ")
            delete_student(student_id)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
