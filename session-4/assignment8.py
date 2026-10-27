# SESSION 4 - User Authentication System
# Topics: User Model, Signup, Login, Logout, Password Hashing,
# Authentication Backend
# ------------------------------------------------------------------------------------


# Task 1: Create Django Project and Enable Authentication

# Terminal commands:
# django-admin startproject musiczone
# cd musiczone
# python manage.py migrate
# python manage.py createsuperuser
# python manage.py runserver

# Django provides a built-in User model and authentication system.
# Add these apps in settings.py if they are not already present:

"""
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
"""

# ------------------------------------------------------------------------------------


# Task 2: Create Signup Form with Secure Password Hashing

# File: accounts/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


# ------------------------------------------------------------------------------------


# Task 3: Create Signup, Login, Logout and Welcome Views

# File: accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignupForm


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('welcome')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('welcome')
    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form': form})


@login_required
def welcome_view(request):
    return render(request, 'welcome.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)

    return redirect('home')


def home_view(request):
    return render(request, 'home.html')


# ------------------------------------------------------------------------------------


# Task 4: Configure URLs

# File: musiczone/urls.py

from django.contrib import admin
from django.urls import path
from accounts.views import (
    signup_view,
    login_view,
    logout_view,
    welcome_view,
    home_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('welcome/', welcome_view, name='welcome'),
]


# ------------------------------------------------------------------------------------


# Task 5: Create Signup Template

# File: templates/signup.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
</head>
<body>
    <h1>Create Account</h1>

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Signup</button>
    </form>

    <p>Already registered?
        <a href="{% url 'login' %}">Login</a>
    </p>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Task 6: Create Login Template

# File: templates/login.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Login</button>
    </form>

    <p>New user?
        <a href="{% url 'signup' %}">Signup</a>
    </p>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Task 7: Display Logged-in Username on Welcome Page

# File: templates/welcome.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
    <h1>Welcome, {{ user.username }}!</h1>
    <p>You are logged in successfully.</p>

    <form method="post" action="{% url 'logout' %}">
        {% csrf_token %}
        <button type="submit">Logout</button>
    </form>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Task 8: Create Navbar with Login, Signup and Logout

# File: templates/base.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>MusicZone</title>
</head>
<body>

    <nav>
        <a href="{% url 'home' %}">Home</a>

        {% if user.is_authenticated %}
            <span>Welcome, {{ user.username }}</span>

            <form method="post"
                  action="{% url 'logout' %}"
                  style="display:inline;">
                {% csrf_token %}
                <button type="submit">Logout</button>
            </form>
        {% else %}
            <a href="{% url 'login' %}">Login</a>
            <a href="{% url 'signup' %}">Signup</a>
        {% endif %}
    </nav>

    <main>
        {% block content %}
        {% endblock %}
    </main>

</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Task 9: Create Homepage Template

# File: templates/home.html

"""
{% extends 'base.html' %}

{% block content %}
    <h1>Welcome to MusicZone!</h1>
    <p>Discover your favorite music.</p>
{% endblock %}
"""

# ------------------------------------------------------------------------------------


# Task 10: Configure Templates in settings.py

"""
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
"""

# Create the accounts app before using the views:
# python manage.py startapp accounts

# Add 'accounts' to INSTALLED_APPS in settings.py.

# ------------------------------------------------------------------------------------


# Important Concepts

# User model:
# Stores usernames, email addresses and hashed passwords.

# UserCreationForm:
# Provides signup fields and password validation.

# AuthenticationForm:
# Validates login credentials.

# login():
# Authenticates a user session.

# logout():
# Ends the current user session.

# @login_required:
# Restricts a view to authenticated users.

# user.is_authenticated:
# Checks whether a user is logged in.

# Password hashing:
# Django stores password hashes rather than plain-text passwords.

# CSRF token:
# Protects POST forms against cross-site request forgery.

# ------------------------------------------------------------------------------------


# Run the Application

# python manage.py migrate
# python manage.py runserver

# Signup: http://127.0.0.1:8000/signup/
# Login:  http://127.0.0.1:8000/login/
# Home:   http://127.0.0.1:8000/
# Welcome: http://127.0.0.1:8000/welcome/

# After logout, the username disappears from the navbar,
# and the Login and Signup links appear again.

# ------------------------------------------------------------------------------------