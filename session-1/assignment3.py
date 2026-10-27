
# Task 1: Ask for the user's name and favorite food, then print a welcome message.

"""
name = input("Enter your name: ")
favorite_food = input("Enter your favorite food: ")

print("Hello", name + ", your favorite food is", favorite_food + "!")
"""
# ------------------------------------------------------------------------------------


# Task 2: Take two numbers, convert them to integers, and print arithmetic results.

"""
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)

if num2 != 0:
    print("Quotient:", num1 / num2)
else:
    print("Quotient: Cannot divide by zero")
"""
# ------------------------------------------------------------------------------------


# Task 3: Zomato-style bill calculator using float() and int().

"""
price = float(input("Enter the food item price: ₹"))
quantity = int(input("Enter the quantity: "))

total_bill = price * quantity

print(f"Your total bill is ₹{total_bill:.2f}")
"""
# ------------------------------------------------------------------------------------


# Task 4: Ask for Instagram follower count and use escape characters.

"""
followers = int(input("Enter your Instagram follower count: "))

print("\n\tYou have {:,} followers".format(followers))
"""
# ------------------------------------------------------------------------------------


# Task 5: Basic calculator using two numbers and an operator.

"""
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Error: Invalid operator.")
"""
# ------------------------------------------------------------------------------------