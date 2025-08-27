from cryptography.fernet import Fernet
import os

KEY_FILE = 'data/key.key'

def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)

def load_key():
    with open(KEY_FILE, 'rb') as f:
        return f.read()

def encrypt_password(password):
    key = load_key()
    return Fernet(key).encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    key = load_key()
    return Fernet(key).decrypt(encrypted_password.encode()).decode()
