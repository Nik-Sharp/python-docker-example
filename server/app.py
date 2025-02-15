from fastapi import FastAPI
import sqlalchemy as sqla
app = FastAPI()
url = sqla.URL.create(
    "postgresql+psycopg",
    username="postgres",
    password="example",
    host="db",
    port=5432,
    database="postgres"
)
engine = sqla.create_engine(url)

@app.get("/")
async def root():
    with engine.connect() as conn:
        return {"message": str(conn.execute(sqla.text("SELECT * from users")).all())}
