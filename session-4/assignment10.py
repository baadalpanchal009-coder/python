# SESSION 4 - Forgot Password + Session Management
# Topics: Django Sessions, Reset Password with OTP,
# Session Expiry, Middleware Basics
# ------------------------------------------------------------------------------------


# Task 1: Create Forgot Password Form

# File: foodiespot/forms.py

from django import forms


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label="Enter your registered email",
        required=True
    )


class VerifyOTPForm(forms.Form):
    otp = forms.CharField(
        max_length=6,
        min_length=6,
        label="Enter 6-digit OTP"
    )


# ------------------------------------------------------------------------------------


# Task 2: Generate OTP, Store It in Session and Send Email

# File: foodiespot/views.py

import secrets
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import ForgotPasswordForm, VerifyOTPForm


def forgot_password_view(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']

            user_exists = User.objects.filter(email=email).exists()

            if user_exists:
                otp = str(secrets.randbelow(900000) + 100000)

                request.session['otp'] = otp
                request.session['otp_email'] = email
                request.session.set_expiry(300)

                send_mail(
                    subject='Password Reset OTP',
                    message=f'Your password reset OTP is {otp}. '
                            'It expires in 5 minutes.',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email],
                    fail_silently=False,
                )

            messages.info(
                request,
                'If the email is registered, an OTP will be sent.'
            )
            return redirect('verify_otp')

    else:
        form = ForgotPasswordForm()

    return render(
        request,
        'forgot_password.html',
        {'form': form}
    )


# ------------------------------------------------------------------------------------


# Task 3: Verify OTP Entered by User

# File: foodiespot/views.py

def verify_otp_view(request):
    if 'otp' not in request.session:
        messages.error(
            request,
            'OTP is missing or expired. Please request a new OTP.'
        )
        return redirect('forgot_password')

    if request.method == 'POST':
        form = VerifyOTPForm(request.POST)

        if form.is_valid():
            entered_otp = form.cleaned_data['otp']
            saved_otp = request.session.get('otp')

            if saved_otp and secrets.compare_digest(
                entered_otp,
                saved_otp
            ):
                request.session['otp_verified'] = True
                messages.success(
                    request,
                    'OTP verified successfully!'
                )
                return redirect('otp_success')

            messages.error(
                request,
                'Invalid OTP. Please try again.'
            )

    else:
        form = VerifyOTPForm()

    return render(
        request,
        'verify_otp.html',
        {'form': form}
    )


# ------------------------------------------------------------------------------------


# Task 4: Set OTP Session Expiry to 5 Minutes

# After storing the OTP in the session, use:

"""
request.session['otp'] = otp
request.session['otp_email'] = email
request.session.set_expiry(300)
"""

# 300 seconds = 5 minutes.
# Django removes the OTP session data when the session expires.
# ------------------------------------------------------------------------------------


# Task 5: Create Custom Middleware to Protect OTP Verification

# File: foodiespot/middleware.py

from django.shortcuts import redirect


class BlockExpiredOTPAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/verify-otp/':
            if 'otp' not in request.session:
                return redirect('forgot_password')

        return self.get_response(request)


# Add middleware in foodiehub_project/settings.py
# after SessionMiddleware:

"""
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'foodiespot.middleware.BlockExpiredOTPAccessMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
"""

# ------------------------------------------------------------------------------------


# Create Forgot Password Template

# File: templates/forgot_password.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Forgot Password</title>
</head>
<body>
    <h1>Forgot Password</h1>

    {% for message in messages %}
        <p>{{ message }}</p>
    {% endfor %}

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Send OTP</button>
    </form>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Create OTP Verification Template

# File: templates/verify_otp.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Verify OTP</title>
</head>
<body>
    <h1>Verify Your OTP</h1>

    {% for message in messages %}
        <p>{{ message }}</p>
    {% endfor %}

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Verify OTP</button>
    </form>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Create OTP Success View

# File: foodiespot/views.py

def otp_success_view(request):
    if not request.session.get('otp_verified'):
        return redirect('forgot_password')

    return render(request, 'otp_success.html')


# File: templates/otp_success.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>OTP Verified</title>
</head>
<body>
    <h1>OTP Verified Successfully!</h1>
    <p>You can now continue with the next password reset step.</p>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Configure URLs

# File: foodiehub_project/urls.py

"""
from django.contrib import admin
from django.urls import path
from foodiespot.views import (
    forgot_password_view,
    verify_otp_view,
    otp_success_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'forgot-password/',
        forgot_password_view,
        name='forgot_password'
    ),
    path(
        'verify-otp/',
        verify_otp_view,
        name='verify_otp'
    ),
    path(
        'otp-success/',
        otp_success_view,
        name='otp_success'
    ),
]
"""

# ------------------------------------------------------------------------------------


# Configure Email Settings in settings.py

"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_16_digit_app_password'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
"""

# For local testing without sending real emails, you can use:
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# This prints email content to the terminal.

# ------------------------------------------------------------------------------------


# Run the Django Development Server

# python manage.py runserver

# Open:
# http://127.0.0.1:8000/forgot-password/

# ------------------------------------------------------------------------------------


# Important Concepts

# Django Session:
# Stores data associated with a visitor between requests.

# secrets.randbelow():
# Generates a cryptographically secure random number.

# request.session['otp']:
# Stores the OTP in the session.

# set_expiry(300):
# Sets session expiry to 5 minutes.

# send_mail():
# Sends the OTP to the user's email address.

# Middleware:
# Processes requests before they reach the view.

# OTP verification:
# Compares the entered OTP with the session OTP.

# ------------------------------------------------------------------------------------