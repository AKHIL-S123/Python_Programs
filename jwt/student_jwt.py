import jwt
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
app = FastAPI()

secret_key = "my_secret_key"

# Create a model for students
class Student(BaseModel):
    name: str
    student_id: int
    class_name: str
    school_name: str

# Create a JWT token encoder
def jwt_encode(payload):
    return jwt.encode(payload, secret_key, algorithm="HS256")

# Create a JWT token decoder
def jwt_decode(token):
    return jwt.decode(token, secret_key, algorithms="HS256")

# Define the `create_student` endpoint
@app.post("/students")
def create_student(student: Student):
    """Create a new student."""

    # Encode the student information as a JWT token
    token = jwt_encode({ "name": student.name, "student_id": student.student_id, "class_name": student.class_name, "school_name": student.school_name })

    # Return the JWT token
    return { "token": token }

# Define the `get_student` endpoint
@app.get("/students/{student_id}")
def get_student(student_id: int):
    """Get a student by ID."""

    # Get the student from the database
    student = Student.query.get(student_id)

    # If the student does not exist, raise an exception
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found.")

    # Encode the student information as a JWT token
    token = jwt_encode({ "name": student.name, "student_id": student.student_id, "class_name": student.class_name, "school_name": student.school_name })

    # Return the JWT token
    return { "token": token }

# Define the `delete_student` endpoint
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    """Delete a student by ID."""

    # Delete the student from the database
    student = Student.query.get(student_id)

    # If the student does not exist, raise an exception
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found.")

    # Delete the student
    student.delete()

    # Return a success message
    return { "message": "Student deleted successfully." }
