python
# SESSION 4 - Apps, Settings & URL Routing
# Topics: Creating Django App, Project vs App, settings.py,
# urls.py, wsgi.py, Mapping URL to View, HttpResponse Basics
# ------------------------------------------------------------------------------------


# Task 1: Create Django App Named playlists

"""
python manage.py startapp playlists
"""

# Standard files generated inside playlists app:
# __init__.py, admin.py, apps.py, models.py, tests.py, views.py
# ------------------------------------------------------------------------------------


# Task 2: Add playlists to INSTALLED_APPS

"""
Open foodiehub_project/settings.py and add 'playlists'
inside the INSTALLED_APPS list.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'playlists',
]
"""
# ------------------------------------------------------------------------------------


# Task 3: Create First View Using HttpResponse

# File: playlists/views.py

from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to My Spotify Playlists!")


# ------------------------------------------------------------------------------------


# Task 4: Configure URL Routing

# File: foodiehub_project/urls.py

from django.contrib import admin
from django.urls import path
from playlists.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', home),
]

# Open in browser:
# http://localhost:8000/music/
# Expected Output: Welcome to My Spotify Playlists!
# ------------------------------------------------------------------------------------


# Task 5: Update Welcome Message with Your Name

# File: playlists/views.py

from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to My Spotify Playlists! My name is Your Name.")

# Replace Your Name with your actual name.
# Visit http://localhost:8000/music/ to verify the updated message.
# Django development server automatically reloads most code changes.
# ------------------------------------------------------------------------------------


# Important Concepts

# Project:
# The complete website configuration and collection of apps.

# App:
# A component of a Django project that handles a specific feature.

# settings.py:
# Contains project configuration and INSTALLED_APPS.

# urls.py:
# Maps URL paths to views.

# views.py:
# Contains functions or classes that handle web requests.

# HttpResponse:
# Sends a response, such as text or HTML, back to the browser.

# ------------------------------------------------------------------------------------


# Trainer Activity: Create accounts App

"""
python manage.py startapp accounts
"""

# Add 'accounts' to INSTALLED_APPS if you want to register it.
# ------------------------------------------------------------------------------------