# run.py
from book_review import create_app, db

app = create_app()

# with app.app_context():
#     db.create_all()

if __name__ == '__main__':
    app.run(debug=True)