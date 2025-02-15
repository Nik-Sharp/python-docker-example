from app import app, engine
from user import does_user_exist, get_token, password_correct
from fastapi import HTTPException
from util import encrypt_password
import sqlalchemy as sqla

@app.post("/log_in")
def log_in(username, password):
    if password_correct(username, password):
        raise HTTPException(status_code = 409, detail="Incorrect username or password")
    token = get_token(username)

    return token
    