# signal = "red"

# if signal == "Yellow":
#     print("Stop, signal is Yellow")
# elif signal == "Green":
#     print("Slow down, signal is Green")
# else:
#     print("Go, signal is Red")

#tests = ["Login", "Signup", "Logout"]
#for t in tests:
  #  print(f"Running test: {t}")

#stdudents = ["Alice", "Bob", "Charlie"]

#for student in stdudents:
 #   print(f"Hello, {student} is present today.")

#for i in range (3):
 #   print("Hello World")

# for i in range (1,11):
#     if i % 2 == 0:
#         print(f"{i} is even")
    # else:
    #     print(f"{i} is odd")

# attempts = 0

# while attempts < 3:
#     print("Attempting to login...")
#     attempts += 1

# print ("Done!")

# password = ""
# correct_password = "secret"

# while password != correct_password:
#     password = input("Enter the password: ")

# print("Access granted!")

# answer = ""
# response = "yes"

# while answer != response:
#     answer = input("Do you want to continue? (yes/no): ")
# print("Continuing...")

# Ask user their username and greet them

username = input("Enter your username: ")
print(f"Hello, {username}!")

# Ask user name 2 numbers and perform arithmetic operation
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid operation"

# Ask for name and print it 3 times using a for loop.
for _ in range(3):
    print(f"{username}")
print(f"The result is: {result}")


# Ask for a number, print whether it is even or odd.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Create a dictionary and  loop thorugh them and print them.
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in my_dict.items():
    print(f"{key}: {value}")    


# Create a list name tests and include some tests within that list and loop through the list and print (“Testing for (testname)”)
tests = ["Login", "Signup", "Logout"]
for t in tests:
    print(f"Testing for {t}")


# Ask for age.If age greater than or equals to  18 → print "You can vote". Else → print "You cannot vote"
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")


# Asks the user for their age
# If age < 10 → print "50% discount"
# Else → print "No discount

age = int(input("Enter your age: "))
if age < 10:
    print("50% discount")
else:
    print("No discount")


# Print “Hello” 5 times using while loop
count = 0
while count < 5:
    print("Hello")
    count += 1

# Ask password from the user until they enter right password(use while loop)

password = ""
correct_password = "secret" 
while password != correct_password:
    password = input("Enter the password: ")
print("Access granted!")


# Keep looping until user types “stop”(while loop)
command = ""
while command != "stop":
    command = input("Type 'stop' to end the loop: ")
print("Loop ended.")




