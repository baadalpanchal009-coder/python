python
# SESSION 4 - Django Forms Basics
# Topics: Django Form Class, GET vs POST, CSRF Token,
# Handling Form Submission
# ------------------------------------------------------------------------------------


# Task 1: Create AddRestaurantForm Using GET Method

# File: foodiespot/forms.py

from django import forms


class AddRestaurantForm(forms.Form):
    name = forms.CharField(max_length=100, label="Restaurant Name")
    cuisine = forms.CharField(max_length=100, label="Cuisine Type")
    contact_email = forms.EmailField(label="Contact Email")


# File: foodiespot/views.py

from django.shortcuts import render
from .forms import AddRestaurantForm


def add_restaurant(request):
    form = AddRestaurantForm()
    return render(request, 'add_restaurant.html', {'form': form})


# ------------------------------------------------------------------------------------


# Task 2: Handle Form Submission Using POST Method

# File: foodiespot/views.py

from django.shortcuts import render
from .forms import AddRestaurantForm


def add_restaurant(request):
    if request.method == 'POST':
        form = AddRestaurantForm(request.POST)

        if form.is_valid():
            return render(
                request,
                'restaurant_success.html',
                {'data': form.cleaned_data}
            )
    else:
        form = AddRestaurantForm()

    return render(request, 'add_restaurant.html', {'form': form})


# File: templates/restaurant_success.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Restaurant Submitted</title>
</head>
<body>
    <h1>Restaurant Details Submitted Successfully!</h1>
    <p>Name: {{ data.name }}</p>
    <p>Cuisine: {{ data.cuisine }}</p>
    <p>Email: {{ data.contact_email }}</p>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Task 3: Add Form Validation and Display Errors

# File: foodiespot/forms.py

from django import forms


class AddRestaurantForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        min_length=3,
        label="Restaurant Name"
    )
    cuisine = forms.CharField(max_length=100, label="Cuisine Type")
    contact_email = forms.EmailField(label="Contact Email")


# File: templates/add_restaurant.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Add Restaurant</title>
</head>
<body>
    <h1>Add Restaurant</h1>

    <form method="post">
        {% csrf_token %}

        {{ form.errors }}

        <div>
            {{ form.name.label_tag }}
            {{ form.name }}
            {{ form.name.errors }}
        </div>

        <div>
            {{ form.cuisine.label_tag }}
            {{ form.cuisine }}
            {{ form.cuisine.errors }}
        </div>

        <div>
            {{ form.contact_email.label_tag }}
            {{ form.contact_email }}
            {{ form.contact_email.errors }}
        </div>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Task 4: Implement CSRF Protection

# Add {% csrf_token %} inside every POST form.

"""
<form method="post">
    {% csrf_token %}
    {{ form.errors }}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
"""

# Django's CSRF middleware checks POST requests for a valid token.
# Submitting without a valid token should return HTTP 403
# when CSRF protection is enabled.
# ------------------------------------------------------------------------------------


# Run the Django Development Server

# python manage.py runserver

# Open in browser:
# http://127.0.0.1:8000/add-restaurant/

# ------------------------------------------------------------------------------------


# Important Concepts

# forms.Form: Creates a Django form.
# GET: Usually displays a page or blank form.
# POST: Sends submitted data to the server.
# is_valid(): Checks submitted data.
# cleaned_data: Contains validated form data.
# EmailField: Validates email format.
# min_length: Requires a minimum number of characters.
# csrf_token: Protects against cross-site request forgery.
# form.errors: Displays validation errors.

# ------------------------------------------------------------------------------------