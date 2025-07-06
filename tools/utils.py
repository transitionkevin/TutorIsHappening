import re
import bcrypt

def is_valid_email(email):
    # Simple regex pattern for basic email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

def hash_password(password):
    # Convert the password to bytes
    password_bytes = password.encode('utf-8')
    # Generate salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed
