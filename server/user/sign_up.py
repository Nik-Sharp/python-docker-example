from app import app, engine
from user import does_user_exist
from fastapi import HTTPException
from util import encrypt_password
import sqlalchemy as sqla

@app.post("/sign-up")
def sign_up(username, password):
    if does_user_exist(username):
        raise HTTPException(status_code = 409, detail="User already exists")
    encrypted_password = encrypt_password(password, username)
    with engine.connect() as conn:
        conn.execute(sqla.text(f"INSERT INTO users (username, password) VALUES ('{username}', '{encrypted_password}')"))
    return {"result": "Account Created"}
    