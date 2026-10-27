# SESSION 4 - Django Model Forms
# Topics: ModelForm Benefits, Automatic Form Generation,
# Saving Form Data to Model
# ------------------------------------------------------------------------------------


# Task 1: Create Restaurant Model and RestaurantForm

# File: foodiespot/models.py

from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    rating = models.FloatField()

    def __str__(self):
        return self.name


# File: foodiespot/forms.py

from django import forms
from .models import Restaurant


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'cuisine', 'rating']


# ------------------------------------------------------------------------------------


# Task 2: Create View to Display and Save Restaurant Form

# File: foodiespot/views.py

from django.shortcuts import render, redirect
from .forms import RestaurantForm


def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('add_restaurant')
    else:
        form = RestaurantForm()

    return render(
        request,
        'add_restaurant.html',
        {'form': form}
    )


# File: foodiehub_project/urls.py

from django.contrib import admin
from django.urls import path
from foodiespot.views import add_restaurant

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-restaurant/', add_restaurant, name='add_restaurant'),
]


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
        {{ form.as_p }}
        <button type="submit">Save Restaurant</button>
    </form>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Task 3: Add Placeholder and Rating Range

# File: foodiespot/forms.py

from django import forms
from .models import Restaurant


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'cuisine', 'rating']

        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Enter restaurant name'}
            ),
            'rating': forms.NumberInput(
                attrs={'min': 1, 'max': 5, 'step': 0.1}
            ),
        }


# ------------------------------------------------------------------------------------


# Task 4: Add Validation and Custom Error Messages

# File: foodiespot/forms.py

from django import forms
from .models import Restaurant


class RestaurantForm(forms.ModelForm):
    name = forms.CharField(
        min_length=3,
        error_messages={
            'min_length': 'Restaurant name must be at least 3 characters long.'
        }
    )

    rating = forms.FloatField(
        min_value=1,
        max_value=5,
        error_messages={
            'min_value': 'Rating must be at least 1.',
            'max_value': 'Rating cannot be greater than 5.',
            'invalid': 'Please enter a valid rating.'
        },
        widget=forms.NumberInput(
            attrs={'min': 1, 'max': 5, 'step': 0.1}
        )
    )

    class Meta:
        model = Restaurant
        fields = ['name', 'cuisine', 'rating']

        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Enter restaurant name'}
            )
        }


# ------------------------------------------------------------------------------------


# Display Validation Errors in Template

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

        {{ form.non_field_errors }}

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
            {{ form.rating.label_tag }}
            {{ form.rating }}
            {{ form.rating.errors }}
        </div>

        <button type="submit">Save Restaurant</button>
    </form>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Run Database Migrations

# python manage.py makemigrations foodiespot
# python manage.py migrate

# Run the server:
# python manage.py runserver

# Open in browser:
# http://127.0.0.1:8000/add-restaurant/

# ------------------------------------------------------------------------------------


# Important Concepts

# ModelForm:
# Automatically creates a form based on a Django model.

# Meta class:
# Defines the model and fields used by the form.

# form.save():
# Saves valid form data to the database.

# widgets:
# Customizes how form fields appear in HTML.

# min_length:
# Requires a minimum number of characters.

# min_value and max_value:
# Restrict the allowed rating range.

# is_valid():
# Validates submitted data before saving.

# ------------------------------------------------------------------------------------