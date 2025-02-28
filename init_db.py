from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from apps import create_app
from apps import db
from apps.models import ArtistsData

app = create_app()


# ========== DATABASE CREATION ==========
@app.before_first_request
def create_tables():
    """Create all tables before the first request."""
    db.create_all()
    seed_database()  # Insert sample data


def seed_database():
    """Insert sample data into the database if it's empty."""
    if not ArtistsData.query.first():  # Prevent duplicate data insertion
        print("📌 Seeding initial data...")

        artist1 = ArtistsData(
            name="Alice Johnson",
            email="alice@example.com",
            height=165,
            weight=60,
            dob=date(1990, 5, 15),
        )
        artist2 = ArtistsData(
            name="Bob Smith",
            email="bob@example.com",
            height=175,
            weight=70,
            dob=date(1985, 7, 22),
        )

        db.session.add_all([artist1, artist2])
        db.session.commit()
        print("✅ Sample data added!")


# ========== RUN THE APP ==========
if __name__ == "__main__":
    with app.app_context():
        create_tables()
    print("🚀 Database initialized successfully!")
