python


# SESSION 4 - Maps & Geolocation API
# Topics: Google Maps API, Geocoding (Address to Latitude/Longitude),
# Embedding Maps in Django, Searching Locations by Distance
# ------------------------------------------------------------------------------------

# Task 1: Get Latitude and Longitude Using Google Geocoding API
# Install:
# pip install requests

# Set your Google Maps API key as an environment variable:
# GOOGLE_MAPS_API_KEY=YOUR_GOOGLE_MAPS_API_KEY

# File: geocoding.py

import os
import requests

def get_coordinates(address):
    api_key = os.environ.get('GOOGLE_MAPS_API_KEY')

    if not api_key:
        raise ValueError('Google Maps API key is not configured.')

    url = 'https://maps.googleapis.com/maps/api/geocode/json'

    response = requests.get(
        url,
        params={
            'address': address,
            'key': api_key
        },
        timeout=15
    )

    response.raise_for_status()
    data = response.json()

    if data.get('status') != 'OK':
        raise ValueError(
            f"Geocoding failed: {data.get('status')}"
        )

    location = data['results'][0]['geometry']['location']

    return location['lat'], location['lng']

if __name__ == '__main__':
    address = 'IIM Ahmedabad, Gujarat'
    latitude, longitude = get_coordinates(address)

    print('Address:', address)
    print('Latitude:', latitude)
    print('Longitude:', longitude)

# ------------------------------------------------------------------------------------

# Task 2: Display a Restaurant Location on Google Maps
# File: foodiespot/views.py

from django.shortcuts import render
from django.conf import settings
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def show_restaurant_location(request):
    address = ''
    latitude = None
    longitude = None
    error = None

    if request.method == 'POST':
        address = request.POST.get('address', '').strip()

        if address:
            try:
                latitude, longitude = get_coordinates(address)
            except (ValueError, requests.RequestException):
                error = 'Unable to find this location. Please try again.'
        else:
            error = 'Please enter a restaurant address.'

    return render(
        request,
        'restaurant_location.html',
        {
            'address': address,
            'latitude': latitude,
            'longitude': longitude,
            'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
            'error': error
        }
    )

# File: foodiehub_project/settings.py

"""
import os

GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY', '')
"""

# File: templates/restaurant_location.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Restaurant Location</title>
</head>
<body>
    <h1>Find Restaurant Location</h1>

    <form method="post">
        {% csrf_token %}
        <input
            type="text"
            name="address"
            placeholder="Enter restaurant address"
            value="{{ address }}"
            required
        >
        <button type="submit">Show Map</button>
    </form>

    {% if error %}
        <p>{{ error }}</p>
    {% endif %}

    {% if latitude != None and longitude != None %}
        <h2>{{ address }}</h2>

        <iframe
            width="600"
            height="450"
            style="border:0"
            loading="lazy"
            allowfullscreen
            referrerpolicy="no-referrer-when-downgrade"
            src="https://www.google.com/maps/embed/v1/view?key={{ google_maps_api_key }}&center={{ latitude }},{{ longitude }}&zoom=15">
        </iframe>

        <p>Latitude: {{ latitude }}</p>
        <p>Longitude: {{ longitude }}</p>
    {% endif %}
</body>
</html>
"""

# ------------------------------------------------------------------------------------

# Task 3: Find Cafes Within 3 KM Using the Haversine Formula
# No geolocation libraries are used.

import math

def haversine_distance(user_lat, user_lng, cafe_lat, cafe_lng):
    # Earth's average radius in kilometers
    earth_radius = 6371.0

    # Convert degrees to radians
    lat1 = math.radians(user_lat)
    lon1 = math.radians(user_lng)
    lat2 = math.radians(cafe_lat)
    lon2 = math.radians(cafe_lng)

    # Calculate differences
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    # Haversine formula
    a = (
        math.sin(delta_lat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(delta_lon / 2) ** 2
    )

    # Protect against floating-point rounding errors
    a = max(0.0, min(1.0, a))

    central_angle = 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )

    return earth_radius * central_angle

def find_nearby_cafes(user_lat, user_lng, cafes):
    nearby_cafes = []

    for cafe in cafes:
        distance = haversine_distance(
            user_lat,
            user_lng,
            cafe['lat'],
            cafe['lng']
        )

        if distance <= 3:
            nearby_cafes.append({
                **cafe,
                'distance': round(distance, 2)
            })

    return nearby_cafes

# Example usage

cafes = [
    {
        'name': 'Cafe Coffee Day',
        'lat': 23.0396,
        'lng': 72.5312
    },
    {
        'name': 'Starbucks',
        'lat': 23.0330,
        'lng': 72.5070
    },
    {
        'name': 'Local Cafe',
        'lat': 23.0225,
        'lng': 72.5714
    },
    {
        'name': 'Distant Cafe',
        'lat': 23.1000,
        'lng': 72.6000
    }
]

user_lat = 23.0330
user_lng = 72.5080

nearby = find_nearby_cafes(
    user_lat,
    user_lng,
    cafes
)

for cafe in nearby:
    print(
        cafe['name'],
        '-',
        cafe['distance'],
        'km away'
    )

# ------------------------------------------------------------------------------------

# Task 4: Search Flipkart Pickup Points by Distance
# File: foodiespot/views.py

from django.shortcuts import render
from django.views.decorators.http import require_http_methods

def search_by_distance(request):
    pickup_points = [
        {
            'name': 'Pickup Point 1',
            'address': 'IIM Ahmedabad, Vastrapur, Ahmedabad, Gujarat'
        },
        {
            'name': 'Pickup Point 2',
            'address': 'Law Garden, Ellisbridge, Ahmedabad, Gujarat'
        },
        {
            'name': 'Pickup Point 3',
            'address': 'Maninagar Railway Station, Ahmedabad, Gujarat'
        },
        {
            'name': 'Pickup Point 4',
            'address': 'SG Highway, Thaltej, Ahmedabad, Gujarat'
        },
        {
            'name': 'Pickup Point 5',
            'address': 'Gandhinagar Railway Station, Gujarat'
        }
    ]

    results = []
    error = None
    user_address = ''

    if request.method == 'POST':
        user_address = request.POST.get('address', '').strip()

        if not user_address:
            error = 'Please enter your current address.'
        else:
            try:
                user_lat, user_lng = get_coordinates(user_address)

                for point in pickup_points:
                    lat, lng = get_coordinates(point['address'])

                    distance = haversine_distance(
                        user_lat,
                        user_lng,
                        lat,
                        lng
                    )

                    results.append({
                        **point,
                        'lat': lat,
                        'lng': lng,
                        'distance': round(distance, 2)
                    })

                results.sort(key=lambda point: point['distance'])

            except (ValueError, requests.RequestException):
                error = 'Unable to find the address. Please try again.'

    return render(
        request,
        'pickup_points.html',
        {
            'results': results,
            'error': error,
            'user_address': user_address
        }
    )

# File: templates/pickup_points.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Nearby Pickup Points</title>
</head>
<body>
    <h1>Find Nearby Pickup Points</h1>

    <form method="post">
        {% csrf_token %}
        <input
            type="text"
            name="address"
            placeholder="Enter your current address"
            value="{{ user_address }}"
            required
        >
        <button type="submit">Search</button>
    </form>

    {% if error %}
        <p>{{ error }}</p>
    {% endif %}

    {% if results %}
        <h2>Pickup Points Sorted by Distance</h2>

        <table border="1" cellpadding="10">
            <tr>
                <th>Pickup Point</th>
                <th>Address</th>
                <th>Distance (KM)</th>
                <th>Map</th>
            </tr>

            {% for point in results %}
            <tr>
                <td>{{ point.name }}</td>
                <td>{{ point.address }}</td>
                <td>{{ point.distance }}</td>
                <td>
                    <a
                        href="https://www.google.com/maps/search/?api=1&query={{ point.lat }},{{ point.lng }}"
                        target="_blank"
                        rel="noopener noreferrer">
                        View Map
                    </a>
                </td>
            </tr>
            {% endfor %}
        </table>
    {% endif %}
</body>
</html>
"""

# ------------------------------------------------------------------------------------

# Configure URLs
# File: foodiehub_project/urls.py

"""
from django.contrib import admin
from django.urls import path
from foodiespot.views import (
    show_restaurant_location,
    search_by_distance
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'restaurant-location/',
        show_restaurant_location,
        name='restaurant_location'
    ),
    path(
        'pickup-points/',
        search_by_distance,
        name='search_by_distance'
    ),
]
"""

# ------------------------------------------------------------------------------------

# Run the Django Application
#
# pip install django requests
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
#
# Restaurant Map:
# http://127.0.0.1:8000/restaurant-location/
#
# Nearby Pickup Points:
# http://127.0.0.1:8000/pickup-points/
#
# Standalone Geocoding Script:
# python geocoding.py

# ------------------------------------------------------------------------------------

# Important Concepts
#
# Geocoding:
# Converts a street address into latitude and longitude.
#
# Google Maps Embed API:
# Displays an interactive map on a webpage.
#
# Haversine Formula:
# Calculates the approximate great-circle distance between two points.
#
# Sorting by Distance:
# Uses sorted() or list.sort() with the distance as the key.
#
# API Key:
# Keep your Google Maps key private and restrict it to the required APIs.
#
# Note:
# The pickup point addresses are illustrative examples, not verified
# Flipkart locations. Replace them with actual pickup point addresses.
# Enable Geocoding API and Maps Embed API in Google Cloud Console.
#
# ------------------------------------------------------------------------------------
