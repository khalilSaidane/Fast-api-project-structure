from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core import settings

engine = create_engine(
    settings.TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)