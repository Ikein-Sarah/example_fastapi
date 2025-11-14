from fastapi.testclient import TestClient
from app.main import app
import pytest
from app import schemas
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.database import get_db, Base



DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
else:
    DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"

# Other environment variables
SECRET_KEY = os.environ.get("SECRET_KEY", "hello123")
ALGORITHM = os.environ.get("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))


engine= create_engine(DATABASE_URL)

TestingSessionLocal= sessionmaker(autocommit=False, autoflush=False, bind= engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind= engine)
    Base.metadata.create_all(bind= engine)
    db=TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
    
     try:
         yield session
     finally:
         session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)