from fastapi import FastAPI
import json

# Create an instance of the FastAPI class
app = FastAPI()

# Load user data from JSON file
with open('users.json') as f:
    users = json.load(f)

# json.loads() --> Converts list of dict to JSON string
# json.load() --> Converts JSON string to list of dict

# Define a basic route
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Define a route to get user details
# Path Parameter
# @app.get("/user/{user_id}")
# def read_item(user_id: int):
#     return {"user_id": user_id}

# Path Parameter
# /user/3
@app.get("/user/{user_id}")
def read_item(user_id: int):
    for user in users:
        if user['user_id'] == user_id:
            return user
    return {"error":"User Not found"}

# Query Parameter
# /user?user_id=3
# /user?user_mame=bob
# http://localhost:8000/user?user_id=2&name=Bob
@app.get("/user")
def get_user(user_id: int, name: str):
    # Find the user by user_id
    for user in users:
        if user['user_id'] == user_id:
            if user['name'] == name:
                return user
    # raise HTTPException(status_code=404, detail="User not found")
    return {"error":"User Not found"}

