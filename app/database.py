import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings


#SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

# Database configuration
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
else:
    DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

# Other environment variables
SECRET_KEY = os.environ.get("SECRET_KEY", "hello123")
ALGORITHM = os.environ.get("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))


engine= create_engine(DATABASE_URL)

SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind= engine)

Base= declarative_base()


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


#while True:
    #try:
        #conn= psycopg2.connect(host= 'localhost', database='fastapi', 
                               #user= 'postgres', password= "1326", cursor_factory= RealDictCursor)
        #cursor= conn.cursor()
        #print("Database connection was successful")
        #break
    #except Exception as error:
        #print("connecting to database failed")
        #print("Error: ", error)
        #time.sleep(2)