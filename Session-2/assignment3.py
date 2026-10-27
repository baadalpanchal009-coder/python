
# Session 2 - List Transformations
# round(), sorted(), sort(), zip() usage
# ------------------------------------------------------------------------------------


# Task 1: Round Cricket Scores

"""
scores = [56.7, 102.3, 88.9, 45.2, 120.8]

rounded_scores = []

for score in scores:
    rounded_scores.append(round(score))

print("Original scores:", scores)
print("Rounded scores:", rounded_scores)
"""

# ------------------------------------------------------------------------------------


# Task 2: Sort Restaurant Ratings in Descending Order

"""
ratings = [4.2, 3.8, 4.9, 2.5, 4.0]

sorted_ratings = sorted(ratings, reverse=True)

print("Ratings in descending order:", sorted_ratings)
"""

# ------------------------------------------------------------------------------------


# Task 3: Sort Flipkart Product Names Alphabetically

"""
products = [
    'Smartphone',
    'Laptop',
    'Headphones',
    'Mouse',
    'Keyboard'
]

products.sort()

print("Alphabetically sorted products:", products)
"""

# ------------------------------------------------------------------------------------


# Task 4: Pair Restaurants with Delivery Times Using zip()

"""
restaurants = ['Burger Hub', 'Pizza Point', 'Sushi House']
delivery_times = [30, 25, 40]

for restaurant, time in zip(restaurants, delivery_times):
    print(f"{restaurant} - {time} min")
"""

# ------------------------------------------------------------------------------------


# Task 5: Pair YouTube Titles with Rounded View Counts

"""
def pair_videos_with_views(titles, view_counts):
    return [
        (title, round(views / 1000) * 1000)
        for title, views in zip(titles, view_counts)
    ]


video_titles = [
    'Python Tutorial',
    'Gaming Highlights',
    'Travel Vlog'
]

view_counts = [12450, 87600, 234500]

result = pair_videos_with_views(video_titles, view_counts)

print("Video titles and rounded views:")
print(result)
"""

# ------------------------------------------------------------------------------------
