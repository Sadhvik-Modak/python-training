# k	v
# virat, 	23
# rohit,	24
# hp, 	30

# Dictionary
dict_a = {"virat":23, "rohit":24, "hp": 30 }
print(dict_a)

# dict_a

# dict_b = {"abc":11, 12:"bdc"}
# print(dict_b)
#           k1      v1      k2  v2      k3  v3
person = {"name": "Bob", "age": 25, "city": "New York"}  # dict

print(person.keys())           # Output: dict_keys(['name', 'age', 'city'])
print(person.values())         # Output: dict_values(['Bob', 25, 'New York'])
print(person.items())          # Output: dict_items([('name', 'Bob'), ('age', 25), ('city', 'New York')])
print(person.get("gender"))      # Output: Bob
# print(person["name1"])
person.update({"age1": 26})
print(person)                  # Output: {'name': 'Bob', 'age': 26, 'city': 'New York'}
person.pop("age")
print(person)                  # Output: {'name': 'Bob', 'age': 26}
person.setdefault("country", "USA")
print(person)                  # Output: {'name': 'Bob', 'age': 26, 'country': 'USA'}
person.update({"country": "India"})
print(person)



## Data in diff formats in diff databases  -->
# Oracle --> timestamp (MM/DD/YYYY)
# Postgres --> timestamp
#
# Data engineering -->
# avro, parquet -->
# Oracle and Postgres ---> Bigquery,
#
# Data Curation --> SQL
#
# Data Indexing -->
#
# ETL Job --> Extract Transform and Load
#
# Desination --> Datalake / Data warehouse