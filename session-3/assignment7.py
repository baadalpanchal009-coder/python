# Session 7 - Polymorphism
# Method Overloading (Conceptual in Python), Method Overriding
# ------------------------------------------------------------------------------------
# Task 1: Method Overriding - InstaStory and WhatsAppStory

# """ class InstaStory: def share(self): print('Sharing an image story')

# class WhatsAppStory(InstaStory): def share(self): print('Sharing a text status')

# insta = InstaStory() whatsapp = WhatsAppStory()

# insta.share() whatsapp.share() """

# ------------------------------------------------------------------------------------
# Task 2: Method Overriding - Payment and UPI

# """ class Payment: def pay(self, amount): print('Paying', amount)

# class UPI(Payment): def pay(self, amount): print('Paying', amount, 'via UPI')

# payment = Payment() upi = UPI()

# payment.pay(1000) upi.pay(500) """

# ------------------------------------------------------------------------------------
# Task 3: Simulate Method Overloading - ZomatoOrder

# """ class ZomatoOrder: def add_item(self, item, quantity=1): print('Item:', item) print('Quantity:', quantity)

# order = ZomatoOrder()

# order.add_item('Pizza')

# order.add_item('Burger', 3) """

# ------------------------------------------------------------------------------------
# Task 4: Fix the Movie Class - Method Overriding

# """ class Content: def display(self, title): print('Title:', title)

# class Movie(Content): def display(self, title, year): print('Title:', title) print('Year:', year)

# movie = Movie()

# movie.display('3 Idiots', 2009) """

# ------------------------------------------------------------------------------------
# Task 5: Method Overriding - Notification Example

# """ class Notification: def send(self): print('Sending a notification')

# class EmailNotification(Notification): def send(self): print('Sending an email notification')

# class SMSNotification(Notification): def send(self): print('Sending an SMS notification')

# notification = Notification() email = EmailNotification() sms = SMSNotification()

# notification.send() email.send() sms.send()

# Explanation:
# Method overriding allows child classes to provide their own
# implementation of a method inherited from the parent class.

# """

# ------------------------------------------------------------------------------------