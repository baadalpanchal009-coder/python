# SESSION 4 - CRUD Operations
# Topics: Create, Read, Update, Delete, Editing Using ModelForm,
# Delete Confirmation Page
# ------------------------------------------------------------------------------------


# Task 1: Create Product Model

# File: foodiespot/models.py

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Run these commands in the terminal:
# python manage.py makemigrations foodiespot
# python manage.py migrate

# ------------------------------------------------------------------------------------


# Task 2: Create Product ModelForm

# File: foodiespot/forms.py

from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category']


# ------------------------------------------------------------------------------------


# Task 3: Create, Read, Update and Delete Views

# File: foodiespot/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm


# CREATE: Add a new product

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})


# READ: Display all products

def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        'product_list.html',
        {'products': products}
    )


# UPDATE: Edit an existing product

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(
        request,
        'edit_product.html',
        {'form': form, 'product': product}
    )


# DELETE: Confirm before deleting a product

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(
        request,
        'delete_product.html',
        {'product': product}
    )


# ------------------------------------------------------------------------------------


# Task 4: Configure URL Routing

# File: foodiehub_project/urls.py

from django.contrib import admin
from django.urls import path
from foodiespot.views import (
    add_product,
    product_list,
    edit_product,
    delete_product,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', product_list, name='product_list'),
    path('products/add/', add_product, name='add_product'),
    path(
        'products/edit/<int:product_id>/',
        edit_product,
        name='edit_product'
    ),
    path(
        'products/delete/<int:product_id>/',
        delete_product,
        name='delete_product'
    ),
]


# ------------------------------------------------------------------------------------


# Task 5: Create Add Product Template

# File: templates/add_product.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Add Product</title>
</head>
<body>
    <h1>Add New Product</h1>

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save Product</button>
    </form>

    <a href="{% url 'product_list' %}">Back to Products</a>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Task 6: Display Products in a Table with Edit and Delete Buttons

# File: templates/product_list.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Product List</title>
</head>
<body>
    <h1>All Products</h1>

    <a href="{% url 'add_product' %}">Add New Product</a>

    <table border="1" cellpadding="10">
        <tr>
            <th>Name</th>
            <th>Price</th>
            <th>Category</th>
            <th>Actions</th>
        </tr>

        {% for product in products %}
        <tr>
            <td>{{ product.name }}</td>
            <td>{{ product.price }}</td>
            <td>{{ product.category }}</td>
            <td>
                <a href="{% url 'edit_product' product.id %}">
                    Edit
                </a>

                <a href="{% url 'delete_product' product.id %}">
                    Delete
                </a>
            </td>
        </tr>
        {% empty %}
        <tr>
            <td colspan="4">No products found.</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Task 7: Create Edit Product Template

# File: templates/edit_product.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Edit Product</title>
</head>
<body>
    <h1>Edit {{ product.name }}</h1>

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Update Product</button>
    </form>

    <a href="{% url 'product_list' %}">Cancel</a>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Task 8: Create Delete Confirmation Page

# File: templates/delete_product.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Delete Product</title>
</head>
<body>
    <h1>Delete Product</h1>

    <p>Are you sure you want to delete "{{ product.name }}"?</p>

    <form method="post">
        {% csrf_token %}
        <button type="submit">Yes, delete</button>
        <a href="{% url 'product_list' %}">Cancel</a>
    </form>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Run the Django Development Server

# python manage.py runserver

# Open in browser:
# http://127.0.0.1:8000/products/

# ------------------------------------------------------------------------------------


# Important Concepts

# Create:
# Adds a new product using ProductForm.

# Read:
# Displays all products using Product.objects.all().

# Update:
# Uses instance=product to pre-fill the form with existing data.

# Delete:
# Displays a confirmation page before deleting a product.

# ModelForm:
# Automatically creates a form from a Django model.

# get_object_or_404():
# Retrieves an object or returns an HTTP 404 response.

# form.save():
# Saves a new product or updates an existing product.

# CSRF Token:
# Protects POST forms against cross-site request forgery.

# ------------------------------------------------------------------------------------