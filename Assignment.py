from fastapi import FastAPI
import random
from uuid import UUID

app = FastAPI()

Faheed = {
        'name': 'faheed',
        'age': 12,
        'sex': 'm'
}

students = {}

@app.get('/')
def home():
        return {'message': 'welcome'}

@app.post('/students')
def create_student(name: str, age: int, sex: str, Height: float):
        id_ = len(students) + 1
        new_student = {
                'id': id_,
                'name': name,
                'age': age,
                'sex': sex,
                'Height': Height
        }
        students[id] = new_student
        return {'message': 'students created successfully', 'data': new_student}

@app.get('/students')
def get_students():
        for stu in students:
            students_arr.append(students[stu])
        return {
                'message': 'students fetched successfully',
                'data': 'students_arr'
        }


@app.get('/students/{id}')
def get_one_student(id: int):
    student = students[id]
    return {
        'message': 'student fetched seccessfully',
        'data': 'student'
    }

@app.put('/students/{id}')
def update_student(id: int, name: str):
        student = students[id]
        student['name'] = name
        return {
                'message': 'student updated successfully',
                'data': student
        }

@app.delete('/student/{id}')
def delete_student(id: int):
     student = students[id]
     del students[id]   
     return {
        'message': 'student deleted successfully'
     }