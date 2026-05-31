from fastapi import FastAPI
from pydantic import BaseModel
    
# TASK 1 (BASIC SYNTAX)
#app = my server
app = FastAPI()

#If someone visits "/"
#run the function below
# @app.get("/")
#Function executed when user visits localHost
# def home():
#     return {"status": "ok"}

# @app.get("/profile")
# def profile():
#     return {"name" : "Abdul Moiz, an AI automation developer. Favourtie Programming Language is Python."}

# @app.get("/goal")
# def goal():
#     return {"Goal" : "I want to become an AI automation python Expert and land 3 Paid Project."}

# TASK 2 (POST REQUEST PRACTICE)
# POST request mean sending data to API
# class User(BaseModel):
#     name: str
#     age: int
#     skill: str


# @app.post("/add-user")
#this will automatically create a user object like: user = User("Ali",22,"Python")
# def adduser(user: User):
#     return {
#         "message": f"{user.name} is {user.age} years old and is skilled in {user.skill}"
#     }

# TASK 3 (MULTI-ENDPOINT)
# class User(BaseModel):
#     name: str
#     skill: str
#     goal: str

# @app.get("/home")
# def home():
#     return {"message" : "Welcome"}

# @app.post("/info")
# def info(user : User):
#     return {
#         "message" : f"{user.name} is skilled in {user.skill} and goal is to become a {user.goal}"
#     }

# class Calculate(BaseModel):
#     a : int
#     b : int
# @app.post("/calculate")
# def calculate(data : Calculate):
#     add = data.a + data.b
#     diff = abs(data.a - data.b)
#     mult = data.a * data.b

#     return {
#         "sum" : add,
#         "difference" : diff,
#         "multiplication" : mult
#     }

# DAY 2 TASK 1 (QUERY PARAMETERS)
# Query parameter is instead of getting input through the user you get it through the URL.

# ENDPOINT 1
# @app.get("/product-search")
# def productsearch(name : str,catogery : str):
#     return {
#         "product_name" : name,
#         "catogery" : catogery
#     }

# ENDPOINT 2
# @app.get("/student-search")
# def studentsearch(st_name : str,st_course : str):
#     return{
#         "student_name" : st_name,
#         "course" : st_course
#     }


# TASK 2 (VALIDATION & ERROR HANDLING)

# @app.get("/course-registration")
# def registration(name : str, age : int,course : str):
#     if(name == ""  or course == ""):
#         return {
#             "message" : "Parameters cannot be empty"
#         }
#     if(age <= 0):
#         return {
#             "message" : "Age is invalid"
#         } 
#     return {
#         "student-name" : name,
#         "student_age" : age,
#         "course_name" : course
#     }

# TASK 3 (MULTI-ENPOINTS WORKING TOGETHER)
# Home enpoint reutrning a simple message
# @app.get("/home")
# def home():
#     return {
#         "message" : "API is running"
#     }

# User profile endpoint with query parameters and dynamic URL
# @app.get("/user-profile")
# def userprofile(name : str):
#     if(name == ""):
#         return {
#             "message" : "Name cannot be empty"
#         }
#     return {
#         "message" : f"Hi {name}, Welcome to your Profile!"
#     }

# @app.get("/analyze")
# def analyze(name : str,age : int,skill : str):
#     if(name == None or skill == None):
#         return{
#             "message" : "Parameters cannot be empty",
#             "status" : "inactive"
#         }
#     if(age <= 0):
#         return {
#             "message" : "Age is Invalid",
#             "status" : "inactive"
#         }
#     return {
#         "message" : f"{name} age is {age} and is skilled in {skill}",
#         "status" : "active"
#     }


# TASK 4 (Mini API SYSTEM DASHBOARD)

#Home enpoint reutrning a simple message
@app.get("/home")
def home():
    return {
        "message" : "API is running"
    }

# User profile endpoint with query parameters and dynamic URL
@app.get("/user-profile")
def userprofile(name : str):
    if(name == None or name == ""):
        return {
            "message" : "Name cannot be empty"
        }
    return {
        "message" : f"Hi {name}, Welcome to your Profile!"
    }

@app.get("/student-analyzer")
def studentanalyzer(name : str, age : int,course : str):
    if(name == None or name == ""  or course == None or course == ""):
        return {
            "status" : "Inactive"
        }
    if(age <= 0):
        return {
            "status" : "Inactive"
        } 
    return {
        "student-name" : name,
        "student_age" : age,
        "course_name" : course,
        "status" : "Active"
    } 

@app.get("/product-search")
def productsearch(name : str,price : float,rating : float):
    if(price >= 1000 and rating >= 4.5):
        return {
            "message" : "Premium Product",
        }
    elif(price > 300 and price < 999 and rating > 3.5 and rating < 4.4):
        return {
            "message" : "Standard Product",
        }
    elif(price < 300 and rating < 3.3):
        return {
            "message" : "Budget Product",
        }
    else:
        return {
            "message" : "No result"
        }