# # list_a = [22,32,11,15,12]
# # #          0, 1, 2, 3, 4
# # # initial index - len --> last index
# # # 0 --> n --> n-1
# #
# # print(list_a)
# #
# # # list_a.
#
# numbers = [1, 10, 2, 3, 10]  # list
#
# numbers.append(4)
# print(numbers)             # Output: [1, 2, 3, 4]
# numbers.extend([5, 6])
# print(numbers)             # Output: [1, 2, 3, 4, 5, 6]
# numbers.insert(4, 10)
# print(numbers)             # Output: [0, 1, 2, 3, 4, 5, 6]
# numbers.remove(10) # a number that you want to remove and not INDEX
# print(numbers)             # Output: [0, 1, 2, 4, 5, 6]
# print(numbers.pop())       # Output: 6
# print(numbers)             # Output: [0, 1, 2, 4, 5]
# numbers.sort()
# print(numbers)             # Output: [0, 1, 2, 4, 5]
# numbers.reverse()
# print(numbers)             # Output: [5, 4, 2, 1, 0]
#
# print(numbers.index(10))    # Output: 1 --> searches for the match of the input given and returns the index of the match
# print(numbers.count(10))    # Output: 1
#
# print(numbers[3])
# # [10, 10, 5, 4, 3, 2, 1]
# #   0,  1, 2, 3, 4, 5 ,6  <-- Index
#
# numbers[3]=25
# print(numbers)
#
# numbers.append("Hello")
# print(numbers)
# # numbers.reverse()
# # [3,2,1,9]
# # [9,1,2,3]

# name  | centuries
# virat | 25
# rohit | 15
# Hp | 20

dict_a= {"virat":25, "rohit":1, "hp":2}
list_b = [
    {"name":"Virat", "centuries_scored": 25},
    {"name": "Rohit", "centuries_scored": 10},
    {"name": "HP", "centuries_scored": 11},
]

print(list_b)


