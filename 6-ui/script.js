document.addEventListener("DOMContentLoaded", function() {
    const apiUrl = "http://127.0.0.1:8000";

    // Show the respective section
    window.showSection = function(sectionId) {
        document.querySelectorAll('.section').forEach(section => {
            section.style.display = 'none';
        });
        document.getElementById(sectionId).style.display = 'block';
    }

    // Function to show status popup
    function showPopup(message) {
        const popup = document.getElementById("statusPopup");
        document.getElementById("statusMessage").innerText = message;
        popup.style.display = "block";
    }

    // Function to close status popup
    window.closePopup = function() {
        document.getElementById("statusPopup").style.display = "none";
    }

    // Register Employee
    document.getElementById("registerForm").addEventListener("submit", function(e) {
        e.preventDefault();

        // Get form values
        const emp_id = document.getElementById("emp_id").value;
        const name = document.getElementById("name").value;
        const salary = document.getElementById("salary").value;
        const address = document.getElementById("address").value;

        // Send POST request to register employee
        fetch(`${apiUrl}/employees/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ emp_id, name, salary, address })
        })
        .then(response => response.json())
        .then(data => {
            showPopup("Employee registered successfully!");
            document.getElementById("registerResult").innerText = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            showPopup("Error: " + error);
        });
    });

    // Get Employee
    document.getElementById("getEmployeeForm").addEventListener("submit", function(e) {
        e.preventDefault();

        // Get employee ID from form
        const emp_id = document.getElementById("get_emp_id").value;

        // Send GET request to get employee details
        fetch(`${apiUrl}/employees/${emp_id}`)
        .then(response => response.json())
        .then(data => {
            const resultDiv = document.getElementById("getEmployeeResult");
            resultDiv.innerHTML = `
                <div class="employee-details">
                    <p><strong>ID:</strong> ${data.emp_id}</p>
                    <p><strong>Name:</strong> ${data.name}</p>
                    <p><strong>Salary:</strong
                    <p><strong>Salary:</strong> ${data.salary}</p>
                    <p><strong>Address:</strong> ${data.address}</p>
                </div>
            `;
        })
        .catch(error => {
            showPopup("Error: " + error);
        });
    });

    // Delete Employee
    document.getElementById("deleteEmployeeForm").addEventListener("submit", function(e) {
        e.preventDefault();

        // Get employee ID from form
        const emp_id = document.getElementById("delete_emp_id").value;

        // Send DELETE request to delete employee
        fetch(`${apiUrl}/employees/${emp_id}`, {
            method: "DELETE"
        })
        .then(response => response.json())
        .then(data => {
            showPopup("Employee deleted successfully!");
            document.getElementById("deleteEmployeeResult").innerText = data.message;
        })
        .catch(error => {
            showPopup("Error: " + error);
        });
    });

    // Get All Employees
    document.getElementById("getAllEmployeesBtn").addEventListener("click", function() {
        // Send GET request to get all employees
        fetch(`${apiUrl}/employees/`)
        .then(response => response.json())
        .then(data => {
            const resultDiv = document.getElementById("allEmployeesResult");
            resultDiv.innerHTML = "";
            data.forEach(employee => {
                resultDiv.innerHTML += `
                    <div class="employee-details">
                        <p><strong>ID:</strong> ${employee.emp_id}</p>
                        <p><strong>Name:</strong> ${employee.name}</p>
                        <p><strong>Salary:</strong> ${employee.salary}</p>
                        <p><strong>Address:</strong> ${employee.address}</p>
                    </div>
                `;
            });
        })
        .catch(error => {
            showPopup("Error: " + error);
        });
    });
});
