a = 5
b = 6

file = open('read.txt', 'w')
file.write(f"Sum of {a} and {b} is {a+b}")
file.close()


file1 = open("read.txt")
print(file1.read())
file1.close()