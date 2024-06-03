# while

# a = 5
# # True
# # False
#
# while a >= 0:
#     print(f"Value of a: {a}")
#     a = a-1

list_a = []
sum = 0

while True:
    number_input=int(input("Enter the number you want to add: "))
    list_a.append(number_input)
    sum= sum + number_input
    print(f"The total sum of {list_a} is {sum}")
