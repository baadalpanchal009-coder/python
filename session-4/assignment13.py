# SESSION 4 - CRUD Using AJAX
# Topics: AJAX Introduction, Fetch API, Sending JSON Request,
# Handling JSON Responses
# ------------------------------------------------------------------------------------


# Task 1: Create Song List and Delete Songs Using AJAX

# File: templates/songs.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>My Spotify Playlist</title>
</head>
<body>
    <h1>My Spotify Playlist</h1>

    <ul id="songList">
        <li id="song-1">
            Shape of You
            <button onclick="deleteSong(1)">Delete</button>
        </li>

        <li id="song-2">
            Perfect
            <button onclick="deleteSong(2)">Delete</button>
        </li>

        <li id="song-3">
            Believer
            <button onclick="deleteSong(3)">Delete</button>
        </li>
    </ul>

    <p id="message"></p>

    <script>
        async function deleteSong(songId) {
            try {
                const response = await fetch(
                    `https://jsonplaceholder.typicode.com/posts/${songId}`,
                    { method: 'DELETE' }
                );

                if (response.ok) {
                    document.getElementById(
                        `song-${songId}`
                    ).remove();

                    document.getElementById('message').textContent =
                        'Song deleted successfully!';
                } else {
                    document.getElementById('message').textContent =
                        'Failed to delete song.';
                }
            } catch (error) {
                document.getElementById('message').textContent =
                    'An error occurred.';
            }
        }
    </script>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Task 2: Flipkart-Style Wishlist Using AJAX

# File: foodiespot/views.py

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect


@require_http_methods(["DELETE"])
@csrf_protect
def remove_from_wishlist(request, product_id):
    # Demo example: Replace with a real database deletion.
    return JsonResponse({
        'success': True,
        'message': 'Product removed from wishlist!',
        'product_id': product_id
    })


# File: foodiehub_project/urls.py

"""
from django.contrib import admin
from django.urls import path
from foodiespot.views import remove_from_wishlist

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'wishlist/remove/<int:product_id>/',
        remove_from_wishlist,
        name='remove_from_wishlist'
    ),
]
"""


# File: templates/wishlist.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>My Wishlist</title>
</head>
<body>
    <h1>My Wishlist</h1>

    <p id="message"></p>

    <div id="product-1">
        <span>Wireless Headphones - ₹1999</span>
        <button onclick="removeProduct(1)">Remove from Wishlist</button>
    </div>

    <div id="product-2">
        <span>Smart Watch - ₹2999</span>
        <button onclick="removeProduct(2)">Remove from Wishlist</button>
    </div>

    <script>
        async function removeProduct(productId) {
            try {
                const response = await fetch(
                    `/wishlist/remove/${productId}/`,
                    {
                        method: 'DELETE',
                        headers: {
                            'X-CSRFToken': getCookie('csrftoken')
                        }
                    }
                );

                const data = await response.json();

                if (response.ok && data.success) {
                    document.getElementById(
                        `product-${productId}`
                    ).remove();

                    document.getElementById('message').textContent =
                        data.message;
                } else {
                    document.getElementById('message').textContent =
                        'Could not remove product.';
                }
            } catch (error) {
                document.getElementById('message').textContent =
                    'An error occurred.';
            }
        }

        function getCookie(name) {
            const cookies = document.cookie.split(';');

            for (const cookie of cookies) {
                const item = cookie.trim();

                if (item.startsWith(name + '=')) {
                    return decodeURIComponent(
                        item.substring(name.length + 1)
                    );
                }
            }

            return '';
        }
    </script>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Task 3: BookMyShow-Style Watch Later List Using JSON

# File: foodiespot/views.py

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
import json


@require_http_methods(["DELETE"])
@csrf_protect
def delete_watch_later(request, movie_id):
    try:
        data = json.loads(request.body or '{}')
    except json.JSONDecodeError:
        return JsonResponse(
            {'success': False, 'message': 'Invalid JSON.'},
            status=400
        )

    # Demo example: Replace with real database deletion.
    return JsonResponse({
        'success': True,
        'message': f"Movie {movie_id} removed from Watch Later!",
        'movie_id': movie_id
    })


# Add to foodiehub_project/urls.py

"""
path(
    'watch-later/delete/<int:movie_id>/',
    delete_watch_later,
    name='delete_watch_later'
),
"""


# File: templates/watch_later.html

"""
<!DOCTYPE html>
<html>
<head>
    <title>Watch Later</title>
</head>
<body>
    <h1>My Watch Later List</h1>

    <p id="message"></p>

    <div id="movie-1">
        <span>Avengers: Endgame</span>
        <button onclick="deleteMovie(1)">Remove</button>
    </div>

    <div id="movie-2">
        <span>Spider-Man</span>
        <button onclick="deleteMovie(2)">Remove</button>
    </div>

    <script>
        async function deleteMovie(movieId) {
            try {
                const response = await fetch(
                    `/watch-later/delete/${movieId}/`,
                    {
                        method: 'DELETE',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': getCookie('csrftoken')
                        },
                        body: JSON.stringify({
                            movie_id: movieId
                        })
                    }
                );

                const data = await response.json();

                if (response.ok && data.success) {
                    document.getElementById(
                        `movie-${movieId}`
                    ).remove();

                    document.getElementById('message').textContent =
                        data.message;
                } else {
                    document.getElementById('message').textContent =
                        'Failed to remove movie.';
                }
            } catch (error) {
                document.getElementById('message').textContent =
                    'An error occurred.';
            }
        }

        function getCookie(name) {
            const cookies = document.cookie.split(';');

            for (const cookie of cookies) {
                const item = cookie.trim();

                if (item.startsWith(name + '=')) {
                    return decodeURIComponent(
                        item.substring(name.length + 1)
                    );
                }
            }

            return '';
        }
    </script>
</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Task 4: Debug AJAX Delete - Update the DOM After Success

# Incorrect approach:
#
# fetch(url, {method: 'DELETE'});
# // The page element is never removed.

# Correct approach:

"""
async function deleteItem(url, elementId) {
    try {
        const response = await fetch(url, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        });

        const data = await response.json();

        if (response.ok && data.success) {
            const element = document.getElementById(elementId);

            if (element) {
                element.remove();
            }

            document.getElementById('message').textContent =
                'Item deleted successfully!';
        } else {
            document.getElementById('message').textContent =
                'Deletion failed.';
        }
    } catch (error) {
        document.getElementById('message').textContent =
            'Network error.';
    }
}
"""

# Main fixes:
# 1. Wait for the fetch response using await.
# 2. Check response.ok and the JSON success value.
# 3. Remove the correct DOM element after successful deletion.
# 4. Display a success or error message.
# 5. Include the CSRF token when using Django's CSRF protection.

# ------------------------------------------------------------------------------------


# Important Concepts

# AJAX:
# Sends requests without reloading the entire page.

# Fetch API:
# JavaScript API for making HTTP requests.

# DELETE:
# HTTP method commonly used to delete a resource.

# JSON:
# Format used to exchange data between client and server.

# JsonResponse:
# Django response class for sending JSON data.

# element.remove():
# Removes an HTML element from the page.

# response.ok:
# Indicates whether the HTTP response status is successful.

# ------------------------------------------------------------------------------------