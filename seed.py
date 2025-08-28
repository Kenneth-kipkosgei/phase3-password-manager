#!/usr/bin/env python3
from models import session, Category

def seed_categories():
    """Seed initial categories"""
    categories = [
        ("Social Media", "Facebook, Twitter, Instagram, etc."),
        ("Email", "Gmail, Yahoo, Outlook, etc."),
        ("Banking", "Online banking and financial services"),
        ("Work", "Work-related accounts"),
        ("Entertainment", "Netflix, Spotify, Gaming, etc.")
    ]
    
    for name, description in categories:
        if not session.query(Category).filter_by(name=name).first():
            category = Category(name=name, description=description)
            session.add(category)
    
    session.commit()
    print("Categories seeded successfully!")

if __name__ == "__main__":
    seed_categories()