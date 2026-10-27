
# Session 3 - Inheritance
# Single, Multilevel, Multiple Inheritance
# ------------------------------------------------------------------------------------


# Task 1: Create a User Class

"""
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


user1 = User('badal_21', 'badal@example.com')

print("Username:", user1.username)
print("Email:", user1.email)
"""

# ------------------------------------------------------------------------------------


# Task 2: Single Inheritance - Influencer Inherits from User

"""
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers


influencer1 = Influencer('badal_21', 'badal@example.com', 15000)

print("Username:", influencer1.username)
print("Email:", influencer1.email)
print("Followers:", influencer1.followers)
"""

# ------------------------------------------------------------------------------------


# Task 3: Multilevel Inheritance - VerifiedInfluencer

"""
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers


class VerifiedInfluencer(Influencer):
    def __init__(self, username, email, followers, badge):
        super().__init__(username, email, followers)
        self.badge = badge


verified_user = VerifiedInfluencer(
    'badal_21',
    'badal@example.com',
    150000,
    True
)

print("Username:", verified_user.username)
print("Email:", verified_user.email)
print("Followers:", verified_user.followers)
print("Verified Badge:", verified_user.badge)
"""

# ------------------------------------------------------------------------------------


# Task 4: Multiple Inheritance - BrandPartner

"""
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers


class Brand:
    def __init__(self, brand_name):
        self.brand_name = brand_name


class BrandPartner(Influencer, Brand):
    def __init__(self, username, email, followers, brand_name):
        Influencer.__init__(self, username, email, followers)
        Brand.__init__(self, brand_name)


partner = BrandPartner(
    'badal_21',
    'badal@example.com',
    25000,
    'Nike'
)

print("Username:", partner.username)
print("Followers:", partner.followers)
print("Brand Name:", partner.brand_name)
"""

# ------------------------------------------------------------------------------------


# Task 5: VerifiedInfluencer with Instagram-Style Profile

"""
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers


class VerifiedInfluencer(Influencer):
    def __init__(self, username, email, followers, badge):
        super().__init__(username, email, followers)
        self.badge = badge

    def format_followers(self):
        if self.followers >= 1_000_000:
            return f"{self.followers / 1_000_000:.1f}M"
        elif self.followers >= 1_000:
            return f"{self.followers / 1_000:.1f}K"
        else:
            return str(self.followers)

    def display_profile(self):
        print("Username:", self.username)
        print("Followers:", self.format_followers())
        print("Verified Badge:", "Yes" if self.badge else "No")


profile = VerifiedInfluencer(
    'badal_21',
    'badal@example.com',
    1500000,
    True
)

profile.display_profile()
"""

# ------------------------------------------------------------------------------------
