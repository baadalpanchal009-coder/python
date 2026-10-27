
# Session 11 - Dictionaries
# Key/value pairs, adding/updating entries, keys(), values(), items()
# ------------------------------------------------------------------------------------


# Task 1: Create and Print a Music Playlist Dictionary

"""
my_playlist = {
    'Kesariya': 4.5,
    'Apna Bana Le': 4.0,
    'Tum Hi Ho': 4.2
}

print("My Playlist:", my_playlist)
"""

# ------------------------------------------------------------------------------------


# Task 2: Add a New Song and Update an Existing Song

"""
my_playlist = {
    'Kesariya': 4.5,
    'Apna Bana Le': 4.0,
    'Tum Hi Ho': 4.2
}

my_playlist['Heeriye'] = 3.5
my_playlist['Kesariya'] = 4.8

print("Updated Playlist:", my_playlist)
"""

# ------------------------------------------------------------------------------------


# Task 3: Display Instagram Friends and Their Followers

"""
def display_friends(friends):
    for username, followers in friends.items():
        if followers >= 1000:
            count = round(followers / 1000, 1)
            print(f"{username}: {count}K followers")
        else:
            print(f"{username}: {followers} followers")


instagram_friends = {
    'rahul': 2300,
    'priya': 1500,
    'amit': 850
}

display_friends(instagram_friends)
"""

# ------------------------------------------------------------------------------------


# Task 4: Use keys(), values(), and items()

"""
food_order = {
    'Pizza': 2,
    'Burger': 1,
    'Fries': 3
}

print("Food items:", food_order.keys())

print("Quantities:", food_order.values())

print("Items with quantities:")
for item, quantity in food_order.items():
    print(item, ":", quantity)
"""

# ------------------------------------------------------------------------------------


# Task 5: Update a Flipkart-Style Shopping Cart

"""
def update_cart(cart, item, qty):
    if item in cart:
        cart[item] += qty
    else:
        cart[item] = qty

    return cart


cart = {
    'Mobile': 1,
    'Headphones': 2
}

cart = update_cart(cart, 'Mobile', 2)
cart = update_cart(cart, 'Laptop', 1)

print("Updated Shopping Cart:", cart)
"""

# ------------------------------------------------------------------------------------
