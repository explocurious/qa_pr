# import modules

# modules.greet("Alice")

# modules.add(5, 10)


# import random

# names = ["Alice", "Bob", "Charlie", "Diana"]

# print(random.choice(names))

# print(random.choices(names, k=2))


# import time

# for i in range(5):
#     time.sleep(2)
#     print(i)

# from modules import  add

# add(7, 3)

# import requests

# r = requests.get("https://jsonplaceholder.typicode.com/todos/1")   

# print("Status Code:", r.status_code)
# print(r.json())



# create a password generator using random module.



import random
import string

def generate_password(length):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = uppercase + lowercase + digits + special_characters

    password = ''.join(random.choice(all_characters) for i in range(length))    
    print(password)


generate_password(int(input("Enter the length of the password: ")))


# create a calculator using user defined module.

from modules import add, subtract, multiply, divide


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    print("Result:", add(num1, num2))
elif operation == '-':
    print("Result:", subtract(num1, num2))
elif operation == '*':
    print("Result:", multiply(num1, num2))
elif operation == '/':
    print("Result:", divide(num1, num2))
else:
    print("Invalid operation")




