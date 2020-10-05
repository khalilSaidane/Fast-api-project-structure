from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import get_settings

Base = declarative_base()


def get_db():
    settings = get_settings()
    engine = create_engine(
        settings.database_url, connect_args={"check_same_thread": False}
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    print(db)
    try:
        yield db
    finally:
        db.close()
