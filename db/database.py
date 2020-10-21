from sqlalchemy import create_engine, engine_from_config
from sqlalchemy.orm import sessionmaker
from core import settings

engine = create_engine(str(settings.DATABASE_URL),  connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
