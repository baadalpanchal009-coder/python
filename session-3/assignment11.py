# Session 11 - Database Connecting with Python
# PyMySQL, MySQL Connectivity, Insert, Fetch, Update, Delete
# ------------------------------------------------------------------------------------
# Task 1: Connect to Local MySQL Server

# """

# Install PyMySQL using:
# pip install pymysql
# File: connect_demo.py

# import pymysql

# connection = None

# try: connection = pymysql.connect( host='localhost', user='root', password='your_password' )

# print('Connection successful')


# except pymysql.MySQLError as e: print('Connection failed:', e)

# finally: if connection: connection.close() """

# ------------------------------------------------------------------------------------
# Task 2: Create Database, Table and Insert Three Playlists

# """ import pymysql

# connection = None cursor = None

# try: connection = pymysql.connect( host='localhost', user='root', password='your_password' )

# cursor = connection.cursor()

# cursor.execute('CREATE DATABASE IF NOT EXISTS music_stream')
# cursor.execute('USE music_stream')

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS playlists (
#         id INT PRIMARY KEY AUTO_INCREMENT,
#         name VARCHAR(100),
#         song_count INT
#     )
# ''')

# playlists = [
#     ('Chill Vibes', 15),
#     ('Workout Hits', 20),
#     ('Romantic Songs', 8)
# ]

# cursor.executemany(
#     'INSERT INTO playlists (name, song_count) VALUES (%s, %s)',
#     playlists
# )

# connection.commit()

# print('Three playlists inserted successfully')


# except pymysql.MySQLError as e: print('Database error:', e)

# finally: if cursor: cursor.close() if connection: connection.close() """

# ------------------------------------------------------------------------------------
# Task 3: Fetch Playlists Where Song Count Is Greater Than 10

# """ import pymysql

# connection = None cursor = None

# try: connection = pymysql.connect( host='localhost', user='root', password='your_password', database='music_stream' )

# cursor = connection.cursor()

# cursor.execute(
#     'SELECT name, song_count FROM playlists WHERE song_count > %s',
#     (10,)
# )

# playlists = cursor.fetchall()

# for playlist in playlists:
#     print('Playlist Name:', playlist[0])
#     print('Song Count:', playlist[1])
#     print()


# except pymysql.MySQLError as e: print('Database error:', e)

# finally: if cursor: cursor.close() if connection: connection.close() """

# ------------------------------------------------------------------------------------
# Task 4: Update Playlist Name

# """ import pymysql

# connection = None cursor = None

# try: connection = pymysql.connect( host='localhost', user='root', password='your_password', database='music_stream' )

# cursor = connection.cursor()

# cursor.execute(
#     'UPDATE playlists SET name = %s WHERE name = %s',
#     ('Chill Hits', 'Chill Vibes')
# )

# connection.commit()

# if cursor.rowcount > 0:
#     print('Playlist name updated successfully')
# else:
#     print('Playlist not found or name unchanged')


# except pymysql.MySQLError as e: print('Database error:', e)

# finally: if cursor: cursor.close() if connection: connection.close() """

# ------------------------------------------------------------------------------------
# Task 5: Delete a Playlist by ID Using try-except

# """ import pymysql

# def delete_playlist(playlist_id): connection = None cursor = None

# try:
#     connection = pymysql.connect(
#         host='localhost',
#         user='root',
#         password='your_password',
#         database='music_stream'
#     )

#     cursor = connection.cursor()

#     cursor.execute(
#         'DELETE FROM playlists WHERE id = %s',
#         (playlist_id,)
#     )

#     connection.commit()

#     if cursor.rowcount > 0:
#         print('Playlist deleted successfully')
#     else:
#         print('Playlist ID does not exist')

# except pymysql.MySQLError as e:
#     print('Database error:', e)

# finally:
#     if cursor:
#         cursor.close()
#     if connection:
#         connection.close()


# delete_playlist(1) """

# ------------------------------------------------------------------------------------