# check_db.py
from backend import create_app, db
from backend.models import User, Review, Book
from sqlalchemy import inspect

app = create_app()

with app.app_context():
    inspector = inspect(db.engine)
    
    tables = inspector.get_table_names()
    print(f"Tables in the database: {tables}")
    
    for table in tables:
        columns = inspector.get_columns(table)
        print(f"\nTable {table} columns:")
        for column in columns:
            print(f"{column['name']} - {column['type']}")

    users = User.query.all()
    print(f"\nUsers in the database: {users}")

    reviews = Review.query.all()
    print(f"\nReviews in the database: {reviews}")