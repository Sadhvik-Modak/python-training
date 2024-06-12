# # Multiple inheritance
# class A:
#     def method_a(self):
#         print("This is class A")
#
#     def print(self):
#         print("This is class A")
#
# class B:
#     def method_b(self):
#         print("This is class B")
#
#     def print(self):
#         print("This is class B")
#
# class C(B,A):
#     def method_c(self):
#         print("This is class C")
#
# obj_c = C()
# obj_c.method_a()
# obj_c.method_b()
# obj_c.method_c()
#
# obj_c.print()

# # multi-level inheritance
#
# class A: ## GF
#     def method_a(self):
#         print("A")
#
# class B(A): # F
#     def method_b(self):
#         print("B")
#
# class C(B): # S
#     def method_c(self):
#         print("C")

# obj_c = C()
# obj_c.method_a()
# obj_c.method_b()
# obj_c.method_c()

# obj_b = B()

# # Hierarrchila inheritance
#
# class A:
#     def method_a(self):
#         print("A")
#
# class B(A):
#     def method_b(self):
#         print("B")
#
# class C(A):
#     def method_c(self):
#         print("C")
#
# obj_c = C()
# obj_c.method_c()
# obj_c.method_a()
#
# obj_b = B()
# obj_b.method_b()
# obj_b.method_a()