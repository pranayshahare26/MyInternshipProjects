import random
import string

def generate_password(length=12):

    # Define char sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Create all char
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# User input
password_length = int(input("Enter desired password length: "))
num_passwords = int(input("Enter number of passwords to generate: "))

passwords = [generate_password(password_length) for _ in range(num_passwords)]

# Print generated passwords
print(f"Generated Passwords:")
for password in passwords:
    print(password)
