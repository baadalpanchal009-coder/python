
# Session 2 - Math & Random Modules
# sqrt(), ceil(), floor(), randint(), random(), sample()
# ------------------------------------------------------------------------------------


# Task 1: Calculate Square Roots Using math.sqrt()

"""
import math

numbers = [16, 49, 81]

for number in numbers:
    print("Square root of", number, "=", math.sqrt(number))
"""

# ------------------------------------------------------------------------------------


# Task 2: Round Product Prices Up Using math.ceil()

"""
import math

prices = [199.1, 349.8, 599.3]

rounded_prices = []

for price in prices:
    rounded_prices.append(math.ceil(price))

print("Original prices:", prices)
print("Rounded prices:", rounded_prices)
"""

# ------------------------------------------------------------------------------------


# Task 3: Calculate Discounted Zomato Bill Using math.floor()

"""
import math

bill_amount = 850

discount = bill_amount * 10 / 100
discounted_bill = bill_amount - discount

final_bill = math.floor(discounted_bill)

print("Original bill: ₹", bill_amount)
print("Discount: ₹", discount)
print("Final bill after discount: ₹", final_bill)
"""

# ------------------------------------------------------------------------------------


# Task 4: Simulate a Dice Roll Using random.randint()

"""
import random

dice_result = random.randint(1, 6)

print("Dice rolled:", dice_result)
"""

# ------------------------------------------------------------------------------------


# Task 5: Select Three Random Songs Using random.sample()

"""
import random

songs = [
    'Kesariya',
    'Shape of You',
    'Believer',
    'Heeriye',
    'Tum Hi Ho',
    'Perfect',
    'Apna Bana Le',
    'Levitating'
]

daily_playlist = random.sample(songs, 3)

print("Today's shuffled playlist:")

for song in daily_playlist:
    print(song)
"""

# ------------------------------------------------------------------------------------
