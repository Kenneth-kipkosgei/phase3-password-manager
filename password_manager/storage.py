from password_manager.encryption import encrypt_password, decrypt_password
from password_manager.auth import load_users, save_users

def add_credential(user, site, username, password):
    users = load_users()
    encrypted_pw = encrypt_password(password)
    users[user.username]['credentials'].append({
        'site': site,
        'username': username,
        'password': encrypted_pw
    })
    save_users(users)

def list_credentials(user):
    users = load_users()
    creds = users[user.username]['credentials']
    return [
        {
            'site': c['site'],
            'username': c['username'],
            'password': decrypt_password(c['password'])
        } for c in creds
    ]
