from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(master_password: str) -> bytes:
    """Generate encryption key from master password"""
    key = hashlib.pbkdf2_hmac('sha256', master_password.encode(), b'salt', 100000)
    return base64.urlsafe_b64encode(key)

def encrypt_password(password: str, master_password: str) -> str:
    """Encrypt password using master password"""
    key = generate_key(master_password)
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password: str, master_password: str) -> str:
    """Decrypt password using master password"""
    key = generate_key(master_password)
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()