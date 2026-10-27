# SESSION 4 - Django Models & Database Connectivity
# Topics: Creating Models, Model Fields, SQLite vs MySQL,
# Migrations, makemigrations, migrate, ORM Basics
# ------------------------------------------------------------------------------------


# Task 1: Create Django App and Restaurant Model

# Terminal command:
# python manage.py startapp foodiespot

# Add 'foodiespot' to INSTALLED_APPS in settings.py

# File: foodiespot/models.py

from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    rating = models.FloatField()

    def __str__(self):
        return self.name


# ------------------------------------------------------------------------------------


# Task 2: Create Cuisine Model and ForeignKey Relationship

# File: foodiespot/models.py

from django.db import models


class Cuisine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    rating = models.FloatField()
    cuisine = models.ForeignKey(
        Cuisine,
        on_delete=models.CASCADE,
        related_name='restaurants'
    )

    def __str__(self):
        return self.name


# ------------------------------------------------------------------------------------


# Task 3: Create Database Tables Using Migrations

# Run these commands in the terminal:

# python manage.py makemigrations foodiespot
# python manage.py migrate

# Verify database records using Django shell:

# python manage.py shell

# from foodiespot.models import Restaurant, Cuisine
# print(Restaurant.objects.all())
# print(Cuisine.objects.all())

# SQLite database file: db.sqlite3
# You can inspect it using DB Browser for SQLite.

# ------------------------------------------------------------------------------------


# Task 4: Connect Django to MySQL Using PyMySQL

# Install PyMySQL:
# pip install pymysql

# File: foodiehub_project/__init__.py

"""
import pymysql

pymysql.install_as_MySQLdb()
"""

# Create a MySQL database before configuring Django:
# CREATE DATABASE foodiehub_db;

# File: foodiehub_project/settings.py

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'foodiehub_db',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
"""

# Replace 'your_mysql_password' with your actual MySQL password.
# Make sure the MySQL server is running.
# After changing the database settings, run:
# python manage.py migrate

# ------------------------------------------------------------------------------------


# Task 5: Add Restaurant and Cuisine Objects Using Django ORM

# Run:
# python manage.py shell

# Enter the following code:

from foodiespot.models import Restaurant, Cuisine

# Create two cuisines
indian = Cuisine.objects.create(
    name="Indian",
    description="Traditional Indian food"
)

italian = Cuisine.objects.create(
    name="Italian",
    description="Italian food and pasta"
)

# Create three restaurants
Restaurant.objects.create(
    name="Spice Garden",
    location="Vadodara",
    rating=4.5,
    cuisine=indian
)

Restaurant.objects.create(
    name="Pasta House",
    location="Ahmedabad",
    rating=4.2,
    cuisine=italian
)

Restaurant.objects.create(
    name="Food Corner",
    location="Surat",
    rating=3.8,
    cuisine=indian
)

# Find restaurants with a rating above 4.0
top_restaurants = Restaurant.objects.filter(rating__gt=4.0)

# Print restaurant names
for restaurant in top_restaurants:
    print(restaurant.name)


# Expected Output:
# Spice Garden
# Pasta House

# ------------------------------------------------------------------------------------


# Important Concepts

# Model:
# Defines the structure of database tables.

# CharField:
# Stores short text.

# TextField:
# Stores longer text.

# FloatField:
# Stores decimal numbers.

# ForeignKey:
# Creates a relationship between two models.

# makemigrations:
# Creates migration files based on model changes.

# migrate:
# Applies migrations to the database.

# ORM:
# Allows database operations using Python instead of writing SQL.

# SQLite:
# A lightweight database used by default in Django projects.

# MySQL:
# A relational database suitable for many web applications.

# ------------------------------------------------------------------------------------