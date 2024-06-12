import psycopg2
import json

pg_connection = psycopg2.connect(
    database="postgres",
    user="yeedu",
    password="yeedu",
    host="localhost",
    port="5432"
)

cursor = pg_connection.cursor()
cursor.execute(f"insert into employee values (1,'Sadhvik')")
pg_connection.commit()
# cursor.execute("create table if not exists employee(id int, name text);")
cursor.execute("SELECT * from employee")
records = cursor.fetchall()

list_of_employees=[]

index_itr = 0
for employee in records:
    # print(f"{index_itr} -- {employee}")
    index_itr = index_itr+1
    employee_dict = {
        "id": employee[0],
        "name": employee[1]
    }

    # file = open(f'employee-{index_itr}.txt', 'w')
    # file.write(f"{employee[0]}:{employee[1]}")
    # file.close()

    list_of_employees.append(employee_dict)
    # print(employee_dict)
print(list_of_employees)
# print(json.dumps(list_of_employees))


# id
# name

file = open('employee.json', 'w')
file.write(json.dumps(list_of_employees))
file.close()

# print(records)

cursor.close()
pg_connection.close()
