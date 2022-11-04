# HNG-Task2
An POST endpoint that performs arithmetic operations based on strings or enum values entered

# How It Works
Using an API client(eg.Postman,Rapid API client) or the live docs at `https://postman.onrender.com/docs`, make a POST request using the format below.
    
- BODY PARAMETERS:

    `operation_type`: Any of the following enum values ie.[addition,multiplication,subtraction] or a string stating clearly the operation you would want to perform eg."multiply 16 by 12" 

    `x`: An integer

    `y`: An integer

  
    - Sample:
        ```json
        {
        "operation_type": "addition",
        "x": 90,
        "y": 12
           
        }
        ```
          
- RESPONSE:
	```json
    {
    
   }
	```   
