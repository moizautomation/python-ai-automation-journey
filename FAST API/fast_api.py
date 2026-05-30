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

class User(BaseModel):
    name: str
    skill: str
    goal: str

@app.get("/home")
def home():
    return {"message" : "Welcome"}

@app.post("/info")
def info(user : User):
    return {
        "message" : f"{user.name} is skilled in {user.skill} and goal is to become a {user.goal}"
    }

class Calculate(BaseModel):
    a : int
    b : int
@app.post("/calculate")
def calculate(data : Calculate):
    add = data.a + data.b
    diff = abs(data.a - data.b)
    mult = data.a * data.b

    return {
        "sum" : add,
        "difference" : diff,
        "multiplication" : mult
    }