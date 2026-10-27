
# Session 3 - Exception Handling Basics
# try, except, Multiple Exceptions
# ------------------------------------------------------------------------------------


# Task 1: Handle Song Not Found Exception

"""
def get_song_duration(song_name):
    songs = {
        'Kesariya': 4.28,
        'Believer': 3.24,
        'Shape of You': 3.53,
        'Tum Hi Ho': 4.22
    }

    try:
        return songs[song_name]
    except KeyError:
        print("Song not found on Spotify!")


duration = get_song_duration('Kesariya')

if duration is not None:
    print("Song duration:", duration, "minutes")
"""

# ------------------------------------------------------------------------------------


# Task 2: Flipkart Order Summary with ValueError Handling

"""
try:
    price = float(input("Enter product price: ₹"))
    quantity = int(input("Enter quantity: "))

    total = price * quantity

    print("Total order amount: ₹", total)

except ValueError:
    print("Error: Please enter a valid numeric price and quantity.")
"""

# ------------------------------------------------------------------------------------


# Task 3: Movie Ticket Booking with Multiple Exceptions

"""
def book_movie_ticket():
    wallet_balance = 1000

    try:
        tickets = int(input("Enter number of tickets: "))

        price_per_ticket = wallet_balance / tickets

        print("Price per ticket: ₹", price_per_ticket)

    except ZeroDivisionError:
        print("Error: Number of tickets cannot be zero.")

    except ValueError:
        print("Error: Please enter a valid whole number.")


book_movie_ticket()
"""

# ------------------------------------------------------------------------------------


# Task 4: Handle IndexError and KeyError

"""
my_list = [1, 2, 3]
my_dict = {'a': 1}

try:
    print(my_list[5])

except IndexError:
    print("Error: List index does not exist.")

try:
    print(my_dict['b'])

except KeyError:
    print("Error: Dictionary key does not exist.")
"""

# ------------------------------------------------------------------------------------
