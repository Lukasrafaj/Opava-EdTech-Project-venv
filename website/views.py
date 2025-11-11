from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def default():
    return render_template('default.html')

@views.route('/home')
@login_required
def home():
    print("Authenticated:", current_user.is_authenticated)
    return render_template('home.html')

@views.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@views.route('/courses')
def courses():
    return render_template('courses.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/donate')
def donate():
    return render_template('donate.html')

