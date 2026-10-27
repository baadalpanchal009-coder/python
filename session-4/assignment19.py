# SESSION 4 - GitHub Deployment & PythonAnywhere Hosting
# Topics: Push Django Project to GitHub, PythonAnywhere Deployment,
# Static & Media Files Configuration, Database Migration, Live Testing
# ------------------------------------------------------------------------------------


# Task 1: Create a Django Project Named MyPlaylistApp and Push It to GitHub

# Step 1: Install Django
# pip install django

# Step 2: Create a new Django project
# django-admin startproject MyPlaylistApp
# cd MyPlaylistApp

# Step 3: Create a Django app
# python manage.py startapp playlists

# Step 4: Add the app to settings.py

# File: MyPlaylistApp/settings.py

"""
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'playlists',
]

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
"""

# Step 5: Create a Playlist Model

# File: playlists/models.py

from django.db import models


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cover_image = models.ImageField(
        upload_to='playlist_covers/',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Step 6: Register the Model in Django Admin

# File: playlists/admin.py

from django.contrib import admin
from .models import Playlist


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)


# Step 7: Create Playlist Views

# File: playlists/views.py

from django.shortcuts import render, get_object_or_404
from .models import Playlist


def playlist_list(request):
    playlists = Playlist.objects.all().order_by('-created_at')

    return render(
        request,
        'playlists/playlist_list.html',
        {'playlists': playlists}
    )


def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)

    return render(
        request,
        'playlists/playlist_detail.html',
        {'playlist': playlist}
    )


# Step 8: Configure URLs

# File: MyPlaylistApp/urls.py

"""
from django.contrib import admin
from django.urls import path
from playlists.views import playlist_list, playlist_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', playlist_list, name='playlist_list'),
    path(
        'playlist/<int:playlist_id>/',
        playlist_detail,
        name='playlist_detail'
    ),
]
"""

# Step 9: Create Templates

# File: playlists/templates/playlists/playlist_list.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>My Playlist App</title>
</head>
<body>
    <h1>My Playlist App</h1>

    <a href="/admin/">Admin Panel</a>

    {% for playlist in playlists %}
        <div>
            <h2>
                <a href="{% url 'playlist_detail' playlist.id %}">
                    {{ playlist.name }}
                </a>
            </h2>

            <p>{{ playlist.description }}</p>

            {% if playlist.cover_image %}
                <img
                    src="{{ playlist.cover_image.url }}"
                    alt="{{ playlist.name }}"
                    width="200"
                >
            {% endif %}
        </div>
    {% empty %}
        <p>No playlists available yet.</p>
    {% endfor %}
</body>
</html>
"""

# File: playlists/templates/playlists/playlist_detail.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>{{ playlist.name }}</title>
</head>
<body>
    <h1>{{ playlist.name }}</h1>

    <p>{{ playlist.description }}</p>

    {% if playlist.cover_image %}
        <img
            src="{{ playlist.cover_image.url }}"
            alt="{{ playlist.name }}"
            width="300"
        >
    {% endif %}

    <p>Created: {{ playlist.created_at }}</p>

    <a href="{% url 'playlist_list' %}">Back to Playlists</a>
</body>
</html>
"""

# Step 10: Configure Static and Media Files Locally

# Add to MyPlaylistApp/settings.py

"""
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
"""

# Add media URL support to MyPlaylistApp/urls.py during development:

"""
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
"""

# Step 11: Install Pillow for ImageField
# pip install pillow

# Step 12: Create Database Tables
# python manage.py makemigrations
# python manage.py migrate

# Step 13: Create an Admin User
# python manage.py createsuperuser

# Step 14: Test Locally
# python manage.py runserver

# Open:
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/admin/

# Step 15: Create requirements.txt
# pip freeze > requirements.txt

# Step 16: Create .gitignore

"""
__pycache__/
*.py[cod]
.env
venv/
.venv/
db.sqlite3
staticfiles/
media/
"""

# Step 17: Initialize Git and Push to GitHub
# Create an empty repository named MyPlaylistApp on GitHub.
# Then run these commands from the project root:

# git init
# git add .
# git commit -m "Initial MyPlaylistApp Django project"
# git branch -M main
# git remote add origin https://github.com/YOUR_USERNAME/MyPlaylistApp.git
# git push -u origin main

# Replace YOUR_USERNAME with your actual GitHub username.

# ------------------------------------------------------------------------------------


# Task 2: Deploy MyPlaylistApp to PythonAnywhere

# Step 1: Sign in to PythonAnywhere.
# Step 2: Open the Consoles tab and start a Bash console.
# Step 3: Clone your GitHub repository.

# git clone https://github.com/YOUR_USERNAME/MyPlaylistApp.git
# cd MyPlaylistApp

# Step 4: Create and activate a virtual environment.

# python3 -m venv ~/.virtualenvs/myplaylistenv
# source ~/.virtualenvs/myplaylistenv/bin/activate

# Step 5: Install dependencies.

# pip install -r requirements.txt

# If Pillow or Django is missing:
# pip install django pillow

# Step 6: Open the Web tab.
# Step 7: Click Add a new web app.
# Step 8: Choose Manual Configuration and the Python version
# supported by your installed Django version.
# Step 9: Set the virtualenv path to:
# /home/YOUR_USERNAME/.virtualenvs/myplaylistenv

# Step 10: Open the WSGI configuration file from the Web tab
# and configure it to point to your project.

# Example WSGI configuration:

"""
import os
import sys

project_home = '/home/YOUR_USERNAME/MyPlaylistApp'

if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'MyPlaylistApp.settings'
)

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
"""

# Replace YOUR_USERNAME with your PythonAnywhere username.
# Ensure the path matches the actual folder containing manage.py.

# Step 11: Configure production settings.

# File: MyPlaylistApp/settings.py

"""
DEBUG = False

ALLOWED_HOSTS = [
    'YOUR_USERNAME.pythonanywhere.com',
]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
"""

# Configure secrets and credentials through environment variables
# or a secure configuration mechanism rather than committing them.

# ------------------------------------------------------------------------------------


# Task 3: Configure Static and Media Files on PythonAnywhere

# Step 1: Run collectstatic in the Bash console.

# source ~/.virtualenvs/myplaylistenv/bin/activate
# cd ~/MyPlaylistApp
# python manage.py collectstatic

# Step 2: Open the Web tab on PythonAnywhere.
# Step 3: Find the Static files section.
# Step 4: Add the following mappings:

# URL: /static/
# Directory: /home/YOUR_USERNAME/MyPlaylistApp/staticfiles

# URL: /media/
# Directory: /home/YOUR_USERNAME/MyPlaylistApp/media

# Replace YOUR_USERNAME with your PythonAnywhere username.

# Step 5: Ensure uploaded images are saved under MEDIA_ROOT.
# Step 6: Click Reload on the Web tab.

# Note:
# Static files include CSS, JavaScript, and other assets.
# Media files include user-uploaded playlist cover images.
# PythonAnywhere static mappings serve these files directly.

# ------------------------------------------------------------------------------------


# Task 4: Run Migrations and Add Playlists Through Admin

# In the PythonAnywhere Bash console:

# cd ~/MyPlaylistApp
# source ~/.virtualenvs/myplaylistenv/bin/activate

# Create migrations:
# python manage.py makemigrations playlists

# Apply migrations:
# python manage.py migrate

# Create an admin account:
# python manage.py createsuperuser

# Open your live admin page:
# https://YOUR_USERNAME.pythonanywhere.com/admin/

# Log in using your superuser credentials.
# Open Playlists and click Add Playlist.
# Enter a name and description, optionally upload a cover image,
# then click Save.

# Open the homepage to verify that the playlist is displayed.

# ------------------------------------------------------------------------------------


# Task 5: Test Live Routes and Document Results

# Route 1: Playlist List
# https://YOUR_USERNAME.pythonanywhere.com/

# Expected result:
# The homepage displays the playlist list.
# If no playlists exist, it displays "No playlists available yet."

# Route 2: Playlist Detail
# https://YOUR_USERNAME.pythonanywhere.com/playlist/1/

# Expected result:
# The detail page displays the playlist name and description.
# The playlist ID must exist in the database.

# Route 3: Django Admin
# https://YOUR_USERNAME.pythonanywhere.com/admin/

# Expected result:
# The login page opens and allows an authorized admin to manage playlists.

# Route 4: Uploaded Cover Image
# https://YOUR_USERNAME.pythonanywhere.com/media/playlist_covers/example.jpg

# Expected result:
# The image opens if it exists at the corresponding media path.

# ------------------------------------------------------------------------------------


# Common Errors and Solutions

# Error 1: DisallowedHost
# Solution:
# Add 'YOUR_USERNAME.pythonanywhere.com' to ALLOWED_HOSTS.

# Error 2: ModuleNotFoundError
# Solution:
# Install dependencies in the same virtual environment configured
# on the PythonAnywhere Web tab.

# Error 3: Static files not loading
# Solution:
# Run python manage.py collectstatic.
# Check the /static/ mapping on the Web tab and reload the app.

# Error 4: Uploaded images not loading
# Solution:
# Check MEDIA_ROOT, MEDIA_URL and the /media/ mapping.
# Confirm the image exists in the configured media directory.

# Error 5: Database tables missing
# Solution:
# Run python manage.py migrate in the correct project directory
# and virtual environment.

# Error 6: Application returns a 500 error
# Solution:
# Open the error log linked from the PythonAnywhere Web tab.
# Fix the reported exception and reload the application.

# ------------------------------------------------------------------------------------


# Important Concepts

# Git:
# Tracks project changes.

# GitHub:
# Hosts the source code repository.

# PythonAnywhere:
# Hosts the live Django application.

# requirements.txt:
# Lists Python package dependencies.

# WSGI:
# Connects the web server to the Django application.

# collectstatic:
# Collects static assets into STATIC_ROOT.

# MEDIA_ROOT:
# Directory for uploaded files.

# makemigrations:
# Generates migration files from model changes.

# migrate:
# Applies migrations to the configured database.

# Debugging:
# Use the PythonAnywhere error logs to investigate deployment issues.

# ------------------------------------------------------------------------------------