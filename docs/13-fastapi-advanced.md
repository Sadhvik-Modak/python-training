### KT Session: Sample API Using FastAPI - Part 2

#### Setting up the FastAPI Project

1. **Install FastAPI and Uvicorn**:
   ```sh
   pip install fastapi uvicorn
   ```

2. **Project Structure**:
   - Create a directory for your project:
     ```
     my_fastapi_project/
         ├── main.py
         ├── employees.json
     ```

3. **Initialize JSON File**:
   Create an empty `employees.json` file with an empty list.
   ```json
   []
   ```

### FastAPI Project

**main.py**:
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from typing import List

app = FastAPI()

# Define the Employee model
class Employee(BaseModel):
    emp_id: int
    name: str
    salary: float
    address: str

# Helper function to read data from the JSON file
def read_employees():
    try:
        with open("employees.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Helper function to write data to the JSON file
def write_employees(employees):
    with open("employees.json", "w") as file:
        json.dump(employees, file, indent=4)

# API to register a new employee
@app.post("/employees/", response_model=Employee)
def register_employee(employee: Employee):
    employees = read_employees()
    
    # Check if employee ID already exists
    for emp in employees:
        if emp["emp_id"] == employee.emp_id:
            raise HTTPException(status_code=400, detail="Employee ID already exists")
    
    employees.append(employee.dict())
    write_employees(employees)
    return employee

# API to get an employee by ID
@app.get("/employees/{emp_id}", response_model=Employee)
def get_employee(emp_id: int):
    employees = read_employees()
    for emp in employees:
        if emp["emp_id"] == emp_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

# API to delete an employee by ID
@app.delete("/employees/{emp_id}", response_model=dict)
def delete_employee(emp_id: int):
    employees = read_employees()
    for emp in employees:
        if emp["emp_id"] == emp_id:
            employees.remove(emp)
            write_employees(employees)
            return {"message": "Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")

# API to get all employees
@app.get("/employees/", response_model=List[Employee])
def get_all_employees():
    return read_employees()
```

**Explanation**:

1. **Creating an Instance of FastAPI**:
   ```python
   app = FastAPI()
   ```

2. **Defining the Employee Model**:
   ```python
   class Employee(BaseModel):
       emp_id: int
       name: str
       salary: float
       address: str
   ```

3. **Helper Functions to Read and Write JSON**:
   ```python
   def read_employees():
       try:
           with open("employees.json", "r") as file:
               return json.load(file)
       except FileNotFoundError:
           return []

   def write_employees(employees):
       with open("employees.json", "w") as file:
           json.dump(employees, file, indent=4)
   ```

4. **Register Employee**:
   ```python
   @app.post("/employees/", response_model=Employee)
   def register_employee(employee: Employee):
       employees = read_employees()
       
       for emp in employees:
           if emp["emp_id"] == employee.emp_id:
               raise HTTPException(status_code=400, detail="Employee ID already exists")
       
       employees.append(employee.dict())
       write_employees(employees)
       return employee
   ```

5. **Get Employee by ID**:
   ```python
   @app.get("/employees/{emp_id}", response_model=Employee)
   def get_employee(emp_id: int):
       employees = read_employees()
       for emp in employees:
           if emp["emp_id"] == emp_id:
               return emp
       raise HTTPException(status_code=404, detail="Employee not found")
   ```

6. **Delete Employee by ID**:
   ```python
   @app.delete("/employees/{emp_id}", response_model=dict)
   def delete_employee(emp_id: int):
       employees = read_employees()
       for emp in employees:
           if emp["emp_id"] == emp_id:
               employees.remove(emp)
               write_employees(employees)
               return {"message": "Employee deleted successfully"}
       raise HTTPException(status_code=404, detail="Employee not found")
   ```

7. **Get All Employees**:
   ```python
   @app.get("/employees/", response_model=List[Employee])
   def get_all_employees():
       return read_employees()
   ```

### Running the FastAPI App

Run the FastAPI application using Uvicorn:
```sh
uvicorn main:app --reload
```

### Summary

- **Register Employee**: POST request to `/employees/` to add a new employee.
- **Get Employee by ID**: GET request to `/employees/{emp_id}` to retrieve an employee by ID.
- **Delete Employee by ID**: DELETE request to `/employees/{emp_id}` to delete an employee by ID.
- **Get All Employees**: GET request to `/employees/` to retrieve all employees.
