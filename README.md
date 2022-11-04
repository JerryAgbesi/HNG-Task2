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
    "msg": {
        "date_of_birth": "Tue, 12 Nov 1991 00:00:00 GMT",
        "first_name": "Benedict",
        "gender": null,
        "hospital_code": "RMC04",
        "hospital_name": "Ridge Medical Center",
        "id_doctor": 32,
        "id_message": null,
        "last_name": "Cumberbatch",
        "license_number": null,
        "middle_name": null,
        "person_image": "https://avatars.dicebear.com/api/bottts/$14.png",
        "user_email": "sherlock@gmail.com"
    },
    "status": true
   }
	```   

```json
    {

        "operation_type": "addition",
        "x": 90,
        "y": 12

    }
```
