# Book Review and Rating Website

Welcome to our Book Review and Rating Website! This web application allows users to write reviews and rate books. The book data is fetched from the Google Books API, and user information such as username, email, reviews, and ratings are stored in an SQLite database.

## Features

- User registration and login
- Book review and rating
- Fetch book previews from Google Books API
- Responsive web interface

## Technologies Used

- Flask (Python)
- SQLite
- HTML/CSS (Bootstrap) - Not decided 
- JavaScript - If we decide to use Raect fro frontend 
- Google Books API

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.6+
- pip (Python package installer)

## Installation

### Step 1: Clone the Repository
### Step 2: Set Up Python Virtual Environment
- On macOS and Linux:
```sh
python3 -m venv venv
source venv/bin/activate
```
- On Windows:
```sh
python -m venv venv
venv\Scripts\activate
```
### Step 3: Install Python Dependencies
```sh
pip install -r requirements.txt
```
### Step 4: Set Up Environment Variables
```sh
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
```

### Step 5: Run the Flask Application
```sh
flask run
```
#### To contribute, please clone the repo, create a new branch for your changes and submit a pull request! 

# Enjoy!!








