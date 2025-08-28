#!/usr/bin/env python3
import click
from models import session, User, Category, Password
from lib import encrypt_password, decrypt_password, validate_input, get_user_choice

class PasswordManager:
    def __init__(self):
        self.current_user = None
        self.master_password = None

    def register_user(self):
        """Register a new user"""
        print("\n=== User Registration ===")
        username = validate_input("Enter username: ", 3)
        
        if session.query(User).filter_by(username=username).first():
            print("Username already exists!")
            return False
            
        master_password = validate_input("Enter master password: ", 6)
        
        user = User(username=username, master_password=master_password)
        session.add(user)
        session.commit()
        print(f"User '{username}' registered successfully!")
        return True

    def login(self):
        """Login user"""
        print("\n=== Login ===")
        username = validate_input("Enter username: ")
        master_password = validate_input("Enter master password: ")
        
        user = session.query(User).filter_by(username=username, master_password=master_password).first()
        if user:
            self.current_user = user
            self.master_password = master_password
            print(f"Welcome back, {username}!")
            return True
        print("Invalid credentials!")
        return False

    def add_password(self):
        """Add a new password"""
        print("\n=== Add Password ===")
        site_name = validate_input("Enter site name: ")
        username = validate_input("Enter username: ")
        password = validate_input("Enter password: ")
        
        categories = session.query(Category).all()
        if categories:
            category_names = [cat.name for cat in categories]
            idx, _ = get_user_choice(category_names + ["No category"], "Select category:")
            category_id = categories[idx].id if idx < len(categories) else None
        else:
            category_id = None
        
        encrypted_pwd = encrypt_password(password, self.master_password)
        
        pwd_entry = Password(
            site_name=site_name,
            username=username,
            encrypted_password=encrypted_pwd,
            user_id=self.current_user.id,
            category_id=category_id
        )
        session.add(pwd_entry)
        session.commit()
        print("Password added successfully!")

    def view_passwords(self):
        """View all passwords"""
        passwords = session.query(Password).filter_by(user_id=self.current_user.id).all()
        
        if not passwords:
            print("No passwords found!")
            return
            
        print("\n=== Your Passwords ===")
        password_data = []
        for pwd in passwords:
            decrypted = decrypt_password(pwd.encrypted_password, self.master_password)
            category_name = pwd.category.name if pwd.category else "No category"
            password_data.append({
                'site': pwd.site_name,
                'username': pwd.username,
                'password': decrypted,
                'category': category_name
            })
        
        for i, data in enumerate(password_data, 1):
            print(f"{i}. Site: {data['site']}, User: {data['username']}, "
                  f"Password: {data['password']}, Category: {data['category']}")

    def add_category(self):
        """Add a new category"""
        print("\n=== Add Category ===")
        name = validate_input("Enter category name: ")
        description = input("Enter description (optional): ").strip()
        
        if session.query(Category).filter_by(name=name).first():
            print("Category already exists!")
            return
            
        category = Category(name=name, description=description)
        session.add(category)
        session.commit()
        print("Category added successfully!")

    def run(self):
        """Main CLI loop"""
        print("Welcome to Password Manager!")
        
        while True:
            if not self.current_user:
                options = ["Login", "Register", "Exit"]
                choice, _ = get_user_choice(options, "Choose an option:")
                
                if choice == 0:
                    if self.login():
                        continue
                elif choice == 1:
                    self.register_user()
                else:
                    break
            else:
                options = ["Add Password", "View Passwords", "Add Category", "Logout"]
                choice, _ = get_user_choice(options, "Choose an option:")
                
                if choice == 0:
                    self.add_password()
                elif choice == 1:
                    self.view_passwords()
                elif choice == 2:
                    self.add_category()
                else:
                    self.current_user = None
                    self.master_password = None
                    print("Logged out successfully!")

@click.command()
def main():
    """Password Manager CLI"""
    pm = PasswordManager()
    pm.run()

if __name__ == "__main__":
    main()