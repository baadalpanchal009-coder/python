# Session 9 - Regex (re module)
# match(), search(), findall()
# ------------------------------------------------------------------------------------
# Task 1: Validate Gmail Using re.match()

# """ import re

# email = input("Enter your Gmail address: ")

# pattern = r"[a-z][a-zA-Z0-9._%+-]*@gmail.com"

# if re.match(pattern, email) and email.endswith("@gmail.com"): print("Valid Gmail") else: print("Invalid Gmail") """

# ------------------------------------------------------------------------------------
# Task 2: Find a 10-Digit Mobile Number Using re.search()

# """ import re

# text = "Food was delicious! Contact: 9876543210. Delivery support: 9123456789."

# pattern = r"\b[0-9]{10}\b"

# match = re.search(pattern, text)

# if match: print("Mobile Number:", match.group()) else: print("No mobile number found") """

# ------------------------------------------------------------------------------------
# Task 3: Extract Hashtags Using re.findall()

# """ import re

# def extract_hashtags(text): return re.findall(r"#[a-zA-Z0-9_]+", text)

# caption = "Enjoying my day! #Foodie #Travel #Instagram2026"

# hashtags = extract_hashtags(caption)

# print("Hashtags:", hashtags) """

# ------------------------------------------------------------------------------------
# Task 4: Filter Order IDs Ending with an Even Number

# """ import re

# order_ids = ['ORD1234', 'ORD5678', 'ORD9999', 'ORD0001']

# pattern = r"ORD[0-9]*[02468]"

# print("Order IDs ending with an even number:")

# for order_id in order_ids: if re.match(pattern, order_id): print(order_id) """

# ------------------------------------------------------------------------------------
# Task 5: Validate Indian Railways PNR Number Using re.match()

# """ import re

# def is_valid_pnr(pnr): pattern = r"[0-9]{10}" return re.match(pattern, pnr) is not None and len(pnr) == 10

# pnr = input("Enter your 10-digit PNR number: ")

# if is_valid_pnr(pnr): print("Valid PNR") else: print("Invalid PNR") """

# ------------------------------------------------------------------------------------