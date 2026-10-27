
# Session 2 - Anonymous Functions
# Lambda with Multiple Expressions
# ------------------------------------------------------------------------------------


# Task 1: Calculate Squares Using a Lambda Function

"""
square = lambda number: number * number

for number in range(1, 6):
    print(number, "square =", square(number))
"""

# ------------------------------------------------------------------------------------


# Task 2: Add 10% Service Charge Using map() and Lambda

"""
prices = [120, 250, 99, 180, 310]

updated_prices = list(map(lambda price: price * 1.10, prices))

print("Prices after 10% service charge:", updated_prices)
"""

# ------------------------------------------------------------------------------------


# Task 3: Filter Usernames with More Than 1000 Followers

"""
users = [
    ('raj', 800),
    ('simran', 1500),
    ('veer', 1200),
    ('ananya', 950)
]

k_badge_users = list(
    map(
        lambda user: user[0],
        filter(lambda user: user[1] > 1000, users)
    )
)

print("Users eligible for K badge:", k_badge_users)
"""

# ------------------------------------------------------------------------------------


# Task 4: Return Sum and Product as a Tuple

"""
calculate = lambda a, b: (a + b, a * b)

pairs = [(3, 4), (5, 2), (7, 8)]

for a, b in pairs:
    result = calculate(a, b)
    print(f"Pair: ({a}, {b}), Sum and Product: {result}")
"""

# ------------------------------------------------------------------------------------


# Task 5: Check Palindrome Using a Lambda Function

"""
is_palindrome = lambda text: text == text[::-1]

print("madam:", is_palindrome('madam'))
print("python:", is_palindrome('python'))
print("noon:", is_palindrome('noon'))
"""

# ------------------------------------------------------------------------------------
