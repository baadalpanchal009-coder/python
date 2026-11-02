# Restaurant Search System

'''from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cuisine = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return self.name
'''


# Restaurant search route (app.py)
"""

@app.route('/restaurants')
def restaurants():
    cuisine = request.args.get('cuisine', '')
    location = request.args.get('location', '')

    results = Restaurant.query.filter(
        Restaurant.cuisine.ilike(f'%{cuisine}%'),
        Restaurant.location.ilike(f'%{location}%')
    ).all()

    return render_template(
        'index.html',
        restaurants=results
    )
"""


# index.html

"""<h2>Restaurant Finder</h2>

<form action="/restaurants" method="GET">
    <input type="text" name="cuisine"
           placeholder="Enter Cuisine">

    <input type="text" name="location"
           placeholder="Enter Location">

    <button type="submit">Search</button>
</form>

<h3>Available Restaurants</h3>

{% for restaurant in restaurants %}
    <div>
        <h3>{{ restaurant.name }}</h3>
        <p>Cuisine: {{ restaurant.cuisine }}</p>
        <p>Location: {{ restaurant.location }}</p>
    </div>
{% else %}
    <p>No restaurants found.</p>
{% endfor %}
"""


#   Registration, Login & OTP Verification

"""import random
import time
from flask import Flask, render_template, request, redirect, session, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if User.query.filter_by(email=email).first():
            return "Email already registered"

        user = User(
            name=name,
            email=email,
            password=generate_password_hash(password)
        )

        db.session.add(user)
        db.session.commit()

        return redirect('/login')

    return render_template('register.html')


# Login and OTP Generation
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            otp = str(random.randint(100000, 999999))

            session['otp'] = otp
            session['otp_time'] = time.time()
            session['user_id'] = user.id

            # Demo: OTP displayed in terminal
            print("Your Login OTP is:", otp)

            return redirect('/verify-otp')

        return "Invalid email or password"

    return render_template('login.html')


# OTP Verification
@app.route('/verify-otp', methods=['GET', 'POST'])
def verify_otp():
    if 'otp' not in session:
        return redirect('/login')

    if request.method == 'POST':
        entered_otp = request.form['otp']

        if time.time() - session['otp_time'] > 180:
            session.pop('otp', None)
            session.pop('otp_time', None)
            session.pop('user_id', None)
            return "OTP Expired! Please login again."

        if entered_otp == session['otp']:
            session.pop('otp', None)
            session.pop('otp_time', None)
            session['logged_in'] = True
            return redirect('/dashboard')

        return "Invalid OTP"

    return render_template('verify_otp.html')


# User Dashboard
@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect('/login')

    user = User.query.get(session['user_id'])
    return render_template('dashboard.html', user=user)


# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
"""

# register.html
"""
<h2>User Registration</h2>

<form method="POST">
    <input type="text" name="name"
           placeholder="Enter Name" required><br><br>

    <input type="email" name="email"
           placeholder="Enter Email" required><br><br>

    <input type="password" name="password"
           placeholder="Enter Password" required><br><br>

    <button type="submit">Register</button>
</form>
"""


# login.html
"""
<h2>User Login</h2>

<form method="POST">
    <input type="email" name="email"
           placeholder="Enter Email" required><br><br>

    <input type="password" name="password"
           placeholder="Enter Password" required><br><br>

    <button type="submit">Login</button>
</form>
"""


# verify_otp.html
"""
<h2>OTP Verification</h2>

<p>Enter your 6-digit OTP.</p>

<form method="POST">
    <input type="text" name="otp"
           maxlength="6" required
           placeholder="Enter OTP">

    <button type="submit">Verify OTP</button>
</form>
"""

# dashboard.html
"""
<h2>Welcome to User Dashboard</h2>

<p>Hello, {{ user.name }}!</p>
<p>Email: {{ user.email }}</p>

<a href="/profile">Manage Profile</a><br><br>
<a href="/restaurants">Search Restaurants</a><br><br>
<a href="/map">Open Google Maps</a><br><br>
<a href="/logout">Logout</a>
"""


#  User Profile Management
"""

import os
from werkzeug.utils import secure_filename

app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if not session.get('logged_in'):
        return redirect('/login')

    user = User.query.get(session['user_id'])

    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        user.address = request.form['address']

        file = request.files.get('picture')

        if file and file.filename:
            filename = secure_filename(file.filename)
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            file.save(os.path.join(
                app.config['UPLOAD_FOLDER'], filename
            ))
            user.profile_picture = filename

        db.session.commit()
        return redirect('/profile')

    return render_template('profile.html', user=user)
"""

# profile.html
"""

<h2>My Profile</h2>

{% if user.profile_picture %}
<img src="{{ url_for('static',
filename='uploads/' + user.profile_picture) }}"
width="120">
{% endif %}

<form method="POST" enctype="multipart/form-data">

    Name:
    <input type="text" name="name"
           value="{{ user.name }}" required><br><br>

    Email:
    <input type="email" name="email"
           value="{{ user.email }}" required><br><br>

    Address:
    <textarea name="address">{{ user.address or '' }}</textarea>
    <br><br>

    Profile Picture:
    <input type="file" name="picture"
           accept="image/*"><br><br>

    <button type="submit">Update Profile</button>
</form>
"""


# app.py route:
"""

@app.route('/map')
def map_page():
    if not session.get('logged_in'):
        return redirect('/login')

    return render_template('map.html')
"""

# map.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>Cab Booking Map</title>

    <style>
        #map {
            height: 450px;
            width: 100%;
        }
    </style>
</head>

<body>

<h2>Cab Booking - Select Pickup Location</h2>

<p id="location">Select your pickup location.</p>

<div id="map"></div>

<script>
let map;
let marker;

function initMap() {
    const defaultLocation = {
        lat: 23.0225,
        lng: 72.5714
    };

    map = new google.maps.Map(
        document.getElementById("map"), {
            center: defaultLocation,
            zoom: 13
        }
    );

    marker = new google.maps.Marker({
        position: defaultLocation,
        map: map,
        draggable: true
    });

    function updateLocation(position) {
        marker.setPosition(position);
        map.setCenter(position);

        document.getElementById("location").innerText =
            "Pickup: " + position.lat.toFixed(6) +
            ", " + position.lng.toFixed(6);
    }

    map.addListener("click", function(event) {
        updateLocation({
            lat: event.latLng.lat(),
            lng: event.latLng.lng()
        });
    });

    marker.addListener("dragend", function(event) {
        updateLocation({
            lat: event.latLng.lat(),
            lng: event.latLng.lng()
        });
    });

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function(position) {
                updateLocation({
                    lat: position.coords.latitude,
                    lng: position.coords.longitude
                });
            },
            function() {
                console.log("Location permission not granted");
            }
        );
    }
}
</script>

<script async defer
src="https://maps.googleapis.com/maps/api/js?key=YOUR_GOOGLE_MAPS_API_KEY&callback=initMap">
</script>

</body>
</html>
"""


# git hub
# git init
# git add .
# git commit -m "Session 20 project completed"
# git branch -M main
# git remote add origin https://github.com/YOUR_USERNAME/Session20-Integration-Project.git
# git push -u origin main

# B. Create requirements.txt
"""
Flask
Flask-SQLAlchemy
Flask-Login
Werkzeug
gunicorn
"""
# Main Flask Application Setup
"""

from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "session20_demo_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import your Restaurant and User models here
# if they are defined in a separate models.py file.

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
"""