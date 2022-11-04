from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
import requests
import operator
import openai
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Postman")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

class Operation(Enum):
    
    addition = "addition"
    subtraction = "subtraction"
    multiplication = "multiplication"

class postin(BaseModel):
    operation_type: Operation|str
    x: int|float
    y: int|float

class postout(BaseModel):
    slackUsername:str = "jerryeagbesi"
    result: int|float|str 
    operation_type: Operation|str
  


@app.post("/",response_model=postout)
def home(payload:postin):
    
    if type(payload.operation_type) == Operation:
        if payload.operation_type.value.lower() == "addition":
            result = payload.x + payload.y 
        elif payload.operation_type.value.lower() == "subtraction":
            result = payload.x - payload.y
        elif payload.operation_type.value.lower() == "multiplication":
            result = payload.x * payload.y
    elif type(payload.operation_type) == str:
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{payload.operation_type}",
        temperature=0.7,
        max_tokens=709,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

        result = response.choices[0].text
        


    return postout(result=result,operation_type=payload.operation_type)
     
            
       
            

