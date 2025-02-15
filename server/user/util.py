import bcrypt
from PyJWT import jwt
def encrypt_password(username, password):
    return bcrypt.hashpw(password, username)

def decrypt_jwt(token):
    return jwt.decode(token, "secret", algorithms=["HS256"])
