
# Session 2 - Dynamic Nested Dictionary Creation
# ------------------------------------------------------------------------------------


# Task 1: Create a Dynamic Flipkart Shopping Cart

"""
cart = {}

cart['badal_21'] = {
    'Mobile': {'name': 'Samsung Mobile', 'quantity': 1, 'price': 15000},
    'Headphones': {'name': 'Boat Headphones', 'quantity': 2, 'price': 1200}
}

cart['raj_07'] = {
    'Shoes': {'name': 'Nike Shoes', 'quantity': 1, 'price': 3500},
    'Watch': {'name': 'Smart Watch', 'quantity': 2, 'price': 2500}
}

print("Shopping Cart:")
print(cart)
"""

# ------------------------------------------------------------------------------------


# Task 2: Add Songs Dynamically to a User's Playlist

"""
def add_song_to_playlist(playlists, user, playlist_name, song_title, artist):
    if user not in playlists:
        playlists[user] = {}

    if playlist_name not in playlists[user]:
        playlists[user][playlist_name] = []

    song = {'title': song_title, 'artist': artist}
    playlists[user][playlist_name].append(song)

    return playlists


playlists = {}

add_song_to_playlist(
    playlists, 'badal', 'Favourites', 'Kesariya', 'Arijit Singh'
)

add_song_to_playlist(
    playlists, 'badal', 'Favourites', 'Tum Hi Ho', 'Arijit Singh'
)

add_song_to_playlist(
    playlists, 'raj', 'Chill', 'Perfect', 'Ed Sheeran'
)

print("Spotify Playlists:")
print(playlists)
"""

# ------------------------------------------------------------------------------------


# Task 3: Store IPL Team Scores Dynamically

"""
ipl_scores = {}

ipl_scores['CSK'] = {
    'Dhoni': 25,
    'Ruturaj': 75,
    'Jadeja': 30
}

ipl_scores['MI'] = {
    'Rohit': 60,
    'Surya': 85,
    'Hardik': 20
}

print("IPL Scores:")
print(ipl_scores)

# Print a specific player's score
player = 'Surya'
team = 'MI'

print(player, "scored", ipl_scores[team][player], "runs")
"""

# ------------------------------------------------------------------------------------


# Task 4: Add and Update Zomato Orders

"""
def add_order(orders, order_id, restaurant, items, total):
    orders[order_id] = {
        'restaurant': restaurant,
        'items': items,
        'total': total
    }
    return orders


def update_order_total(orders, order_id, new_total):
    if order_id in orders:
        orders[order_id]['total'] = new_total
    else:
        print("Order ID not found:", order_id)

    return orders


orders = {}

add_order(
    orders, 101, 'Pizza Hut', ['Pizza', 'Garlic Bread'], 650
)

add_order(
    orders, 102, 'Burger King', ['Burger', 'Fries'], 350
)

update_order_total(orders, 101, 700)

print("Zomato Orders:")
print(orders)
"""

# ------------------------------------------------------------------------------------


# Task 5: Prevent KeyError with Dynamic Playlist Creation

"""
playlists = {
    'user1': {
        'Favourites': ['Song1', 'Song2']
    }
}

# Create missing user and playlist automatically
playlists.setdefault('user2', {})
playlists['user2'].setdefault('Chill', [])

# Add a song
playlists['user2']['Chill'].append('Song3')

print("Updated Playlists:")
print(playlists)
"""

# ------------------------------------------------------------------------------------
