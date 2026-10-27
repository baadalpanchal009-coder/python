
# Session 2 - List Iteration Patterns
# For loops on lists, range() with lists
# ------------------------------------------------------------------------------------


# Task 1: Print Playlist Songs with Position

"""
playlist = [
    'Kesariya',
    'Apna Bana Le',
    'Tum Hi Ho',
    'Heeriye',
    'Channa Mereya'
]

for index in range(len(playlist)):
    print(index + 1, playlist[index])
"""

# ------------------------------------------------------------------------------------


# Task 2: Print the First Three Food Items Using range()

"""
foods = ['Pizza', 'Burger', 'Dosa', 'Pasta', 'Fries']

for index in range(3):
    print(foods[index])
"""

# ------------------------------------------------------------------------------------


# Task 3: Calculate Total Flipkart Shopping Cart Value

"""
prices = [299, 499, 150, 1200, 350]

total = 0

for price in prices:
    total += price

print("Total cart value: ₹", total)
"""

# ------------------------------------------------------------------------------------


# Task 4: WhatsApp-Style Unread Messages Counter

"""
unread_counts = [2, 0, 15, 120, 5]

for count in unread_counts:
    if count > 99:
        print("99+")
    else:
        print(count)
"""

# ------------------------------------------------------------------------------------
