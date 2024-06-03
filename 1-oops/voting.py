#
# # class
# # age= int(input("Enter age:"))
# #
# # if age>18:
# #     print("Eligibel to Vote")
# # else:
# #     print("Not Eligible to Vote")
#
# # a = 5
# # print(a)
#
# class Printer:
#     var_a = "Hello sir" # Class variable
#     var_b = "inside class"
#     print(f"Inside class, without method: {var_a}")
#
#     def print_text(self):
#         print("Hello")
#
#     def print_class_variable(self):
#         print(f"Inside method value: {self.var_a}")
#
#     def print_variable(self, var_b):
#         print(f"Printing method variable: {var_b}")
#
# class Calculator:
#     def addition(self, a, b):
#         print(f"Sum of {a} and {b} is {a+b}")
#     def subtract(self,a,b):
#         # print(a-b)
#         print(f"Diff of {a} and {b} is {a-b}")
# #
# # c = Calculator()
# # c.addition(a=5,b=12)
# # c.subtract(a=12,b=13)
#
# p1 = Printer()
# p1.print_variable(var_b=5)
#
# p2 = Printer()
# p2.print_variable(var_b=15)
#
# # Constructor
#
# # p.
# # print(f"Printing class variable from object: {p.var_a}")
# # p.print_text()
# # p.print_class_variable()
# # p.print_variable(var_b=12)
#
# # print()
# # print(var_a)

# Construction

# Default Constructor
# class Printer:
#     var_a = 5
#     var_b = 6
#     def __init__(self, var_a, var_b):
#         self.var_a = var_a
#         self.var_b = var_b
#
#     # print(var_b+var_a)
#
#     def addition_class_variables(self):
#         print(self.var_a+ self.var_b)
#
#     def add_method_variables(self, var_a, var_b):
#         print(var_a+var_b)
#
#     # def add_constructor_variables(self):
#     #     print(self)
#
# # print()
#
# d = Printer(var_a=30, var_b=50)
# d.addition_class_variables() # 5+6
# d.add_method_variables(var_a=10,var_b=6) # 10+6


class Voting:
    # validation_age = 15
    def __init__(self, validation_age):
        self.validation_age = validation_age
    def print_validation_age(self):
        print(f"Validation age is {self.validation_age}")

    def validate_age(self, age):
        if age > self.validation_age:
            print("Elgible")
        else:
            print("NA")

indian_voting_criteria = Voting(validation_age=18)
indian_voting_criteria.print_validation_age()
indian_voting_criteria.validate_age(17)

american_voting_criteria = Voting(validation_age=16)
american_voting_criteria.print_validation_age()
american_voting_criteria.validate_age(17)

# v = Voting()
# v.validate_age(age=5)
# v.validate_age(age=25)
