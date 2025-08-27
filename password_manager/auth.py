import json
import os
from password_manager.models import User

DATA_FILE = 'data/database.json'

def load_users():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(DATA_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def register(username, password):
    users = load_users()
    if username in users:
        return False  # User exists
    users[username] = {'password': password, 'credentials': []}
    save_users(users)
    return True

def login(username, password):
    users = load_users()
    user_data = users.get(username)
    if not user_data:
        return None
    if user_data['password'] != password:
        return None
    return User(username, password)
