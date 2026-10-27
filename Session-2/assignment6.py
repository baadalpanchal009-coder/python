
# Session 2 - Converting Lists to Dictionary
# Using zip(), loops
# ------------------------------------------------------------------------------------


# Task 1: Convert Product Names and Prices into a Dictionary Using zip()

"""
products = ['Mobile', 'Laptop', 'Headphones', 'Mouse']
prices = [15000, 55000, 2000, 800]

product_prices = dict(zip(products, prices))

print("Product prices:", product_prices)
"""

# ------------------------------------------------------------------------------------


# Task 2: Create a Dictionary Using a Loop Without zip()

"""
usernames = ['raj_07', 'ananya_xo', 'baadal_21']
followers = [2500, 4500, 1800]

instagram_followers = {}

for index in range(len(usernames)):
    instagram_followers[usernames[index]] = followers[index]

print("Instagram followers:", instagram_followers)
"""

# ------------------------------------------------------------------------------------


# Task 3: Print IPL Teams with More Than 10 Points

"""
teams = ['CSK', 'MI', 'GT', 'RCB', 'KKR']
points = [12, 8, 15, 10, 14]

team_points = dict(zip(teams, points))

print("Teams with more than 10 points:")

for team, point in team_points.items():
    if point > 10:
        print(team, "-", point, "points")
"""

# ------------------------------------------------------------------------------------


# Task 4: Create a List of Movie Dictionaries Using zip()

"""
titles = ['3 Idiots', 'Dangal', 'Jawan']
genres = ['Comedy-Drama', 'Sports-Drama', 'Action']
ratings = [8.4, 8.3, 7.0]

movies = [
    {'title': title, 'genre': genre, 'rating': rating}
    for title, genre, rating in zip(titles, genres, ratings)
]

print("Movie details:", movies)
"""

# ------------------------------------------------------------------------------------

