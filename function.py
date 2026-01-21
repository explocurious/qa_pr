#User Greeting Function
# def greet_user():
#     username = input("Enter your username: ")
#     print(f"Hello, {username} Welcome to QA Training!")
# greet_user()


# Function with paramerters
# def test_login(username):
#     print(f"Testing login for user: {username}")

# test_login("test_user")
# test_login("admin")


# function with return value
# def verify_status(code):
#     if code == 200:
#         return "Success"
#     elif code == 404:
#         return "Not Found"
#     else:
#         return "Error"

# status = verify_status(200)
# print(f"Status: {status}")


# multiple parammerters
# def check_credentials(username, password):
#     if username == "admin" and password == "password123":
#         print("Credentials are valid.")
        
#     else:
#         print("Invalid credentials.")

# check_credentials("admin", "password123")    


# 
def can_vote(name,age):
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

can_vote(input("Enter your name: "), int(input("Enter your age: ")))

