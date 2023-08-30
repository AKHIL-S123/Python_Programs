from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,validator,Field
from typing import List

app=FastAPI()

class Student(BaseModel):
    name : str=Field(default='akhil')
    age:int=Field(default=18,gt=0,le=100)
    gender :str=Field(default="male")
    address:str=Field(default="295/indira nagar")
    city:str =Field(default="tirupur")
    pincode:int=Field(default=123456,gt=99999,lt=1000000)
    @validator('name')
    def val_name(cls,value):
        if any(char.isdigit() for char in value):
            raise ValueError("name must be charater")
        return value
    @validator('gender')
    def val_gen(cls,value):
        genders=["male","female","others"]
        if value not in genders:
            raise ValueError("gender value must be male or female or others")
        return value

db=[]
counter_id=0

@app.post('/create')
def create(student:Student):
    global counter_id
    counter_id += 1
    id =  counter_id
    student_info=student.__dict__
    print(student_info)
    student_info["id"]=id
    db.append(student_info)
    return student_info
    

@app.get('/get_all_student/',response_model=list[Student])
def show_all():
    return db

@app.get('/get_by_id/{id}')
def get_by_id(id:int):
    for i in db:
        if i["id"]==id:
            return i
        raise HTTPException(status_code=404,detail="item not found")
    
@app.put('/update/{id}')
def update(id:int,student:Student):
    # if id in db:
    #     x=id - 1
    #     return db[x]
    for i in db:
        if i["id"]==id:
            tem=db[id - 1]
            for k,v in student.__dict__.items():
                if v is not None:
                    tem[k]=v
                return tem
        raise HTTPException(status_code=404,detail="found")

@app.delete('/delate')
def remove(id:int):
    for i in db:
        if i["id"]==id:
            db.remove(i)
            return {"item removed"} 
    raise HTTPException(status_code=404,detail="not found")



