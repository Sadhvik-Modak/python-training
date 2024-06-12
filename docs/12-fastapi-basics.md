### KT Session: Sample API Using FastAPI - Part 1

#### Introduction to FastAPI

**Definition**:
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

**Key Features**:
- **High Performance**: Built on top of Starlette and Pydantic.
- **Ease of Use**: Intuitive and easy-to-use interface.
- **Automatic Docs**: Generates interactive API documentation with Swagger UI and ReDoc.
- **Data Validation**: Automatic data validation based on Python type hints.
- **Asynchronous Support**: Built-in support for asynchronous programming.

**Benefits**:
- **Fast Development**: Less time writing code due to automatic validation and interactive documentation.
- **Ease of Testing**: Built-in tools to facilitate testing.
- **Interactive Documentation**: Automatically generated Swagger UI and ReDoc documentation.

### Setting up a FastAPI Project

1. **Install FastAPI and Uvicorn**:
   ```sh
   pip install fastapi uvicorn
   ```

2. **Project Structure**:
   - Create a directory for your project:
     ```
     my_fastapi_project/
         ├── main.py
     ```

### Basic Routing and Request Handling

**main.py**:
```python
from fastapi import FastAPI
from pydantic import BaseModel

# Create an instance of the FastAPI class
app = FastAPI()

# Define a basic route
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Define a route with a path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Define a route with a query parameter
@app.get("/users/")
def read_user(user_id: int):
    return {"user_id": user_id}

# Define a Pydantic model for the request body
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# Define a route to handle POST requests
@app.post("/items/")
def create_item(item: Item):
    return {"item": item}
```

**Running the FastAPI App**:
```sh
uvicorn main:app --reload
```

**Explanation**:
- **Creating an Instance of FastAPI**:
  ```python
  app = FastAPI()
  ```
  This line creates an instance of the FastAPI class. This instance will be used to define all routes and handle incoming requests.

- **Defining Routes**:
  - **Basic Route**:
    ```python
    @app.get("/")
    def read_root():
        return {"message": "Hello, World!"}
    ```
    This route is defined using the `@app.get("/")` decorator, which maps HTTP GET requests to the root URL (`/`). The function `read_root` handles the request and returns a JSON response.

  - **Route with Path Parameter**:
    ```python
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: str = None):
        return {"item_id": item_id, "q": q}
    ```
    This route accepts a path parameter (`item_id`) and an optional query parameter (`q`). The path parameter is part of the URL path, while the query parameter is passed as part of the URL query string.

  - **Route with Query Parameter**:
    ```python
    @app.get("/users/")
    def read_user(user_id: int):
        return {"user_id": user_id}
    ```
    This route accepts a query parameter (`user_id`). Query parameters are specified in the URL after a question mark (`?`).

  - **Defining a Pydantic Model for the Request Body**:
    ```python
    from pydantic import BaseModel

    class Item(BaseModel):
        name: str
        description: str = None
        price: float
        tax: float = None
    ```
    This defines a Pydantic model `Item` that will be used for data validation and parsing of the request body.

  - **Handling POST Requests**:
    ```python
    @app.post("/items/")
    def create_item(item: Item):
        return {"item": item}
    ```
    This route is defined using the `@app.post("/items/")` decorator, which maps HTTP POST requests to the URL path `/items/`. The function `create_item` accepts an `Item` object as the request body and returns it as a JSON response.

### Summary

- **Introduction to FastAPI**: Overview of FastAPI and its key features.
- **Setting up a FastAPI Project**: Installing FastAPI and Uvicorn, and setting up the project structure.
- **Basic Routing and Request Handling**: Defining routes with path and query parameters, handling GET and POST requests, and using Pydantic for data validation.
