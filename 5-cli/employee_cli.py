import argparse
import requests
import json

API_URL = "http://127.0.0.1:8000"

def register_employee(emp_id, name, salary, address):
    response = requests.post(f"{API_URL}/employees/", json={
        "emp_id": emp_id,
        "name": name,
        "salary": salary,
        "address": address
    })
    if response.status_code == 200:
        print("Employee registered:", response.json())
    else:
        print("Error:", response.json())

def get_employee(emp_id):
    response = requests.get(f"{API_URL}/employees/{emp_id}")
    if response.status_code == 200:
        print("Employee:", response.json())
    else:
        print("Error:", response.json())

def delete_employee(emp_id):
    response = requests.delete(f"{API_URL}/employees/{emp_id}")
    if response.status_code == 200:
        print("Message:", response.json()["message"])
    else:
        print("Error:", response.json())

def get_all_employees():
    response = requests.get(f"{API_URL}/employees/")
    if response.status_code == 200:
        print("All Employees:", json.dumps(response.json(), indent=4))
    else:
        print("Error:", response.json())

def main():
    parser = argparse.ArgumentParser(description="Employee Management CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Register employee command
    register_parser = subparsers.add_parser("register", help="Register a new employee")
    register_parser.add_argument("emp_id", type=int, help="Employee ID")
    register_parser.add_argument("name", type=str, help="Name")
    register_parser.add_argument("salary", type=float, help="Salary")
    register_parser.add_argument("address", type=str, help="Address")

    # Get employee command
    get_parser = subparsers.add_parser("get", help="Get an employee by ID")
    get_parser.add_argument("emp_id", type=int, help="Employee ID")

    # Delete employee command
    delete_parser = subparsers.add_parser("delete", help="Delete an employee by ID")
    delete_parser.add_argument("emp_id", type=int, help="Employee ID")

    # Get all employees command
    subparsers.add_parser("list", help="Get all employees")

    args = parser.parse_args()

    if args.command == "register":
        register_employee(args.emp_id, args.name, args.salary, args.address)
    elif args.command == "get":
        get_employee(args.emp_id)
    elif args.command == "delete":
        delete_employee(args.emp_id)
    elif args.command == "list":
        get_all_employees()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
