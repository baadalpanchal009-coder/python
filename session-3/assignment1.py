
# Session 3 - File Handling Basics
# open(), read(), write(), File Modes: r, w, a
# ------------------------------------------------------------------------------------


# Task 1: Write 5 Favorite Songs into a Text File

"""
with open('my_fav_songs.txt', 'w') as file:
    file.write('Kesariya\n')
    file.write('Shape of You\n')
    file.write('Believer\n')
    file.write('Tum Hi Ho\n')
    file.write('Perfect\n')

print("Songs written successfully!")
"""

# ------------------------------------------------------------------------------------


# Task 2: Read Songs with Line Numbers

"""
with open('my_fav_songs.txt', 'r') as file:
    for line_number, song in enumerate(file, start=1):
        print(f"{line_number}. {song.strip()}")
"""

# ------------------------------------------------------------------------------------


# Task 3: Append 2 More Songs Without Deleting Existing Content

"""
with open('my_fav_songs.txt', 'a') as file:
    file.write('Heeriye\n')
    file.write('Apna Bana Le\n')

print("Two songs added successfully!")
"""

# ------------------------------------------------------------------------------------


# Task 4: Count the Total Number of Songs

"""
with open('my_fav_songs.txt', 'r') as file:
    songs = file.readlines()

total_songs = len(songs)

print("Total songs:", total_songs)
"""

# ------------------------------------------------------------------------------------

