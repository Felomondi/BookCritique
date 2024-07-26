# run.py
from backend import create_app, db
from flask_cors import CORS

app = create_app()

CORS(app, resources={r"/api/*": {"origins": "*"}}) # Adjust origin as needed

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Initialize the database and create tables
    app.run(debug=True, host="0.0.0.0", port=5001)