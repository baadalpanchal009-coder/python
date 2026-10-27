
# Session 2 - File Pointer & Cursor Control
# tell(), seek(), Reading Line-by-Line
# ------------------------------------------------------------------------------------


# Task 1: Check File Pointer Position Using tell()

"""
with open('lyrics.txt', 'r') as file:
    print("Initial position:", file.tell())

    content = file.read(10)
    print("First 10 characters:", content)

    print("Position after reading:", file.tell())
"""

# ------------------------------------------------------------------------------------


# Task 2: Read the Next Line After Seeking to Byte 20

"""
def read_next_line(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        file.seek(20)
        line = file.readline()
        print("Line from position 20:", line)


read_next_line('lyrics.txt')
"""

# ------------------------------------------------------------------------------------


# Task 3: Create and Read Zomato-Style Order History

"""
# Create orders.txt with five orders
with open('orders.txt', 'w') as file:
    file.write('Order 101 - Pizza\n')
    file.write('Order 102 - Burger\n')
    file.write('Order 103 - Dosa\n')
    file.write('Order 104 - Pasta\n')
    file.write('Order 105 - Fries\n')


# Read orders line-by-line and display file pointer position
with open('orders.txt', 'r') as file:
    while True:
        order = file.readline()

        if not order:
            break

        print("Order:", order.strip())
        print("File pointer position:", file.tell())
"""

# ------------------------------------------------------------------------------------


# Task 4: Read Only the Third Song Using seek() and readline()

"""
with open('playlist.txt', 'r') as file:
    file.readline()  # Skip first song
    file.readline()  # Skip second song

    third_song = file.readline()

    print("Third song:", third_song.strip())
"""

# ------------------------------------------------------------------------------------
