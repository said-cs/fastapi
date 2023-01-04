from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2 as psy
import time
from psycopg2.extras import RealDictCursor
from .config import settings


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psy.connect(host='localhost', database='fastapi', user='said', password='2906', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successsful")
#         break
#     except Exception as error:
#         print("Connection to database failed")
#         print("Error was: ", error)
#         time.sleep(2)
