# Phase 3 Password Manager

A secure command-line password manager built with Python, SQLAlchemy, and encryption.

## Features

- User registration and authentication
- Encrypted password storage
- Password categorization
- Secure master password-based encryption
- SQLAlchemy ORM with Alembic migrations
- Interactive CLI interface

## Installation

1. Clone the repository
2. Create virtual environment: `python3 -m venv venv`
3. Activate virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install sqlalchemy alembic click cryptography`
5. Run migrations: `./venv/bin/alembic upgrade head`
6. Seed categories: `python3 seed.py`

## Usage

Run the password manager:
```bash
python3 cli.py
CLI Workflow
Main Menu (Not Logged In)
Login - Login with existing credentials

Register - Create new user account

Exit - Exit the application

Main Menu (Logged In)
Add Password - Store a new password entry

View Passwords - Display all stored passwords

Add Category - Create new password category

Logout - Return to login screen

Functions
User Management
register_user() - Creates new user with username and master password

login() - Authenticates user and starts session

Password Management
add_password() - Encrypts and stores new password with site, username, and category

view_passwords() - Decrypts and displays all user passwords

Category Management
add_category() - Creates new password categories for organization

Security Functions
encrypt_password() - Encrypts passwords using master password

decrypt_password() - Decrypts passwords for viewing

generate_key() - Creates encryption key from master password

Utility Functions
validate_input() - Validates user input with minimum length requirements

get_user_choice() - Presents menu options and handles user selection

Database Schema
Users Table
id - Primary key

username - Unique username

master_password - Master password for encryption

created_at - Account creation timestamp

Categories Table
id - Primary key

name - Category name (unique)

description - Category description

Passwords Table
id - Primary key

site_name - Website/service name

username - Account username

encrypted_password - Encrypted password

user_id - Foreign key to users table

category_id - Foreign key to categories table

created_at - Entry creation timestamp

Security Features
Passwords encrypted using Fernet symmetric encryption

Master password-based key derivation using PBKDF2

No plain text password storage

User input validation

Dependencies
SQLAlchemy - ORM for database operations

Alembic - Database migration management

Click - CLI framework

Cryptography - Password encryption/decryption

License
MIT License

Copyright (c) 2025 Kenneth Kipkosgei
