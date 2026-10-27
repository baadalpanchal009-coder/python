
# Session 6 - Loops (while) + Patterns
# while loop, break, Star Patterns
# ------------------------------------------------------------------------------------


# Task 1: Print Numbers from 1 to 10

"""
number = 1

while number <= 10:
    print(number)
    number += 1
"""

# ------------------------------------------------------------------------------------


# Task 2: Zomato-Style Offer Countdown

"""
minutes_left = 5

while minutes_left > 0:
    print("Offer ends in", minutes_left, "minutes")
    minutes_left -= 1

print("Offer expired!")
"""

# ------------------------------------------------------------------------------------


# Task 3: Right-Angled Triangle Star Pattern

"""
row = 1

while row <= 5:
    print("*" * row)
    row += 1
"""

# ------------------------------------------------------------------------------------


# Task 4: Loading Spinner Using while True and break

"""
count = 0

while True:
    print("Loading...")
    count += 1

    if count == 3:
        break

print("Loading complete!")
"""

# ------------------------------------------------------------------------------------


# Task 5: Pyramid Star Pattern (4 Rows)

"""
rows = 4
row = 1

while row <= rows:
    spaces = 1

    while spaces <= rows - row:
        print(" ", end="")
        spaces += 1

    stars = 1

    while stars <= (2 * row - 1):
        print("*", end="")
        stars += 1

    print()
    row += 1
"""

# ------------------------------------------------------------------------------------
