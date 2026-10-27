
# Session 3 - Custom Exceptions
# raise Keyword, Creating User-Defined Exceptions
# ------------------------------------------------------------------------------------


# Task 1: Create InvalidCouponCodeError

"""
class InvalidCouponCodeError(Exception):
    pass


def apply_coupon(coupon_code):
    valid_coupons = ['SAVE10', 'FOOD20', 'ZOMATO50']

    if coupon_code not in valid_coupons:
        raise InvalidCouponCodeError("Invalid coupon code!")

    print("Coupon applied successfully:", coupon_code)


try:
    apply_coupon('SAVE10')
    apply_coupon('INVALID50')

except InvalidCouponCodeError as error:
    print(error)
"""

# ------------------------------------------------------------------------------------


# Task 2: Create SongAlreadyExistsError

"""
class SongAlreadyExistsError(Exception):
    pass


def add_song_to_playlist(song_name, playlist):
    if song_name in playlist:
        raise SongAlreadyExistsError(
            f"'{song_name}' already exists in the playlist!"
        )

    playlist.append(song_name)
    return playlist


playlist = ['Kesariya', 'Believer']

try:
    add_song_to_playlist('Shape of You', playlist)
    print("Updated playlist:", playlist)

    add_song_to_playlist('Kesariya', playlist)

except SongAlreadyExistsError as error:
    print(error)
"""

# ------------------------------------------------------------------------------------


# Task 3: Create PaymentFailedError

"""
class PaymentFailedError(Exception):
    pass


def process_payment(amount):
    if amount <= 0:
        raise PaymentFailedError(
            "Payment amount must be greater than zero."
        )

    print("Payment Successful")


try:
    process_payment(500)
    process_payment(-100)

except PaymentFailedError as error:
    print(error)
"""

# ------------------------------------------------------------------------------------


# Task 4: Explain and Fix the NameError Traceback

"""
# Original buggy code:
# raise InvalidSeatNumberError(
#     'Seat number must be positive'
# )

# Explanation:
# NameError occurs because Python does not know what
# InvalidSeatNumberError is. The exception class has not
# been defined or imported before it is used.

# Corrected code:

class InvalidSeatNumberError(Exception):
    pass


def book_ticket(movie_name, seat_number):
    if seat_number <= 0:
        raise InvalidSeatNumberError(
            'Seat number must be positive'
        )

    print(f"Ticket booked for {movie_name}, seat {seat_number}")


try:
    book_ticket('Avengers', -2)

except InvalidSeatNumberError as error:
    print("Booking error:", error)
"""

# ------------------------------------------------------------------------------------
