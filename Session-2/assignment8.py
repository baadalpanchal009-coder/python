
# Session 2 - Functions Revisited
# Keyword & Positional Arguments, Default Values
# ------------------------------------------------------------------------------------


# Task 1: Calculate Total Using Positional Arguments

"""
def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(120, 3)

print("Total price: ₹", total)
"""

# ------------------------------------------------------------------------------------


# Task 2: Format Username Using a Default Prefix

"""
def format_username(username, prefix='user_'):
    return prefix + username


print(format_username('badal'))
print(format_username('badal', 'insta_'))
"""

# ------------------------------------------------------------------------------------


# Task 3: Book Movie Tickets Using Positional and Keyword Arguments

"""
def book_movie_ticket(movie_name, seat_type='Regular', snacks=None):
    print("Movie:", movie_name)
    print("Seat type:", seat_type)
    print("Snacks:", snacks if snacks is not None else 'None')
    print("-------------------------")


# Positional arguments
book_movie_ticket('Jawan', 'Regular', 'Popcorn')

# Only keyword arguments
book_movie_ticket(
    movie_name='Pathaan',
    seat_type='VIP',
    snacks='Nachos'
)

# Mix of positional and keyword arguments
book_movie_ticket('Jawan', snacks='Popcorn', seat_type='VIP')
"""

# ------------------------------------------------------------------------------------


# Task 4: Apply Coupon Discount

"""
def apply_coupon(amount, coupon_code=None):
    if coupon_code == 'SAVE10':
        amount = amount - (amount * 10 / 100)

    return amount


print("Without coupon: ₹", apply_coupon(1000))
print("With coupon: ₹", apply_coupon(1000, 'SAVE10'))
"""

# ------------------------------------------------------------------------------------
