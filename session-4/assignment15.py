# SESSION 4 - Django Authentication (Advanced)
# Topics: Login Required Decorator, Role-Based Access,
# Permissions, Groups, Role-Based Dashboards
# ------------------------------------------------------------------------------------


# Task 1: Create a My Orders Page Using @login_required

# File: foodiespot/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def my_orders(request):
    return render(request, 'my_orders.html')


# File: templates/my_orders.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>My Orders</title>
</head>
<body>
    <h1>My Orders</h1>
    <p>Welcome, {{ user.username }}!</p>
    <p>Here you can view your order history.</p>
</body>
</html>
"""

# Only logged-in users can access the My Orders page.
# Anonymous users are redirected to the login page.

# ------------------------------------------------------------------------------------


# Task 2: Create Seller and Buyer Roles Using Django Groups

# File: foodiespot/decorators.py

from django.contrib.auth.decorators import user_passes_test


def seller_required(view_func):
    return user_passes_test(
        lambda user: (
            user.is_authenticated
            and user.groups.filter(name='Seller').exists()
        ),
        login_url='login',
        permission_denied_message='Only Sellers can post products.'
    )(view_func)


# File: foodiespot/views.py

from django.contrib.auth.decorators import login_required
from .decorators import seller_required


@login_required(login_url='login')
@seller_required
def post_product(request):
    return render(request, 'post_product.html')


# File: templates/post_product.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Post Product</title>
</head>
<body>
    <h1>Seller Product Management</h1>
    <p>You can post your products here.</p>
</body>
</html>
"""

# Create Seller and Buyer groups in Django Admin:
# 1. Run: python manage.py createsuperuser
# 2. Open: http://127.0.0.1:8000/admin/
# 3. Open Groups and create Seller and Buyer.
# 4. Assign users to the appropriate groups.

# ------------------------------------------------------------------------------------


# Task 3: Create MovieCritic and MovieFan Groups with Permissions

# File: foodiespot/models.py

from django.db import models


class MovieReview(models.Model):
    movie_name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        return self.movie_name


# Run migrations to create default model permissions:
# python manage.py makemigrations foodiespot
# python manage.py migrate

# Django automatically creates these permissions:
# add_moviereview
# change_moviereview
# delete_moviereview
# view_moviereview

# Create groups in Django Admin:
#
# MovieCritic:
# - Add Movie Review
# - Change Movie Review
# - View Movie Review
#
# MovieFan:
# - View Movie Review only
#
# Assign users to each group using the admin panel.

# ------------------------------------------------------------------------------------


# Restrict Movie Review Pages by Permissions

# File: foodiespot/views.py

from django.contrib.auth.decorators import permission_required
from .models import MovieReview


@permission_required(
    'foodiespot.view_moviereview',
    raise_exception=True
)
def movie_reviews(request):
    reviews = MovieReview.objects.all()

    return render(
        request,
        'movie_reviews.html',
        {'reviews': reviews}
    )


@permission_required(
    'foodiespot.add_moviereview',
    raise_exception=True
)
def add_movie_review(request):
    return render(request, 'add_movie_review.html')


@permission_required(
    'foodiespot.change_moviereview',
    raise_exception=True
)
def edit_movie_review(request, review_id):
    review = MovieReview.objects.get(id=review_id)

    return render(
        request,
        'edit_movie_review.html',
        {'review': review}
    )


# ------------------------------------------------------------------------------------


# Task 4: Create Role-Based Dashboards

# File: foodiespot/views.py

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def dashboard_redirect(request):
    user = request.user

    if user.groups.filter(name='Seller').exists():
        return redirect('seller_dashboard')

    elif user.groups.filter(name='Buyer').exists():
        return redirect('buyer_dashboard')

    return redirect('home')


@login_required(login_url='login')
def seller_dashboard(request):
    if not request.user.groups.filter(name='Seller').exists():
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied

    return render(request, 'seller_dashboard.html')


@login_required(login_url='login')
def buyer_dashboard(request):
    if not request.user.groups.filter(name='Buyer').exists():
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied

    return render(request, 'buyer_dashboard.html')


# File: templates/seller_dashboard.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Seller Dashboard</title>
</head>
<body>
    <h1>Welcome to Seller Dashboard</h1>
    <p>Manage your products and sales here.</p>
</body>
</html>
"""


# File: templates/buyer_dashboard.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Buyer Dashboard</title>
</head>
<body>
    <h1>Welcome to Buyer Dashboard</h1>
    <p>View your orders and purchase history here.</p>
</body>
</html>
"""

# In your existing login view, redirect after successful login:
#
# from django.contrib.auth import login
# login(request, user)
# return redirect('dashboard_redirect')

# ------------------------------------------------------------------------------------


# Task 5: Restrict Playlist Admin Access to the Admin Group

# File: foodiespot/models.py

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# Run migrations:
# python manage.py makemigrations foodiespot
# python manage.py migrate


# File: foodiespot/admin.py

from django.contrib import admin
from django.core.exceptions import PermissionDenied
from .models import Playlist


class PlaylistAdmin(admin.ModelAdmin):

    def has_module_permission(self, request):
        return (
            request.user.is_active
            and request.user.is_staff
            and request.user.groups.filter(name='Admin').exists()
        )

    def has_view_permission(self, request, obj=None):
        return self.has_module_permission(request)

    def has_add_permission(self, request):
        return self.has_module_permission(request)

    def has_change_permission(self, request, obj=None):
        return self.has_module_permission(request)

    def has_delete_permission(self, request, obj=None):
        return self.has_module_permission(request)


admin.site.register(Playlist, PlaylistAdmin)


# Create an Admin group in Django Admin and assign the required
# staff users to it. Only active staff members in this group
# can view, add, edit, or delete Playlist records in the admin.
#
# Django superusers normally bypass ordinary permission checks,
# so use a non-superuser staff account to test this restriction.

# ------------------------------------------------------------------------------------


# Configure URLs

# File: foodiehub_project/urls.py

"""
from django.contrib import admin
from django.urls import path
from foodiespot import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('my-orders/', views.my_orders, name='my_orders'),
    path('post-product/', views.post_product, name='post_product'),

    path(
        'movie-reviews/',
        views.movie_reviews,
        name='movie_reviews'
    ),
    path(
        'movie-reviews/add/',
        views.add_movie_review,
        name='add_movie_review'
    ),
    path(
        'movie-reviews/edit/<int:review_id>/',
        views.edit_movie_review,
        name='edit_movie_review'
    ),

    path(
        'dashboard/',
        views.dashboard_redirect,
        name='dashboard_redirect'
    ),
    path(
        'seller-dashboard/',
        views.seller_dashboard,
        name='seller_dashboard'
    ),
    path(
        'buyer-dashboard/',
        views.buyer_dashboard,
        name='buyer_dashboard'
    ),
]
"""

# ------------------------------------------------------------------------------------


# Important Concepts

# @login_required:
# Allows access only to authenticated users.

# Groups:
# Organize users into roles such as Seller, Buyer, MovieCritic and MovieFan.

# user.groups.filter().exists():
# Checks whether a user belongs to a particular group.

# @permission_required:
# Restricts access based on Django model permissions.

# has_module_permission():
# Controls whether a model appears in the Django admin index.

# has_view_permission():
# Controls permission to view model records.

# has_add_permission():
# Controls permission to add records.

# has_change_permission():
# Controls permission to edit records.

# has_delete_permission():
# Controls permission to delete records.

# ------------------------------------------------------------------------------------


# Run the Application

# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
# python manage.py runserver

# Django Admin:
# http://127.0.0.1:8000/admin/

# My Orders:
# http://127.0.0.1:8000/my-orders/

# Post Product:
# http://127.0.0.1:8000/post-product/

# Role-Based Dashboard:
# http://127.0.0.1:8000/dashboard/

# Movie Reviews:
# http://127.0.0.1:8000/movie-reviews/

# ------------------------------------------------------------------------------------