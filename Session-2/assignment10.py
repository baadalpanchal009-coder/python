
# Session 2 - Custom Modules
# File: playlist.py
# ------------------------------------------------------------------------------------


# Task 1: Add a Song to the Playlist

"""
def add_song(song_name, playlist):
    playlist.append(song_name)
    return playlist
"""

# ------------------------------------------------------------------------------------


# Task 3: Remove a Song from the Playlist

"""
def remove_song(song_name, playlist):
    if song_name in playlist:
        playlist.remove(song_name)
    else:
        print(song_name, "not found in playlist")

    return playlist
"""

# ------------------------------------------------------------------------------------


# Task 4: Display Playlist with Position Numbers

"""
def display_playlist(playlist):
    for index, song in enumerate(playlist, start=1):
        print(f"{index}. {song}")
"""

# ------------------------------------------------------------------------------------
