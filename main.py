from fastapi import FastAPI
from models import Base, Admins
from database import engine
import psycopg2
from psycopg2.extras import RealDictCursor
from auth import auth_routher
from admin import admin_router

Base.metadata.create_all(bind=engine)
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="password",
    database="online_store",
    cursor_factory=RealDictCursor
    )

cursor = conn.cursor()

app = FastAPI()

app.include_router(auth_routher)
app.include_router(admin_router)
