# SESSION 4 - Email Sending in Django
# Topics: SMTP Setup, Django Email Functions,
# HTML Email Templates
# ------------------------------------------------------------------------------------


# Task 1: Configure Gmail SMTP Settings

# File: foodiehub_project/settings.py

"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_16_digit_app_password'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
"""

# Replace your_email@gmail.com with your Gmail address.
# Use a Google App Password instead of your regular Gmail password.
# Keep credentials private and do not upload them to GitHub.


# Send a Test Email

# File: foodiespot/views.py

from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


def send_test_email(request):
    send_mail(
        subject='Django Test Email',
        message='Hello! This is a test email sent using Django.',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['your_test_email@gmail.com'],
        fail_silently=False,
    )

    return HttpResponse('Test email sent successfully!')


# ------------------------------------------------------------------------------------


# Task 2: Send Password Reset Email

# File: foodiespot/views.py

from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse


def send_password_reset_email(request, user_email):
    reset_path = reverse('password_reset')
    reset_link = request.build_absolute_uri(reset_path)

    subject = 'Reset Your Password - FoodieHub'

    message = (
        'Hello,\n\n'
        'We received a request to reset your password.\n'
        f'Please visit this link to continue: {reset_link}\n\n'
        'If you did not request a password reset, please ignore this email.'
    )

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user_email],
        fail_silently=False,
    )

    return HttpResponse('Password reset email sent!')

# Important: This example sends a link to the password reset page.
# A production app must generate a secure, user-specific, time-limited
# reset token and must not expose password reset functionality through
# an unrestricted URL parameter.


# ------------------------------------------------------------------------------------


# Task 3: Create HTML Order Confirmation Email

# File: templates/order_confirmation.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Order Confirmation</title>
</head>
<body>
    <h1>Thank you for your order, {{ customer_name }}!</h1>

    <p>Your food order has been confirmed.</p>

    <h3>Order Details</h3>
    <p>Order ID: {{ order_id }}</p>
    <p>Restaurant: {{ restaurant_name }}</p>
    <p>Food Item: {{ food_item }}</p>
    <p>Total Amount: ₹{{ total_amount }}</p>

    <p>Your delicious food will be delivered soon!</p>
    <p>Thank you for choosing FoodieHub.</p>
</body>
</html>
"""


# Send HTML Email Using EmailMultiAlternatives

# File: foodiespot/views.py

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.http import HttpResponse


def send_order_confirmation(request):
    context = {
        'customer_name': 'Rahul',
        'order_id': 'FH1001',
        'restaurant_name': 'Spice Garden',
        'food_item': 'Paneer Pizza',
        'total_amount': '299.00',
    }

    subject = 'Your FoodieHub Order Is Confirmed!'

    text_content = (
        f"Hello {context['customer_name']}, "
        f"your order {context['order_id']} has been confirmed."
    )

    html_content = render_to_string(
        'order_confirmation.html',
        context
    )

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=['your_test_email@gmail.com'],
    )

    email.attach_alternative(html_content, 'text/html')
    email.send(fail_silently=False)

    return HttpResponse('Order confirmation email sent!')


# ------------------------------------------------------------------------------------


# Task 4: Use Dynamic Customer and Order Details

# The order_confirmation.html template already uses dynamic variables:
#
# {{ customer_name }}
# {{ order_id }}
# {{ restaurant_name }}
# {{ food_item }}
# {{ total_amount }}
#
# Pass actual customer and order values in the context dictionary
# instead of the sample values shown above.
#
# Replace 'your_test_email@gmail.com' with your own test email address.


# ------------------------------------------------------------------------------------


# Task 5: Send Welcome Email for IPL Fantasy League

# File: templates/ipl_welcome.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to IPL Fantasy League</title>
</head>
<body>
    <h1>Welcome to IPL Fantasy League, {{ username }}!</h1>

    <p>Your fantasy cricket journey starts now!</p>

    <p>Create your dream team, choose your favorite players,
    earn points, and compete with friends throughout the season.</p>

    <h3>Pick Your Players. Build Your Team. Own the Game!</h3>

    <p>Good luck, and may your team hit plenty of sixes!</p>

    <p>Regards,<br>IPL Fantasy League Team</p>
</body>
</html>
"""


# File: foodiespot/views.py

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.http import HttpResponse


def send_ipl_welcome_email(request):
    username = 'CricketFan'

    context = {
        'username': username,
    }

    subject = '🏏 Welcome to IPL Fantasy League - Your Dream Team Awaits!'

    text_content = (
        f'Welcome to IPL Fantasy League, {username}! '
        'Build your dream team, pick your favorite players, '
        'and compete with friends.'
    )

    html_content = render_to_string(
        'ipl_welcome.html',
        context
    )

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=['your_test_email@gmail.com'],
    )

    email.attach_alternative(html_content, 'text/html')
    email.send(fail_silently=False)

    return HttpResponse('IPL Fantasy welcome email sent!')


# ------------------------------------------------------------------------------------


# Add URL Patterns in foodiehub_project/urls.py

"""
from django.contrib import admin
from django.urls import path
from foodiespot.views import (
    send_test_email,
    send_order_confirmation,
    send_ipl_welcome_email,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send-test-email/', send_test_email),
    path('send-order-email/', send_order_confirmation),
    path('send-ipl-email/', send_ipl_welcome_email),
]
"""


# ------------------------------------------------------------------------------------


# Important Concepts

# SMTP:
# Protocol used to send emails through an email server.

# send_mail():
# Sends a basic text email.

# EmailMultiAlternatives:
# Sends an email containing plain-text and HTML versions.

# render_to_string():
# Renders a Django template into a string.

# EMAIL_HOST:
# Specifies the SMTP server.

# EMAIL_USE_TLS:
# Enables encrypted email transmission.

# App Password:
# A separate Google credential used for supported third-party apps.

# ------------------------------------------------------------------------------------


# Run the Django Development Server

# python manage.py runserver

# Test URLs:
# http://127.0.0.1:8000/send-test-email/
# http://127.0.0.1:8000/send-order-email/
# http://127.0.0.1:8000/send-ipl-email/

# Replace all sample email addresses with your test email address.
# Keep SMTP credentials private.

# ------------------------------------------------------------------------------------