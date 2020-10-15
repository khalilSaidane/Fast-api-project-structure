from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core import settings
from db.utils import Database

database = Database(**settings.DATABASES['default'])
engine = create_engine(
    database.get_url(), connect_args=database.get_connect_args()
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
