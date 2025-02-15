from datetime import date, timedelta
from app import app, engine
from util import decrypt_jwt
from user import does_user_exist, get_token, password_correct
from fastapi import HTTPException
from util import encrypt_password
import sqlalchemy as sqla

# TODO: error handlign
@app.post("/get_streak")
def get_streak(token):
    username = decrypt_jwt(token)["username"]
    if not does_user_exist(username):
        raise HTTPException(status_code = 409, detail="User does not exist")
    with engine.connect() as conn:
        query = "SELECT start_date, end_date FROM streaks WHERE username = :username"
        result = conn.execute(sqla.text(query), {"username": username}).fetchone()
        
        if result:
            start_date, end_date = result
            
            if end_date == date.today() - timedelta(days=1):
                end_date = date.today()
            elif end_date < date.today() - timedelta(days=1):
                start_date = date.today()
                end_date = date.today()
            
            update_query = """
            UPDATE streaks 
            SET start_date = :start_date, end_date = :end_date 
            WHERE username = :username
            """
            conn.execute(sqla.text(update_query), {"start_date": start_date, "end_date": end_date, "username": username})
            
            return int(end_date - start_date)

        