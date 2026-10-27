
# Session 2 - Dictionaries Deep Dive
# Updating values, nested dictionaries
# ------------------------------------------------------------------------------------


# Task 1: Create Playlist and Update Song Duration

"""
playlist = {
    'Kesariya': 240,
    'Apna Bana Le': 225,
    'Tum Hi Ho': 260
}

playlist['Kesariya'] = 250

print("Updated playlist:", playlist)
"""

# ------------------------------------------------------------------------------------


# Task 2: Create Nested User Profiles

"""
user_profiles = {
    'raj_07': {
        'followers': 2500,
        'following': 500,
        'posts': 120
    },
    'ananya_xo': {
        'followers': 4500,
        'following': 700,
        'posts': 95
    }
}

print("Ananya's followers:", user_profiles['ananya_xo']['followers'])
"""

# ------------------------------------------------------------------------------------


# Task 3: Create and Update a Restaurant Menu

"""
restaurants = {
    'Burger Hub': {
        'cuisine': 'Fast Food',
        'rating': 4.2
    },
    'Pizza Point': {
        'cuisine': 'Italian',
        'rating': 4.0
    }
}

restaurants['Pizza Point']['rating'] = 4.5

print("Updated restaurant menu:", restaurants)
"""

# ------------------------------------------------------------------------------------


# Task 4: Add GT to the IPL Team Squad

"""
team = {
    'CSK': {'captain': 'Dhoni', 'players': 18},
    'MI': {'captain': 'Rohit', 'players': 17}
}

team['GT'] = {'captain': 'Hardik', 'players': 16}

for team_name, details in team.items():
    print(team_name, "-", details['captain'])
"""

# ------------------------------------------------------------------------------------
