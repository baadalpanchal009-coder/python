# SESSION 5 - Django Admin Customization
# Topics: Enabling Admin, Adding Models to Admin, Custom List Display,
# Search Fields, Filters
# ------------------------------------------------------------------------------------


# Task 1: Enable Django Admin and Create Superuser

# Run these commands in the terminal:

# python manage.py migrate
# python manage.py createsuperuser
# python manage.py runserver

# Open in browser:
# http://127.0.0.1:8000/admin/

# Enter your superuser username and password to log in.
# ------------------------------------------------------------------------------------


# Task 2: Create Restaurant Model

# File: foodiespot/models.py

from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    rating = models.FloatField()

    def __str__(self):
        return self.name


# Add 'foodiespot' to INSTALLED_APPS in settings.py.
# ------------------------------------------------------------------------------------


# Task 3: Register Restaurant Model and Customize List Display

# File: foodiespot/admin.py

from django.contrib import admin
from .models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'cuisine', 'rating')


# Run these commands after creating or changing the model:
# python manage.py makemigrations foodiespot
# python manage.py migrate

# ------------------------------------------------------------------------------------


# Task 4: Add Search Functionality

# File: foodiespot/admin.py

from django.contrib import admin
from .models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'cuisine', 'rating')
    search_fields = ('name', 'cuisine')


# The admin search box can now search by restaurant name or cuisine.
# ------------------------------------------------------------------------------------


# Task 5: Add Cuisine Filter

# File: foodiespot/admin.py

from django.contrib import admin
from .models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'cuisine', 'rating')
    search_fields = ('name', 'cuisine')
    list_filter = ('cuisine',)


# ------------------------------------------------------------------------------------


# Final Restaurant Model

# File: foodiespot/models.py

from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    rating = models.FloatField()

    def __str__(self):
        return self.name


# ------------------------------------------------------------------------------------


# Final Admin Configuration

# File: foodiespot/admin.py

from django.contrib import admin
from .models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'cuisine', 'rating')
    search_fields = ('name', 'cuisine')
    list_filter = ('cuisine',)


# ------------------------------------------------------------------------------------


# Important Concepts

# admin.site:
# Provides access to the Django admin interface.

# createsuperuser:
# Creates an administrator account.

# list_display:
# Specifies which fields appear in the admin list view.

# search_fields:
# Adds a search box for selected fields.

# list_filter:
# Adds sidebar filters to the admin list view.

# __str__():
# Returns a readable name for each Restaurant object.

# ------------------------------------------------------------------------------------
