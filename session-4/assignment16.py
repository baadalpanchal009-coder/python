# SESSION 4 - Django Integrations
# Topics: Social Login (Google), Email APIs (Mailgun),
# SMS APIs (Twilio), OTP Storage and Verification
# ------------------------------------------------------------------------------------


# Task 1: Integrate Google Login Using social-auth-app-django

# Install package:
# pip install social-auth-app-django

# File: foodiehub_project/settings.py

"""
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
]

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'YOUR_GOOGLE_CLIENT_ID'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'YOUR_GOOGLE_CLIENT_SECRET'

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email', 'profile']
"""

# Create OAuth credentials in Google Cloud Console.
# Add your local callback URL to the authorized redirect URIs:
# http://127.0.0.1:8000/auth/complete/google-oauth2/
# Keep your client secret private.


# File: foodiehub_project/urls.py

"""
from django.contrib import admin
from django.urls import path, include
from foodiespot.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('social_django.urls', namespace='social')),
    path('', home_view, name='home'),
]
"""


# File: foodiespot/views.py

from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')


# File: templates/home.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>FoodieHub Home</title>
</head>
<body>
    {% if user.is_authenticated %}
        <h1>Welcome, {{ user.first_name|default:user.username }}!</h1>
        <p>Email: {{ user.email }}</p>

        <form method="post" action="{% url 'logout' %}">
            {% csrf_token %}
            <button type="submit">Logout</button>
        </form>
    {% else %}
        <h1>Welcome to FoodieHub</h1>
        <a href="{% url 'social:begin' 'google-oauth2' %}">
            Sign in with Google
        </a>
    {% endif %}
</body>
</html>
"""

# Add a logout URL if your project does not already have one:
#
# from django.contrib.auth.views import LogoutView
# path('logout/', LogoutView.as_view(), name='logout')

# Run migrations:
# python manage.py migrate

# ------------------------------------------------------------------------------------


# Task 2: Send Welcome Email Using Mailgun API

# Install packages:
# pip install requests

# Configure credentials using environment variables in production.
# File: foodiehub_project/settings.py

"""
MAILGUN_API_KEY = 'YOUR_MAILGUN_API_KEY'
MAILGUN_DOMAIN = 'YOUR_VERIFIED_MAILGUN_DOMAIN'
MAILGUN_FROM_EMAIL = 'FoodieHub <postmaster@YOUR_VERIFIED_MAILGUN_DOMAIN>'
"""

# File: foodiespot/views.py

import requests
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST


def send_welcome_email(user):
    response = requests.post(
        f'https://api.mailgun.net/v3/{settings.MAILGUN_DOMAIN}/messages',
        auth=('api', settings.MAILGUN_API_KEY),
        data={
            'from': settings.MAILGUN_FROM_EMAIL,
            'to': [user.email],
            'subject': 'Welcome to FoodieHub!',
            'text': (
                f"Hello {user.username}, welcome to FoodieHub! "
                "We are happy to have you with us."
            ),
        },
        timeout=15,
    )

    response.raise_for_status()
    return response


@require_POST
def register_user(request):
    username = request.POST.get('username', '').strip()
    email = request.POST.get('email', '').strip()
    password = request.POST.get('password', '')

    if not username or not email or not password:
        return HttpResponse(
            'Username, email and password are required.',
            status=400
        )

    if User.objects.filter(username=username).exists():
        return HttpResponse('Username already exists.', status=400)

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
    )

    try:
        send_welcome_email(user)
    except requests.RequestException:
        # The account is created, but email delivery may have failed.
        return HttpResponse(
            'Account created, but welcome email could not be sent.',
            status=502
        )

    return HttpResponse('Registration successful. Welcome email sent!')


# ------------------------------------------------------------------------------------


# Task 3: Send a 6-Digit OTP Using Twilio SMS API

# Install package:
# pip install twilio

# Configure Twilio credentials in settings.py:
"""
TWILIO_ACCOUNT_SID = 'YOUR_TWILIO_ACCOUNT_SID'
TWILIO_AUTH_TOKEN = 'YOUR_TWILIO_AUTH_TOKEN'
TWILIO_PHONE_NUMBER = 'YOUR_TWILIO_PHONE_NUMBER'
"""

# File: foodiespot/views.py

import secrets
from twilio.rest import Client
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def send_sms_otp(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile', '').strip()

        if not mobile.startswith('+') or not mobile[1:].isdigit():
            messages.error(
                request,
                'Enter a valid mobile number with country code.'
            )
            return render(request, 'send_otp.html')

        otp = str(secrets.randbelow(900000) + 100000)

        try:
            client = Client(
                settings.TWILIO_ACCOUNT_SID,
                settings.TWILIO_AUTH_TOKEN,
            )

            client.messages.create(
                body=f'Your FoodieHub OTP is {otp}. It expires in 5 minutes.',
                from_=settings.TWILIO_PHONE_NUMBER,
                to=mobile,
            )

            # Store OTP securely in the session for this demo.
            request.session['sms_otp'] = otp
            request.session['sms_mobile'] = mobile
            request.session['sms_otp_verified'] = False
            request.session.set_expiry(300)

            messages.success(request, 'OTP sent successfully!')

        except Exception:
            messages.error(request, 'Unable to send OTP. Please try again.')

    return render(request, 'send_otp.html')


# File: templates/send_otp.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Send SMS OTP</title>
</head>
<body>
    <h1>Verify Mobile Number</h1>

    {% for message in messages %}
        <p>{{ message }}</p>
    {% endfor %}

    <form method="post">
        {% csrf_token %}
        <label>Mobile Number (with country code):</label>
        <input type="text" name="mobile" placeholder="+911234567890" required>
        <button type="submit">Send OTP</button>
    </form>

    <a href="{% url 'verify_sms_otp' %}">Verify OTP</a>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Task 4: Create a Model to Store and Verify SMS OTP Codes

# File: foodiespot/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class SMSOTP(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sms_otps'
    )
    mobile = models.CharField(max_length=20)
    otp_hash = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_verified = models.BooleanField(default=False)
    attempts = models.PositiveSmallIntegerField(default=0)

    def is_expired(self):
        return timezone.now() >= self.expires_at

    def __str__(self):
        return f"SMS OTP for {self.user.username}"


# ------------------------------------------------------------------------------------


# Hash and Store OTP Securely

# File: foodiespot/otp_utils.py

import hashlib
import hmac
from django.conf import settings


def hash_otp(otp):
    return hmac.new(
        settings.SECRET_KEY.encode(),
        otp.encode(),
        hashlib.sha256
    ).hexdigest()


def verify_otp_hash(entered_otp, saved_hash):
    return hmac.compare_digest(
        hash_otp(entered_otp),
        saved_hash
    )


# ------------------------------------------------------------------------------------


# Create and Send a Database-Backed OTP

# File: foodiespot/views.py

from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import SMSOTP
from .otp_utils import hash_otp


@login_required
@require_http_methods(["GET", "POST"])
def create_sms_otp(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile', '').strip()

        if not mobile.startswith('+') or not mobile[1:].isdigit():
            messages.error(request, 'Enter a valid mobile number.')
            return render(request, 'send_otp.html')

        otp = str(secrets.randbelow(900000) + 100000)

        SMSOTP.objects.filter(
            user=request.user,
            is_verified=False
        ).delete()

        otp_record = SMSOTP.objects.create(
            user=request.user,
            mobile=mobile,
            otp_hash=hash_otp(otp),
            expires_at=timezone.now() + timedelta(minutes=5),
        )

        try:
            client = Client(
                settings.TWILIO_ACCOUNT_SID,
                settings.TWILIO_AUTH_TOKEN,
            )

            client.messages.create(
                body=f'Your verification OTP is {otp}. It expires in 5 minutes.',
                from_=settings.TWILIO_PHONE_NUMBER,
                to=mobile,
            )

            messages.success(request, 'OTP sent successfully!')

        except Exception:
            otp_record.delete()
            messages.error(request, 'Unable to send OTP.')

    return render(request, 'send_otp.html')


# ------------------------------------------------------------------------------------


# Verify OTP Stored in the Database

# File: foodiespot/views.py

from django.shortcuts import redirect
from .otp_utils import verify_otp_hash


@login_required
@require_http_methods(["GET", "POST"])
def verify_sms_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp', '').strip()

        otp_record = SMSOTP.objects.filter(
            user=request.user,
            is_verified=False
        ).order_by('-created_at').first()

        if not otp_record or otp_record.is_expired():
            messages.error(request, 'OTP expired. Please request a new one.')

        elif otp_record.attempts >= 5:
            messages.error(request, 'Too many attempts. Request a new OTP.')

        else:
            otp_record.attempts += 1
            otp_record.save(update_fields=['attempts'])

            if verify_otp_hash(entered_otp, otp_record.otp_hash):
                otp_record.is_verified = True
                otp_record.save(update_fields=['is_verified'])
                messages.success(request, 'Mobile number verified!')
            else:
                messages.error(request, 'Invalid OTP. Please try again.')

    return render(request, 'verify_sms_otp.html')


# File: templates/verify_sms_otp.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Verify OTP</title>
</head>
<body>
    <h1>Enter SMS OTP</h1>

    {% for message in messages %}
        <p>{{ message }}</p>
    {% endfor %}

    <form method="post">
        {% csrf_token %}
        <input
            type="text"
            name="otp"
            maxlength="6"
            minlength="6"
            pattern="[0-9]{6}"
            placeholder="Enter 6-digit OTP"
            required
        >
        <button type="submit">Verify OTP</button>
    </form>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Configure URLs

# File: foodiehub_project/urls.py

"""
from django.contrib import admin
from django.urls import path
from foodiespot import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('register/', views.register_user, name='register_user'),
    path('send-sms-otp/', views.send_sms_otp, name='send_sms_otp'),
    path('create-sms-otp/', views.create_sms_otp, name='create_sms_otp'),
    path('verify-sms-otp/', views.verify_sms_otp, name='verify_sms_otp'),
]
"""


# Run database migrations:
# python manage.py makemigrations foodiespot
# python manage.py migrate
# python manage.py runserver

# ------------------------------------------------------------------------------------


# Important Concepts

# Google OAuth:
# Allows users to sign in with their Google account.

# Mailgun API:
# Sends transactional emails using an HTTP API.

# Twilio SMS API:
# Sends SMS messages using a verified Twilio account and phone number.

# secrets.randbelow():
# Generates a secure random number.

# SMSOTP model:
# Stores OTP hashes, expiration times, verification status and attempts.

# hmac.compare_digest():
# Compares hashes safely.

# Session expiry:
# request.session.set_expiry(300) sets a five-minute session expiry.

# Security:
# Keep API credentials in environment variables.
# Use HTTPS in production.
# Add rate limiting to OTP sending and verification endpoints.
# Never log or store raw OTPs unnecessarily.

# ------------------------------------------------------------------------------------