from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
import requests
import operator

app = FastAPI(title="Postman")

class operation(Enum):
    
    addition = "addition"
    subtraction = "subtraction"
    multiplication = "multiplication"

class postin(BaseModel):
    operation_type: operation
    x: int or float
    y: int or float

class postout(BaseModel):
    slackUsername:str = "jerryeagbesi"
    result: int or float 
    operation_type: operation
  


@app.post("/",response_model=postout)
def home(payload:postin):
    if payload.operation_type.value == "addition":
        result = payload.x + payload.y 
    elif payload.operation_type.value == "subtraction":
        result = payload.x - payload.y
    elif payload.operation_type.value == "multiplication":
        result = payload.x * payload.y          
 

    return postout(result=result,operation_type=payload.operation_type)

