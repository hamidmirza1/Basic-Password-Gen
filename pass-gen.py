import secrets
import string

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for i in range(length))

password_length = 12
random_password = generate_password(password_length)
print(f"Generated password: {random_password}")
