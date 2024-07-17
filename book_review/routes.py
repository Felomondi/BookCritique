# book_review/routes.py
from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify
from flask_login import logout_user, login_user, login_required
from book_review.forms import RegistrationForm, LoginForm, ReviewForm
from book_review.models import User, Review
from book_review import db
import requests

main = Blueprint('main', __name__)

# Existing web routes
@main.route("/")
@main.route("/signup")
def home():
    return render_template('signup.html')

@main.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            user = User(username=form.username.data, email=form.email.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Account created successfully!', 'success')
            return redirect(url_for('main.homepage'))
        except Exception as e:
            print(f"Error: {e}")
            flash('An error occurred during registration.', 'danger')
    return render_template('register.html', title='Register', form=form)

@main.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember.data)
            flash('You have been logged in!', 'success')
            return redirect(url_for('main.homepage'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route("/review", methods=['GET', 'POST'])
@login_required
def review():
    form = ReviewForm()
    if form.validate_on_submit():
        review = Review(book_title=form.book_title.data, review=form.review.data, rating=form.rating.data, user_id=current_user.id)
        db.session.add(review)
        db.session.commit()
        flash('Review added successfully!', 'success')
        return redirect(url_for('main.home'))
    return render_template('review.html', title='Review', form=form)

# API endpoints
@main.route("/api/users", methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email, 'password':user.password} for user in users])

@main.route("/api/users", methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@main.route("/api/users/<int:id>", methods=['GET'])
def get_user_by_id(id):
    user = User.query.get_or_404(id)
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email})

@main.route("/api/users/username/<string:username>", methods=['GET'])
def get_user_by_username(username):
    user = User.query.filter_by(username=username).first_or_404()
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email})

@main.route("/api/reviews", methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    return jsonify([{'id': review.id, 'book_title': review.book_title, 'review': review.review, 'rating': review.rating, 'user_id': review.user_id} for review in reviews])

@main.route("/api/reviews", methods=['POST'])
def create_review():
    data = request.get_json()
    new_review = Review(book_title=data['book_title'], review=data['review'], rating=data['rating'], user_id=data['user_id'])
    db.session.add(new_review)
    db.session.commit()
    return jsonify({'message': 'Review created successfully'}), 201

# New route for book previews
@main.route("/homepage")
@login_required
def homepage():
    num_books = request.args.get('num_books', default=20, type=int)
    try:
        response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=programming&maxResults={num_books}')
        books = response.json().get('items', [])
    except Exception as e:
        print(f"Error fetching books: {e}")
        books = []
    return render_template('homepage.html', title='Book Previews', books=books)