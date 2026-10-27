
# Session 12 - Functions + Lambda
# Defining functions, arguments, return values, map(), filter(), reduce()
# ------------------------------------------------------------------------------------


# Task 1: Calculate Discounted Price

"""
def get_discounted_price(price, discount_percent):
    discount = price * discount_percent / 100
    final_price = price - discount
    return final_price


result = get_discounted_price(500, 10)

print("Final price after discount: ₹", result)
"""

# ------------------------------------------------------------------------------------


# Task 2: Format Instagram Follower Count

"""
def format_follower_count(number):
    if number >= 1000000:
        return f"{number / 1000000:.1f}M"
    elif number >= 1000:
        return f"{number / 1000:.1f}K"
    else:
        return str(number)


print(format_follower_count(1500))
print(format_follower_count(1200000))
print(format_follower_count(850))
"""

# ------------------------------------------------------------------------------------


# Task 3: Convert Song Durations to Seconds Using map()

"""
song_durations = [3, 4, 5, 2, 6]

durations_in_seconds = list(
    map(lambda minutes: minutes * 60, song_durations)
)

print("Song durations in seconds:", durations_in_seconds)
"""

# ------------------------------------------------------------------------------------


# Task 4: Filter Product Names Starting with M

"""
products = ['Mobile', 'Mouse', 'Laptop', 'Monitor', 'Keyboard']

filtered_products = list(
    filter(lambda product: product.startswith('M'), products)
)

print("Products starting with M:", filtered_products)
"""

# ------------------------------------------------------------------------------------


# Task 5: Calculate Total Swiggy Bill Using reduce()

"""
from functools import reduce

item_prices = [120, 80, 150, 60]

total_bill = reduce(lambda total, price: total + price, item_prices)

print("Total Swiggy bill: ₹", total_bill)
"""

# ------------------------------------------------------------------------------------
