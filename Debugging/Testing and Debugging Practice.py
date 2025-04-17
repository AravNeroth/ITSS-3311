# 1:
print("Hello World")


# 2:
def add(a, b):
    return a + b


# 3:
my_list = [1, 2, 3]
try:
    print(my_list[3])
except IndexError:
    print("Index out of range")


# 4:
num = 5
result = num + int("10")
print("4 →", result)


# 5:
variable = "some value"
print("5 →", variable)


# 6:
my_string = "hello"
my_string += "!"
print("6 →", my_string)


# 7:
def greet():
    print("Hello!")
greet()


# 8:
try:
    num2 = int("abc")
except ValueError:
    print("8 → Cannot convert to int")
    num2 = 0


# 9:
divisor = 0
if divisor != 0:
    print("9 →", 10 / divisor)
else:
    print("9 → Cannot divide by zero")


# 10:
try:
    with open('non_existent_file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("10 → File not found.")
    content = ""


# 11:
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Done!")
countdown(5)


# 12:
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area
print("12 →", calculate_area(5))


# 13:
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print("13 →", find_max([3, 1, 4, 2]))


# 14:
def concatenate_strings(str1, str2):
    return str1 + str(str2)
print("14 →", concatenate_strings("Hello", 123))


# 15:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print("15 →", factorial(5))
