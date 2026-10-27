
# SESSION 4 - Introduction to Django & Setup
# Topics: What is Django, Django vs Flask, Django Features,
# MVT Architecture, Installing Django, Creating Project,
# Running Django Server
# ------------------------------------------------------------------------------------


# Task 1: Install Django and Verify Installation

"""
pip install django
django-admin --version
"""


# ------------------------------------------------------------------------------------


# Task 2: Create Django Project and Run Development Server

"""
django-admin startproject foodiehub_project
cd foodiehub_project
python manage.py runserver

Open in browser:
http://127.0.0.1:8000/
"""


# ------------------------------------------------------------------------------------


# Task 3: Explore Django Project Structure

"""
foodiehub_project/
    manage.py
    foodiehub_project/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py


File Descriptions:

manage.py:
Used to run commands and manage the Django project.

settings.py:
Contains project configuration, installed apps, database settings,
middleware, and other settings.

urls.py:
Defines URL patterns and routes requests to the appropriate views.

wsgi.py:
Provides an entry point for deploying Django applications
on WSGI-compatible servers.

asgi.py:
Provides an entry point for deploying Django applications
on ASGI-compatible servers and supports asynchronous features.
"""


# ------------------------------------------------------------------------------------


# Task 4: Comparison Between Django and Flask

"""
Django is a full-stack Python framework with built-in authentication,
database tools, and an admin panel.

Flask is a lightweight framework that provides flexibility and allows
developers to choose their own tools.

For an application like Zomato, Django is a good choice because it can
manage users, restaurants, orders, and databases efficiently.

Flask is suitable for smaller applications and simple APIs where
a lightweight and flexible structure is preferred.
"""


# ------------------------------------------------------------------------------------


# Trainer Activities: Create doctorfinder_project

"""
django-admin startproject doctorfinder_project

Explore the project structure and understand the purpose of
manage.py, settings.py, urls.py, wsgi.py, and asgi.py.
"""


# ------------------------------------------------------------------------------------


# Important Django Features

"""
1. Fast development
2. Built-in authentication
3. Database integration
4. Automatic admin panel
5. URL routing
6. Security features
7. Reusable applications
8. Scalability
"""


# ------------------------------------------------------------------------------------


# MVT Architecture

"""
MVT stands for Model, View, and Template.

Model:
Manages data and database operations.

View:
Handles application logic and processes requests.

Template:
Displays the user interface using HTML.
"""


# ------------------------------------------------------------------------------------
