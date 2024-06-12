### KT Session: Python to PostgreSQL Data CRUD - Part 1

#### Introduction to PostgreSQL

**Definition**:
PostgreSQL is a powerful, open-source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads.

**Key Features**:
- **ACID Compliance**: Ensures reliable transactions.
- **Extensibility**: Supports custom functions and data types.
- **Scalability**: Efficiently handles large volumes of data.
- **Community Support**: Active community and extensive documentation.

### Setting up PostgreSQL

1. **Installation**:
   - **Windows/Mac**: Download the installer from [PostgreSQL Downloads](https://www.postgresql.org/download/).
   - **Linux**: Use the package manager for your distribution.
     ```sh
     sudo apt-get update
     sudo apt-get install postgresql postgresql-contrib
     ```

2. **Starting the PostgreSQL Service**:
   - **Windows**: The installer should set up a service that starts automatically.
   - **Linux**:
     ```sh
     sudo service postgresql start
     ```

3. **Accessing the PostgreSQL Command Line Interface (psql)**:
   ```sh
   sudo -u postgres psql
   ```

4. **Creating a Database and User**:
   ```sql
   CREATE DATABASE mydatabase;
   CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
   GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
   ```

### Connecting Python to PostgreSQL using `psycopg2`

**Installing psycopg2**:
```sh
pip install psycopg2
```

**Connecting to PostgreSQL**:
```python
import psycopg2

try:
    connection = psycopg2.connect(
        database="mydatabase",
        user="myuser",
        password="mypassword",
        host="127.0.0.1",
        port="5432"
    )
    cursor = connection.cursor()
    print("PostgreSQL connection is open")

    # Fetch PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # Closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
```

### Summary

- **Introduction to PostgreSQL**: Overview and key features.
- **Setting up PostgreSQL**: Installation and basic setup.
- **Connecting Python to PostgreSQL**: Using `psycopg2` to connect and interact with PostgreSQL.

---

### KT Session: Python to PostgreSQL Data CRUD - Part 2

#### CRUD Operations (Create, Read, Update, Delete)

**Creating a Table**:
```python
import psycopg2

try:
    connection = psycopg2.connect(
        database="mydatabase",
        user="myuser",
        password="mypassword",
        host="127.0.0.1",
        port="5432"
    )
    cursor = connection.cursor()

    create_table_query = '''
    CREATE TABLE employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        salary REAL
    );
    '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully")

except (Exception, psycopg2.Error) as error:
    print("Error while creating table", error)
finally:
    if connection:
        cursor.close()
        connection.close()
```

**Insert Operation**:
```python
import psycopg2

try:
    connection = psycopg2.connect(
        database="mydatabase",
        user="myuser",
        password="mypassword",
        host="127.0.0.1",
        port="5432"
    )
    cursor = connection.cursor()

    insert_query = '''INSERT INTO employees (name, salary) VALUES (%s, %s)'''
    record_to_insert = ('John Doe', 75000)
    cursor.execute(insert_query, record_to_insert)
    connection.commit()
    print("Record inserted successfully")

except (Exception, psycopg2.Error) as error:
    print("Error while inserting data", error)
finally:
    if connection:
        cursor.close()
        connection.close()
```

**Read Operation**:
```python
import psycopg2

try:
    connection = psycopg2.connect(
        database="mydatabase",
        user="myuser",
        password="mypassword",
        host="127.0.0.1",
        port="5432"
    )
    cursor = connection.cursor()

    select_query = "SELECT * FROM employees"
    cursor.execute(select_query)
    records = cursor.fetchall()
    print("Data retrieved successfully")
    for row in records:
        print(f"ID = {row[0]}, Name = {row[1]}, Salary = {row[2]}")

except (Exception, psycopg2.Error) as error:
    print("Error while reading data", error)
finally:
    if connection:
        cursor.close()
        connection.close()
```

**Update Operation**:
```python
import psycopg2

try:
    connection = psycopg2.connect(
        database="mydatabase",
        user="myuser",
        password="mypassword",
        host="127.0.0.1",
        port="5432"
    )
    cursor = connection.cursor()

    update_query = """UPDATE employees SET salary = %s WHERE id = %s"""
    cursor.execute(update_query, (80000, 1))
    connection.commit()
    print("Record updated successfully")

except (Exception, psycopg2.Error) as error:
    print("Error while updating data", error)
finally:
    if connection:
        cursor.close()
        connection.close()
```

**Delete Operation**:
```python
import psycopg2

try:
    connection = psycopg2.connect(
        database="mydatabase",
        user="myuser",
        password="mypassword",
        host="127.0.0.1",
        port="5432"
    )
    cursor = connection.cursor()

    delete_query = "DELETE FROM employees WHERE id = %s"
    cursor.execute(delete_query, (1,))
    connection.commit()
    print("Record deleted successfully")

except (Exception, psycopg2.Error) as error:
    print("Error while deleting data", error)
finally:
    if connection:
        cursor.close()
        connection.close()
```

### Handling Transactions

**Transaction Example**:
```python
import psycopg2

try:
    connection = psycopg2.connect(
        database="mydatabase",
        user="myuser",
        password="mypassword",
        host="127.0.0.1",
        port="5432"
    )
    cursor = connection.cursor()

    # Start a transaction block
    connection.autocommit = False

    cursor.execute("INSERT INTO employees (name, salary) VALUES (%s, %s)", ('Jane Doe', 85000))
    cursor.execute("INSERT INTO employees (name, salary) VALUES (%s, %s)", ('Mark Smith', 90000))
    
    # Commit the transaction
    connection.commit()
    print("Transaction committed successfully")

except (Exception, psycopg2.Error) as error:
    print("Error while performing transaction", error)
    connection.rollback()
    print("Transaction rolled back")
finally:
    if connection:
        cursor.close()
        connection.close()
```

### Parsing Data from SELECT Query to Lists, Dicts and Saving to JSON

**Fetching Data and Converting to List of Dicts**:
```python
import psycopg2
import json

try:
    connection = psycopg2.connect(
        database="mydatabase",
        user="myuser",
        password="mypassword",
        host="127.0.0.1",
        port="5432"
    )
    cursor = connection.cursor()

    select_query = "SELECT * FROM employees"
    cursor.execute(select_query)
    records = cursor.fetchall()

    # Convert to list of dicts
    employees = []
    for row in records:
        employee = {
            "id": row[0],
            "name": row[1],
            "salary": row[2]
        }
        employees.append(employee)

    # Save to JSON file
    with open('employees.json', 'w') as file:
        json.dump(employees, file, indent=4)

    print("Data saved to employees.json")

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data", error)
finally:
    if connection:
        cursor.close()
        connection.close()
```

### Summary

- **CRUD Operations**: Performing Create, Read, Update, and Delete operations using `psycopg2`.
- **Handling Transactions**: Ensuring data integrity with transactions.
- **Data Parsing and Saving**: Parsing data from a SELECT query into lists and dicts, and saving it to a JSON file.

