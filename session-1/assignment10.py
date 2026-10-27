
# Session 10 - Tuples
# Tuple creation, indexing, immutability, slicing, concatenation
# ------------------------------------------------------------------------------------


# Task 1: Create and Print a Tuple

"""
fav_apps = ('Instagram', 'Zomato', 'Spotify', 'WhatsApp', 'Flipkart')

print("My favorite apps:", fav_apps)
"""

# ------------------------------------------------------------------------------------


# Task 2: Access the 2nd and 4th Apps Using Indexing

"""
fav_apps = ('Instagram', 'Zomato', 'Spotify', 'WhatsApp', 'Flipkart')

print("2nd app:", fav_apps[1])
print("4th app:", fav_apps[3])
"""

# ------------------------------------------------------------------------------------


# Task 3: Try to Change the First Element (Immutability)

"""
fav_apps = ('Instagram', 'Zomato', 'Spotify', 'WhatsApp', 'Flipkart')

# Tuples are immutable, so their elements cannot be changed.
# The following line raises a TypeError.

fav_apps[0] = 'YouTube'

print(fav_apps)
"""

# ------------------------------------------------------------------------------------


# Task 4: Print the Middle Three Apps Using Slicing

"""
fav_apps = ('Instagram', 'Zomato', 'Spotify', 'WhatsApp', 'Flipkart')

print("Middle three apps:", fav_apps[1:4])
"""

# ------------------------------------------------------------------------------------


# Task 5: Concatenate Two Tuples

"""
fav_apps = ('Instagram', 'Zomato', 'Spotify', 'WhatsApp', 'Flipkart')

new_apps = ('Telegram', 'Pinterest')

all_apps = fav_apps + new_apps

print("All apps:", all_apps)
"""

# ------------------------------------------------------------------------------------
