# routes.py
from flask import Blueprint, request, jsonify
from flask_login import login_user, login_required, current_user
from .forms import RegistrationForm, LoginForm, ReviewForm
from .models import User, Review
from . import db
import requests
from flask_cors import CORS

main = Blueprint('main', __name__)

@main.route('/register', methods=['POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return jsonify({'message': 'Invalid input data'}), 400

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'message': 'User already exists!'}), 400

        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        print(f"Error during registration: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500

@main.route('/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            login_user(user)
            return jsonify({'message': 'You have been logged in!'}), 200
        else:
            return jsonify({'message': 'Login Unsuccessful. Please check email and password'}), 401
    except Exception as e:
        print(f"Error during login: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500

def _build_cors_preflight_response():
    response = jsonify({'message': 'CORS preflight successful'})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE,OPTIONS")
    return response


@main.route('/reviews', methods=['GET', 'POST'])
@login_required
def reviews():
    if request.method == 'GET':
        reviews = Review.query.all()
        return jsonify([review.to_dict() for review in reviews])
    elif request.method == 'POST':
        data = request.get_json()
        form = ReviewForm(data=data)
        if form.validate_on_submit():
            review = Review(book_title=form.book_title.data, review=form.review.data, rating=form.rating.data, user_id=current_user.id)
            db.session.add(review)
            db.session.commit()
            return jsonify({'message': 'Review added successfully!'}), 201
        return jsonify({'errors': form.errors}), 400

@main.route('/books', methods=['GET', 'OPTIONS'])
def books():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    query = request.args.get('query', default='bestsellers', type=str)
    num_books = request.args.get('num_books', default=12, type=int)
    try:
        response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={num_books}')
        books = response.json().get('items', [])
        return jsonify(books), 200
    except Exception as e:
        print(f"Error fetching books: {e}")
        return jsonify({'error': str(e)}), 500

@main.route('/books/<string:id>', methods=['GET', 'OPTIONS'])
def get_book_by_id(id):
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    try:
        response = requests.get(f'https://www.googleapis.com/books/v1/volumes/{id}')
        if response.status_code == 200:
            book = response.json()
            return jsonify(book), 200
        else:
            return jsonify({'error': 'Book not found'}), 404
    except Exception as e:
        print(f"Error fetching book details: {e}")
        return jsonify({'error': str(e)}), 500
    

@main.route('/users', methods=['GET', 'OPTIONS'])
def get_users():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email, 'password': user.password} for user in users])

@main.route('/users', methods=['POST', 'OPTIONS'])
def create_user():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@main.route('/users/<int:id>', methods=['GET', 'OPTIONS'])
def get_user_by_id(id):
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    user = User.query.get_or_404(id)
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email})

@main.route('/users/username/<string:username>', methods=['GET', 'OPTIONS'])
def get_user_by_username(username):
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    user = User.query.filter_by(username=username).first_or_404()
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email})

@main.route('/reviews', methods=['GET', 'OPTIONS'])
def get_reviews():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    reviews = Review.query.all()
    return jsonify([{'id': review.id, 'book_title': review.book_title, 'review': review.review, 'rating': review.rating, 'user_id': review.user_id} for review in reviews])

@main.route('/reviews', methods=['POST', 'OPTIONS'])
def create_review():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    data = request.get_json()
    new_review = Review(book_title=data['book_title'], review=data['review'], rating=data['rating'], user_id=data['user_id'])
    db.session.add(new_review)
    db.session.commit()
    return jsonify({'message': 'Review created successfully'}), 201

# Add other routes as needed