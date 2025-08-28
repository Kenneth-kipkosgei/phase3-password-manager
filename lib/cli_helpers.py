def validate_input(prompt: str, min_length: int = 1) -> str:
    """Validate user input with minimum length requirement"""
    while True:
        user_input = input(prompt).strip()
        if len(user_input) >= min_length:
            return user_input
        print(f"Input must be at least {min_length} characters long.")

def get_user_choice(options: list, prompt: str) -> tuple:
    """Get user choice from a list of options"""
    print(f"\n{prompt}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(options):
                return choice - 1, options[choice - 1]
            print(f"Please enter a number between 1 and {len(options)}")
        except ValueError:
            print("Please enter a valid number")