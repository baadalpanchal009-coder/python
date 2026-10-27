# Session 8 - Modules & Packages
# Import Module, Creating Own Module, Math & Random Modules
# ------------------------------------------------------------------------------------
# Task 1: Create a Greet Module

# """

# File: greet_module.py

# def greet_user(name): print('Hello,', name, '!')

# """

# File: main.py

# """ import greet_module

# greet_module.greet_user('Badal') """

# ------------------------------------------------------------------------------------
# Task 2: BMI Calculator Using Math Module

# """ import math

# weight = float(input('Enter weight in kg: ')) height = float(input('Enter height in meters: '))

# bmi = weight / math.pow(height, 2)

# print('BMI:', round(bmi, 2)) """

# ------------------------------------------------------------------------------------
# Task 3: Shuffle a Playlist Using Random Module

# """ import random

# song_list = [ 'Kesariya', 'Believer', 'Perfect', 'Shape of You', 'Chaleya' ]

# random.shuffle(song_list)

# print('Shuffled Playlist:')

# for song in song_list: print(song) """

# ------------------------------------------------------------------------------------
# Task 4: Create a Package - insta_utils

# """

# File: insta_utils/likes.py

# def like_count(current, increment): return current + increment

# File: insta_utils/comments.py

# def comment_count(current, new_comments): return current + new_comments

# File: main.py

# from insta_utils import likes, comments

# current_likes = 100 new_likes = 25

# current_comments = 10 new_comments = 5

# total_likes = likes.like_count(current_likes, new_likes) total_comments = comments.comment_count( current_comments, new_comments )

# print('Total Likes:', total_likes) print('Total Comments:', total_comments) """

# ------------------------------------------------------------------------------------
# Task 5: Import Song List from a Separate Module

# """

# File: songs.py

# song_list = [ 'Kesariya', 'Believer', 'Perfect', 'Shape of You', 'Chaleya' ]

# File: random_playlist.py

# import random from songs import song_list

# random.shuffle(song_list)

# print('Shuffled Playlist:')

# for song in song_list: print(song) """

# ------------------------------------------------------------------------------------