from fastapi import FastAPI
import sqlalchemy as sqla
from app import engine
from util import encrypt_password
from PyJWT import jwt
def does_user_exist(username: str):
    with engine.connect() as conn:
        result = conn.execute(sqla.text(f"SELECT * from users WHERE username='{username}'"))
        # spaghetti
        for value in result:
            return True
        return False
def password_correct(username: str, password: str):
    encrypted_password = encrypt_password(password, username)
    with engine.connect() as conn:
        result = conn.execute(sqla.text(f"SELECT * from users WHERE username='{username}' AND password='{encrypted_password}'"))
        # spaghetti
        for value in result:
            return True
        return False
def get_token(username: str):
    # JWT token with username as payload
    # TODO: Add expiration and change secret
    return jwt.encode({"username": username}, "secret", algorithm="HS256")