Sure! Let's create a simple web portal using plain HTML, CSS, and JavaScript that interacts with the FastAPI backend we created for the Employee API. The portal will have functionality to register an employee, get an employee by ID, delete an employee, and get all employees.

### Project Structure
```
my_web_portal/
    ├── index.html
    ├── style.css
    ├── script.js
```

### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee Portal</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Employee Portal</h1>
        
        <div class="section">
            <h2>Register Employee</h2>
            <form id="registerForm">
                <label for="emp_id">Employee ID:</label>
                <input type="number" id="emp_id" name="emp_id" required>
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <label for="salary">Salary:</label>
                <input type="number" id="salary" name="salary" required>
                <label for="another_column">Another Column:</label>
                <input type="text" id="another_column" name="another_column" required>
                <button type="submit">Register</button>
            </form>
            <div id="registerResult"></div>
        </div>

        <div class="section">
            <h2>Get Employee</h2>
            <form id="getEmployeeForm">
                <label for="get_emp_id">Employee ID:</label>
                <input type="number" id="get_emp_id" name="get_emp_id" required>
                <button type="submit">Get Employee</button>
            </form>
            <div id="getEmployeeResult"></div>
        </div>

        <div class="section">
            <h2>Delete Employee</h2>
            <form id="deleteEmployeeForm">
                <label for="delete_emp_id">Employee ID:</label>
                <input type="number" id="delete_emp_id" name="delete_emp_id" required>
                <button type="submit">Delete Employee</button>
            </form>
            <div id="deleteEmployeeResult"></div>
        </div>

        <div class="section">
            <h2>All Employees</h2>
            <button id="getAllEmployeesBtn">Get All Employees</button>
            <div id="allEmployeesResult"></div>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

### style.css
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

h1 {
    text-align: center;
}

.section {
    margin-bottom: 20px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
input[type="number"] {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    box-sizing: border-box;
}

button {
    padding: 10px 15px;
    background-color: #007BFF;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

#registerResult,
#getEmployeeResult,
#deleteEmployeeResult,
#allEmployeesResult {
    margin-top: 10px;
    padding: 10px;
    background-color: #e9ecef;
}
```

### script.js
```javascript
document.addEventListener("DOMContentLoaded", function() {
    const apiUrl = "http://127.0.0.1:8000";

    // Register Employee
    document.getElementById("registerForm").addEventListener("submit", function(e) {
        e.preventDefault();
        const emp_id = document.getElementById("emp_id").value;
        const name = document.getElementById("name").value;
        const salary = document.getElementById("salary").value;
        const another_column = document.getElementById("another_column").value;

        fetch(`${apiUrl}/employees/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ emp_id, name, salary, another_column })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("registerResult").innerText = "Employee registered: " + JSON.stringify(data);
        })
        .catch(error => {
            document.getElementById("registerResult").innerText = "Error: " + error;
        });
    });

    // Get Employee
    document.getElementById("getEmployeeForm").addEventListener("submit", function(e) {
        e.preventDefault();
        const emp_id = document.getElementById("get_emp_id").value;

        fetch(`${apiUrl}/employees/${emp_id}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("getEmployeeResult").innerText = "Employee: " + JSON.stringify(data);
        })
        .catch(error => {
            document.getElementById("getEmployeeResult").innerText = "Error: " + error;
        });
    });

    // Delete Employee
    document.getElementById("deleteEmployeeForm").addEventListener("submit", function(e) {
        e.preventDefault();
        const emp_id = document.getElementById("delete_emp_id").value;

        fetch(`${apiUrl}/employees/${emp_id}`, {
            method: "DELETE"
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("deleteEmployeeResult").innerText = data.message;
        })
        .catch(error => {
            document.getElementById("deleteEmployeeResult").innerText = "Error: " + error;
        });
    });

    // Get All Employees
    document.getElementById("getAllEmployeesBtn").addEventListener("click", function() {
        fetch(`${apiUrl}/employees/`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("allEmployeesResult").innerText = "All Employees: " + JSON.stringify(data, null, 2);
        })
        .catch(error => {
            document.getElementById("allEmployeesResult").innerText = "Error: " + error;
        });
    });
});
```

### Running the FastAPI App

First, start your FastAPI app using Uvicorn:
```sh
uvicorn main:app --reload
```

### Running the Web Portal

Simply open the `index.html` file in your web browser. The HTML, CSS, and JavaScript will interact with the FastAPI backend to perform the desired operations.

### Summary

- **Register Employee**: Form to register a new employee.
- **Get Employee**: Form to get an employee by ID.
- **Delete Employee**: Form to delete an employee by ID.
- **Get All Employees**: Button to get all employees.

This setup will give your interns a comprehensive understanding of how to create a web portal using plain HTML, CSS, and JavaScript that interacts with a FastAPI backend for performing CRUD operations on employee data.c