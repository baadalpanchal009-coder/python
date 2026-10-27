
# Session 8 - Strings
# Indexing, Slicing, String Methods
# ------------------------------------------------------------------------------------


# Task 1: Instagram Caption - Print First 10 Characters
# File name: insta_caption.py

"""
caption = input("Enter your Instagram caption: ")

print("First 10 characters:", caption[:10])
"""

# ------------------------------------------------------------------------------------


# Task 2: Extract Artist Name from Song Title

"""
def extract_artist(song_title):
    dash_index = song_title.index("-")
    artist_name = song_title[dash_index + 1:].strip()
    return artist_name


song = input("Enter song title (Song Name - Artist Name): ")

print("Artist Name:", extract_artist(song))
"""

# ------------------------------------------------------------------------------------


# Task 3: Reverse a Message Without reversed() or [::-1]

"""
def reverse_message(message):
    reversed_text = ""

    for character in message:
        reversed_text = character + reversed_text

    return reversed_text


text = input("Enter a message: ")

print("Reversed message:", reverse_message(text))
"""

# ------------------------------------------------------------------------------------


# Task 4: Extract First Word, Last Word, and Total Words

"""
description = input("Enter Flipkart product description: ")

words = description.split()

if len(words) > 0:
    print("First word:", words[0])
    print("Last word:", words[-1])
    print("Total words:", len(words))
else:
    print("No words found in the description.")
"""

# ------------------------------------------------------------------------------------


# Task 5: Mask a 10-Digit Phone Number

"""
def mask_phone_number(phone):
    if len(phone) != 10 or not phone.isdigit():
        return "Invalid phone number! Enter exactly 10 digits."

    return "*" * 6 + phone[-4:]


number = input("Enter your 10-digit phone number: ")

print("Masked phone number:", mask_phone_number(number))
"""

# ------------------------------------------------------------------------------------
