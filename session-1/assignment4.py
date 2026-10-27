# if, else, elif, Nested if
# ------------------------------------------------------------------------------------


# Task 1: Instagram Account Eligibility

"""
age = int(input("Enter your age: "))

if age >= 13:
    print("You are eligible to create an Instagram account.")
else:
    print("You are not eligible to create an Instagram account.")
"""

# ------------------------------------------------------------------------------------


# Task 2: Grade Calculation

"""
marks = int(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")
elif marks >= 90:
    print("Your grade is A")
elif marks >= 75:
    print("Your grade is B")
elif marks >= 60:
    print("Your grade is C")
elif marks >= 40:
    print("Your grade is D")
else:
    print("Your grade is F")
"""

# ------------------------------------------------------------------------------------


# Task 3: Zomato Late-Night Order Eligibility

"""
age = int(input("Enter your age: "))
time = int(input("Enter current time (0-23): "))

if 0 <= time <= 23:
    if age >= 18:
        if time >= 22 or time <= 2:
            print("Order allowed")
        else:
            print("Order not allowed")
    else:
        print("Order not allowed")
else:
    print("Invalid time! Enter an hour between 0 and 23.")
"""

# ------------------------------------------------------------------------------------


# Task 4: Cricket Team Score

"""
score = int(input("Enter your favorite cricket team's score: "))

if score >= 200:
    print("High Score!")
elif score >= 150:
    print("Good Score")
elif score >= 100:
    print("Average")
else:
    print("Needs Improvement")
"""

# ------------------------------------------------------------------------------------