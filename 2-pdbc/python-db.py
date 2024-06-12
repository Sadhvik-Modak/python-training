import psycopg2

# id_to_be_inserted= 5
# name_to_be_inserted='Vivek'

print("Register User here: ")
id_to_be_inserted= int(input("Enter the User ID: "))
name_to_be_inserted=input("Enter the name: ")

pg_connection = psycopg2.connect(
    database="postgres",
    user="yeedu",
    password="yeedu",
    host="localhost",
    port="5432"
)

cursor = pg_connection.cursor()

# cursor.execute("SELECT version();")
#
# print(cursor.fetchall())
# #
cursor.execute("create table if not exists employee(id int, name text);")
#
# cursor.execute(f"insert into employee values (10,'ABC')")
itr = 0
while itr<4:
    cursor.execute(f"insert into employee values ({id_to_be_inserted},'{itr}{name_to_be_inserted}')")
    pg_connection.commit()
    itr=itr+1

#
# cursor.execute("select * from employee e;")

print("user entry created succesfully!!!")


# record = cursor.fetchall()
# print(record)

cursor.close()
pg_connection.close()
