
# Session 2 - Packages
# Creating packages, __init__.py usage
# ------------------------------------------------------------------------------------


# Task 1: Create musicplayer Package

"""
# File: musicplayer/__init__.py
# This file can remain empty.

# File: musicplayer/player.py

def play_song():
    print("Playing song...")


# File: main.py

from musicplayer.player import play_song

play_song()
"""

# ------------------------------------------------------------------------------------


# Task 2: Create foodorder Package

"""
# File: foodorder/menu.py

def get_menu():
    return ['Pizza', 'Burger', 'Dosa', 'Pasta']


# File: foodorder/order.py

def place_order(item):
    print(f"Order placed for: {item}")


# File: foodorder/__init__.py

from .menu import get_menu
from .order import place_order


# File: main.py

from foodorder import get_menu, place_order

print("Menu:", get_menu())
place_order('Pizza')
"""

# ------------------------------------------------------------------------------------


# Task 3: Create shoppingcart Package

"""
# File: shoppingcart/actions.py

def add_to_cart(item, cart):
    cart.append(item)
    return cart


# File: shoppingcart/__init__.py

from .actions import add_to_cart


# File: main.py

from shoppingcart import add_to_cart

cart = []
add_to_cart('Mobile', cart)
add_to_cart('Headphones', cart)

print("Shopping cart:", cart)
"""

# ------------------------------------------------------------------------------------


# Task 4: Create instahelpers Package

"""
# File: instahelpers/__init__.py

def format_likes(count):
    if count >= 1000000:
        return f"{count / 1000000:.1f}M"
    elif count >= 1000:
        return f"{count / 1000:.1f}K"
    else:
        return count


# File: main.py

from instahelpers import format_likes

print(format_likes(1200))
print(format_likes(1500000))
print(format_likes(850))
"""

# ------------------------------------------------------------------------------------


# Task 5: Create ticketbooking Package

"""
# File: ticketbooking/search.py

def search_event(event_name):
    print(f"Searching for event: {event_name}")


# File: ticketbooking/booking.py

def book_ticket(event_name):
    print(f"Ticket booked for: {event_name}")


# File: ticketbooking/__init__.py

from .search import search_event
from .booking import book_ticket


# File: main.py

from ticketbooking import search_event, book_ticket

search_event('IPL Final')
book_ticket('IPL Final')
"""

# ------------------------------------------------------------------------------------
