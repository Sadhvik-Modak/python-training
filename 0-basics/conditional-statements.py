# if else
# if elif else
# = assigning and == equating

# a = 11
# a = int(input("Enter the number you to want check: "))
# if a % 2 == 0:
#     print("Even")
# else:
#     print("odd")

# age = 19
# if age > 18:
#     print("Eligible")
# else:
#     print("not eligible")
#

# print("For English press: 1")
# print("For Telugu press: 2")
# print("For Hindi press: 3")
# # print("For python press: 4")
# print("To go back press: 0")
# number_opted = int(input("Enter the number: "))
#
# if number_opted == 1:
#     print("Proceeding with english...")
# elif number_opted == 2:
#     print("Proceeding with Telugu...")
# elif number_opted == 3:
#     print("Proceeding with Hindi...")
# elif number_opted == 0:
#     print("Going back to menu...")
# else:
#     print("Invalid Input given")

dict_lang = {1:"English", 2: "Telugu", 3: "Hindi", 4: "NA"}

size_of_dict=len(dict_lang)
print(f"Size of Dict: {size_of_dict}")

while size_of_dict > 0:
    print(f"For {dict_lang.get(size_of_dict)} press: {size_of_dict}")
    size_of_dict = size_of_dict - 1

print(dict_lang)
input_num= int(input("Enter the number: "))
print(dict_lang.get(input_num))

