from fastapi import FastAPI
from typing import Union
from enum import Enum
from pydantic import BaseModel


app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/hello")
async def my_root():
    return {"message":"hy this is my secound api"}


"""path parameters with type of str"""

@app.get('/item/{item_id}')
async def read_item(item_id):
    return {"item_id":item_id}


"""path parameters with type of int """


@app.get('item_id/{item_id}')
async def read_item_id(item_id:int):
    return {"item_id_is":item_id}


"""query parameters with required field"""
@app.get('/query')
async def query_function(name:str,roll_num:int):
    var_name={"name":name,"roll no":roll_num}
    return(var_name)


"""query parameters with use union 3.8"""
@app.get('/union')
async def query_union(student_name:str,roll_number:Union[int,None]=None):
    details={"name":student_name,"Roll_number":roll_number}
    return {'the details of student':details}




@app.get("/items_1/")
async def read_item(skip: int = 1, limit: int = 10):
    return fake_items_db[skip : skip + limit]



@app.get("/student/{student_id}")
async def read_student(student_id: str, q: str | None = None):
    if q:
        return {"student_id": student_id, "q": q}
    return {"student_id": student_id}




class Gender(str,Enum):
    male="male"
    female='female'
    other='other'

@app.get('/gender/{gender_name}')
async def get_model(gender_name:Gender):
    if gender_name is Gender.male :
        return {'gender_name':gender_name,'message':"YOU GENDER IS MALE"}
    
    if gender_name.value =='female':
        return {'gender_name':gender_name,'message':'YOU GENDER IS FEMALE'}
    
    return {'gender_name':gender_name,'message':"YOU GENDER IS OTHER"}



class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"



@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

class Choice1(str,Enum):
    one='one'
    two='two'
    three='three'


@app.get('/choice/{choice_name}')
async def choice_model(choice_name:Choice1):
    return {"my choice is :":choice_name}


"""Request Body When you need to send data from a client (let's say, a browser) to your API, you send it as a request body """
"""Requeired"""

class Employee(BaseModel):
    employee_name:str
    is_employee:bool
    employee_salary:float

@app.post('/student/')
async def employee_details(Employee_details:Employee):
    return {"Employee details is":Employee_details}



"""request with default None parametter"""


class Item(BaseModel):
    item_name:str
    price:float | None = None
    description:str | None = None


@app.post('/items/')
async def item_details(item_details:Item):
    return {"item propty is:":item_details}


"""use attributes inside of the function"""





