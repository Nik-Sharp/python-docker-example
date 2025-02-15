from app import app, engine
from util import decrypt_jwt
from user import does_user_exist, get_token, password_correct
from fastapi import HTTPException
from util import encrypt_password
import sqlalchemy as sqla

@app.post("/get_tasks")
def get_tasks(token):
    username = decrypt_jwt(token)["username"]
    if not does_user_exist(username):
        raise HTTPException(status_code = 409, detail="User does not exist")
    with engine.connect() as conn:
        result = conn.execute(sqla.text(f"SELECT * from tasks WHERE username='{username}'"))
        # TODO: fix return value
        return result.all()
    