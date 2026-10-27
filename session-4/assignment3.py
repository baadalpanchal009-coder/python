# SESSION 4 - Templates & Static Files
# Topics: Templates Folder Structure, Template Inheritance (base.html),
# Loading Static Files (CSS, JS), Using Template Tags
# ------------------------------------------------------------------------------------


# Task 1: Create templates folder and base.html

# File: templates/base.html

"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Website</title>
</head>
<body>

    <nav>
        <a href="/">Home</a>
        <a href="/explore/">Explore</a>
        <a href="/profile/">Profile</a>
    </nav>

    <main>
        <h1>Welcome to My Website</h1>
    </main>

    <footer>
        <p>© 2026 My Website</p>
    </footer>

</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Task 2: Add Bootstrap CDN and Footer

# File: templates/base.html

"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Website</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
          rel="stylesheet">
</head>
<body class="d-flex flex-column min-vh-100">

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="/">My Website</a>
            <div class="navbar-nav">
                <a class="nav-link" href="/">Home</a>
                <a class="nav-link" href="/explore/">Explore</a>
                <a class="nav-link" href="/profile/">Profile</a>
            </div>
        </div>
    </nav>

    <main class="container my-4 flex-grow-1">
        <h1>Welcome to My Website</h1>
    </main>

    <footer class="bg-dark text-white text-center p-3 mt-auto">
        <p class="mb-0">© 2026 My Website. All rights reserved.</p>
    </footer>

</body>
</html>
"""

# ------------------------------------------------------------------------------------


# Task 3: Create home.html Using Template Inheritance

# File: templates/home.html

"""
{% extends 'base.html' %}

{% block content %}
<div class="container text-center mt-5">
    <h1>Welcome to My Website!</h1>
    <p>Explore trending playlists and discover something new.</p>
</div>
{% endblock %}
"""

# Add this block inside base.html main section:
# {% block content %}{% endblock %}
# ------------------------------------------------------------------------------------


# Task 4: Create Static Folder and Add Custom CSS

# File structure:
#
# project/
#     manage.py
#     static/
#         style.css
#     templates/
#         base.html
#         home.html
#         explore.html

# File: static/style.css

"""
body {
    background-color: #f0f8ff;
    font-family: Arial, sans-serif;
}

h1 {
    color: #198754;
}

footer {
    width: 100%;
}
"""

# Add these lines near the top of base.html, before the HTML:
# {% load static %}

# Add this inside the <head> section:
# <link rel="stylesheet" href="{% static 'style.css' %}">

# Configure static files in settings.py if necessary:
# STATIC_URL = 'static/'
# STATICFILES_DIRS = [BASE_DIR / 'static']
# ------------------------------------------------------------------------------------


# Task 5: Create explore.html with 6 Bootstrap Cards

# File: templates/explore.html

"""
{% extends 'base.html' %}

{% block content %}
<div class="container mt-4">
    <h1 class="text-center mb-4">Trending Playlists</h1>

    <div class="row g-4">

        <div class="col-md-4">
            <div class="card">
                <img src="https://placehold.co/400x250?text=Chill+Vibes"
                     class="card-img-top" alt="Chill Vibes">
                <div class="card-body">
                    <h5 class="card-title">Chill Vibes</h5>
                    <p class="card-text">Relax and enjoy your favorite music.</p>
                </div>
            </div>
        </div>

        <div class="col-md-4">
            <div class="card">
                <img src="https://placehold.co/400x250?text=Top+Hits"
                     class="card-img-top" alt="Top Hits">
                <div class="card-body">
                    <h5 class="card-title">Top Hits</h5>
                    <p class="card-text">Listen to the latest popular songs.</p>
                </div>
            </div>
        </div>

        <div class="col-md-4">
            <div class="card">
                <img src="https://placehold.co/400x250?text=Workout"
                     class="card-img-top" alt="Workout">
                <div class="card-body">
                    <h5 class="card-title">Workout Mix</h5>
                    <p class="card-text">Music to power your workouts.</p>
                </div>
            </div>
        </div>

        <div class="col-md-4">
            <div class="card">
                <img src="https://placehold.co/400x250?text=Romantic"
                     class="card-img-top" alt="Romantic">
                <div class="card-body">
                    <h5 class="card-title">Romantic Songs</h5>
                    <p class="card-text">Enjoy beautiful romantic melodies.</p>
                </div>
            </div>
        </div>

        <div class="col-md-4">
            <div class="card">
                <img src="https://placehold.co/400x250?text=Party+Mix"
                     class="card-img-top" alt="Party Mix">
                <div class="card-body">
                    <h5 class="card-title">Party Mix</h5>
                    <p class="card-text">Get ready to dance and celebrate.</p>
                </div>
            </div>
        </div>

        <div class="col-md-4">
            <div class="card">
                <img src="https://placehold.co/400x250?text=Classics"
                     class="card-img-top" alt="Classics">
                <div class="card-body">
                    <h5 class="card-title">Classic Favorites</h5>
                    <p class="card-text">Rediscover timeless music.</p>
                </div>
            </div>
        </div>

    </div>
</div>
{% endblock %}
"""

# ------------------------------------------------------------------------------------


# Important: base.html Must Have a Content Block

# Inside base.html, replace the main section with:
#
# <main class="container my-4 flex-grow-1">
#     {% block content %}{% endblock %}
# </main>

# ------------------------------------------------------------------------------------


# Summary

# base.html: Common layout, navbar, footer, Bootstrap CDN.
# home.html: Home page that inherits base.html.
# explore.html: Displays six Bootstrap playlist cards.
# style.css: Custom styling for the website.
# {% extends 'base.html' %}: Enables template inheritance.
# {% load static %}: Loads Django's static template tags.
# {% static 'style.css' %}: Generates the static CSS file URL.

# ------------------------------------------------------------------------------------