# SESSION 4 - Django ORM: QuerySet Deep Dive
# Topics: filter(), exclude(), annotate(), select_related(),
# prefetch_related(), Aggregations, Q() Objects, Pagination
# ------------------------------------------------------------------------------------


# Task 1: Create Restaurant Model and Filter Chinese Restaurants
# File: foodiespot/models.py

from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    rating = models.FloatField()

    def __str__(self):
        return self.name


# File: foodiespot/views.py

from .models import Restaurant

restaurants = Restaurant.objects.filter(
    cuisine='Chinese',
    rating__gt=4
)

for restaurant in restaurants:
    print(restaurant.name, restaurant.cuisine, restaurant.rating)

# filter(): Retrieves objects matching the given conditions.
# rating__gt=4 means rating greater than 4.

# ------------------------------------------------------------------------------------


# Task 2: Exclude Users Whose Email Contains gmail.com

from django.contrib.auth.models import User

users = User.objects.exclude(
    email__contains='gmail.com'
)

for user in users:
    print(user.username, user.email)

# exclude(): Returns objects that do not match the given condition.
# email__contains performs a case-sensitive substring search.

# ------------------------------------------------------------------------------------


# Task 3: Count Reviews for Each Movie Using annotate()

# File: foodiespot/models.py

class Movie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    comment = models.TextField()
    rating = models.FloatField()

    def __str__(self):
        return f"Review for {self.movie.name}"


# File: foodiespot/views.py

from django.db.models import Count
from .models import Movie

movies = Movie.objects.annotate(
    review_count=Count('reviews')
)

for movie in movies:
    print(movie.name, movie.review_count)

# annotate(): Adds a calculated value to each object in a QuerySet.
# Count('reviews'): Counts the related reviews for each movie.

# ------------------------------------------------------------------------------------


# Task 4: Use select_related() to Fetch Products and Categories

# File: foodiespot/models.py

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __str__(self):
        return self.name


# File: foodiespot/views.py

from .models import Product

products = Product.objects.select_related('category').all()

for product in products:
    print(product.name, product.category.name)

# select_related(): Fetches related ForeignKey or OneToOne objects
# using a SQL JOIN, reducing additional database queries.

# ------------------------------------------------------------------------------------


# Task 5: Filter Products Using Q() and Paginate Results

# File: foodiespot/views.py

from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product


def product_list(request):
    products = Product.objects.filter(
        Q(category__name='Electronics') |
        Q(price__lt=1000)
    ).select_related('category').order_by('id')

    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'product_list.html',
        {'page_obj': page_obj}
    )


# ------------------------------------------------------------------------------------


# File: templates/product_list.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Product Listing</title>
</head>
<body>
    <h1>Products</h1>

    <table border="1" cellpadding="10">
        <tr>
            <th>Name</th>
            <th>Price</th>
            <th>Category</th>
        </tr>

        {% for product in page_obj %}
        <tr>
            <td>{{ product.name }}</td>
            <td>{{ product.price }}</td>
            <td>{{ product.category.name }}</td>
        </tr>
        {% empty %}
        <tr>
            <td colspan="3">No products found.</td>
        </tr>
        {% endfor %}
    </table>

    <div>
        {% if page_obj.has_previous %}
            <a href="?page=1">First</a>
            <a href="?page={{ page_obj.previous_page_number }}">
                Previous
            </a>
        {% endif %}

        <span>
            Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}
        </span>

        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">Next</a>
            <a href="?page={{ page_obj.paginator.num_pages }}">Last</a>
        {% endif %}
    </div>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Bonus: Use prefetch_related() for Related Reviews

from .models import Movie

movies = Movie.objects.prefetch_related('reviews').all()

for movie in movies:
    print("Movie:", movie.name)

    for review in movie.reviews.all():
        print("Review:", review.comment, "Rating:", review.rating)

# prefetch_related(): Fetches related objects in separate queries
# and joins them in Python. Useful for reverse ForeignKey and
# many-to-many relationships.

# ------------------------------------------------------------------------------------


# Bonus: Aggregation Examples

from django.db.models import Avg, Count, Max, Min
from .models import Restaurant

stats = Restaurant.objects.aggregate(
    average_rating=Avg('rating'),
    highest_rating=Max('rating'),
    lowest_rating=Min('rating'),
    total_restaurants=Count('id')
)

print(stats)

# aggregate(): Returns summary values for a QuerySet.

# ------------------------------------------------------------------------------------


# Bonus: Use Multiple Conditions with Q()

from django.db.models import Q
from .models import Restaurant

restaurants = Restaurant.objects.filter(
    Q(cuisine='Chinese') | Q(rating__gte=4.5)
)

for restaurant in restaurants:
    print(restaurant.name, restaurant.cuisine, restaurant.rating)

# | means OR
# & means AND
# ~Q(...) means NOT

# ------------------------------------------------------------------------------------


# Run Database Migrations

# python manage.py makemigrations foodiespot
# python manage.py migrate

# Open the Django shell:
# python manage.py shell

# ------------------------------------------------------------------------------------


# Important Concepts

# filter(): Selects matching records.
# exclude(): Excludes matching records.
# annotate(): Adds calculated values to each object.
# select_related(): Optimizes ForeignKey and OneToOne queries.
# prefetch_related(): Optimizes reverse and many-to-many queries.
# aggregate(): Calculates summary statistics.
# Q(): Combines conditions using OR, AND, and NOT.
# Paginator: Divides results into pages.
# order_by(): Sorts QuerySet results.

# ------------------------------------------------------------------------------------