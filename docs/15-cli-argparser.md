# Employee Management CLI

## Introduction

This is a Command Line Interface (CLI) tool to manage employees using a FastAPI backend. It allows you to perform CRUD operations (Create, Read, Update, Delete) on employee data. The data is stored in a JSON file on the server.

## Features

- Register a new employee
- Get details of an employee by ID
- Delete an employee by ID
- List all employees

## Dependencies

The CLI tool requires the following Python packages:

- `argparse`: For parsing command-line arguments (included in the Python standard library)
- `requests`: For making HTTP requests to the FastAPI backend
- `setuptools`: For packaging the CLI tool
- `argcomplete`: For enabling shell autocompletion (optional, but recommended)

## Installation

1. **Clone the repository**:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the dependencies**:

   ```sh
   pip install requests setuptools argcomplete
   ```

3. **Create a setup script (`setup.py`)**:

   ```python
   from setuptools import setup

   setup(
       name="employee_cli",
       version="0.1",
       py_modules=["employee_cli"],
       install_requires=[
           "requests",
       ],
       entry_points="""
           [console_scripts]
           employee=employee_cli:main
       """,
   )
   ```

4. **Install the CLI tool**:

   Run this command in the directory containing `setup.py`:

   ```sh
   pip install --editable .
   ```

5. **Enable Shell Autocompletion (optional)**:

   To enable autocompletion for the `employee` command:

   ```sh
   pip install argcomplete
   activate-global-python-argcomplete --user
   ```

## FastAPI Backend Setup

Make sure your FastAPI backend is running. You can run it using Uvicorn:

```sh
uvicorn main:app --reload
```

## Usage

### Register a New Employee

```sh
employee register <emp_id> <name> <salary> <address>
```

**Example**:
```sh
employee register 1 "John Doe" 50000 "123 Main St"
```

### Get Employee Details by ID

```sh
employee get <emp_id>
```

**Example**:
```sh
employee get 1
```

### Delete an Employee by ID

```sh
employee delete <emp_id>
```

**Example**:
```sh
employee delete 1
```

### List All Employees

```sh
employee list
```

**Example**:
```sh
employee list
```

## API Endpoints

The CLI interacts with the following API endpoints:

- **Register Employee**: `POST /employees/`
- **Get Employee**: `GET /employees/{emp_id}`
- **Delete Employee**: `DELETE /employees/{emp_id}`
- **List All Employees**: `GET /employees/`

## Example API Usage

1. **Register a New Employee**:
   ```python
   import requests

   response = requests.post("http://127.0.0.1:8000/employees/", json={
       "emp_id": 1,
       "name": "John Doe",
       "salary": 50000,
       "address": "123 Main St"
   })
   print(response.json())
   ```

2. **Get Employee Details**:
   ```python
   import requests

   response = requests.get("http://127.0.0.1:8000/employees/1")
   print(response.json())
   ```

3. **Delete an Employee**:
   ```python
   import requests

   response = requests.delete("http://127.0.0.1:8000/employees/1")
   print(response.json())
   ```

4. **List All Employees**:
   ```python
   import requests

   response = requests.get("http://127.0.0.1:8000/employees/")
   print(response.json())
   ```
