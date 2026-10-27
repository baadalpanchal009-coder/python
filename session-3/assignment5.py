
# Session 3 - Classes & Objects
# Class Structure, __init__ Method, Creating Objects
# ------------------------------------------------------------------------------------


# Task 1: Create a Song Class and Two Objects

"""
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration


song1 = Song('Kesariya', 'Arijit Singh', 268)
song2 = Song('Believer', 'Imagine Dragons', 204)

print(song1.title, "-", song1.artist, "-", song1.duration, "seconds")
print(song2.title, "-", song2.artist, "-", song2.duration, "seconds")
"""

# ------------------------------------------------------------------------------------


# Task 2: Create a FoodOrder Class

"""
class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

    def show_order(self):
        print("Restaurant:", self.restaurant_name)
        print("Items:", ", ".join(self.items))
        print("Total Price: ₹", self.total_price)


order1 = FoodOrder(
    'Pizza Hut',
    ['Pizza', 'Garlic Bread', 'Cold Drink'],
    650
)

order1.show_order()
"""

# ------------------------------------------------------------------------------------


# Task 3: Create an InstagramPost Class

"""
class InstagramPost:
    def __init__(self, caption, likes, comments):
        self.caption = caption
        self.likes = likes
        self.comments = comments

    def add_comment(self, comment_text):
        self.comments.append(comment_text)
        self.likes += 1


post1 = InstagramPost(
    'Enjoying my weekend!',
    100,
    ['Amazing photo!', 'Nice post!']
)

post1.add_comment('Beautiful!')
 
print("Caption:", post1.caption)
print("Likes:", post1.likes)
print("Comments:", post1.comments)
"""

# ------------------------------------------------------------------------------------


# Task 4: Fix the Movie Class Bug

"""
class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating


m = Movie('Jawan', 4.5)

print(m.title, m.rating)
"""

# ------------------------------------------------------------------------------------
