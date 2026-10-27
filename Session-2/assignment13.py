
# Session 2 - List Comprehension - Nested List
# ------------------------------------------------------------------------------------


# Task 1: Generate Even Numbers Between 10 and 50

"""
even_numbers = [num for num in range(10, 51) if num % 2 == 0]

print("Even numbers:", even_numbers)
"""

# ------------------------------------------------------------------------------------


# Task 2: Filter Song Durations Greater Than 200 Seconds

"""
playlists = [
    [210, 180, 240],
    [150, 200],
    [300, 120, 90]
]

long_durations = [
    duration
    for playlist in playlists
    for duration in playlist
    if duration > 200
]

print("Durations above 200 seconds:", long_durations)
"""

# ------------------------------------------------------------------------------------


# Task 3: Create Product Tuples with Prices Above 1000

"""
names = ['Shoes', 'Bag', 'Watch', 'Headphones']
prices = [999, 1500, 700, 2200]

products = [
    (name, price)
    for name, price in zip(names, prices)
    if price > 1000
]

print("Products above ₹1000:", products)
"""

# ------------------------------------------------------------------------------------


# Task 4: Flatten Restaurant Ratings Above 4

"""
ratings = [
    [4, 5, 3, 2],
    [5, 4, 4, 3],
    [3, 2, 5, 5]
]

high_ratings = [
    rating
    for restaurant in ratings
    for rating in restaurant
    if rating > 4
]

print("Ratings above 4:", high_ratings)
"""

# ------------------------------------------------------------------------------------
