
# Session 2 - Tuples Advanced
# Creating mixed tuples, slicing rules, tuple <-> list conversion
# ------------------------------------------------------------------------------------


# Task 1: Create a Tuple with Personal Profile

"""
my_profile = ('Baadal', 20, 'Pizza', True)

print("My Profile:", my_profile)
"""

# ------------------------------------------------------------------------------------


# Task 2: Print the 2nd, 3rd, and 4th Songs Using Slicing

"""
playlist = (
    'Shape of You',
    'Blinding Lights',
    'Believer',
    'Senorita',
    'Levitating'
)

print("Selected songs:", playlist[1:4])
"""

# ------------------------------------------------------------------------------------


# Task 3: Convert Tuple to List, Add Item, Convert Back to Tuple

"""
order = ('Burger', 'Fries', 'Coke')

order_list = list(order)

order_list.append('Ice Cream')

order = tuple(order_list)

print("Final order:", order)
"""

# ------------------------------------------------------------------------------------


# Task 4: Create a Mixed Tuple and Print Element Types

"""
insta_post = (
    101,
    'baadal',
    2500,
    ['Python', 'Coding', 'Learning'],
    True
)

print("Instagram Post:", insta_post)

for element in insta_post:
    print(element, "->", type(element))
"""

# ------------------------------------------------------------------------------------


# Task 5: Remove WhatsApp Calls Shorter Than 5 Minutes

"""
call_durations = (12, 5, 0, 20, 7, 3, 15)

duration_list = list(call_durations)

filtered_durations = [
    duration for duration in duration_list
    if duration >= 5
]

call_durations = tuple(filtered_durations)

print("Call durations of 5 minutes or more:", call_durations)
"""

# ------------------------------------------------------------------------------------
