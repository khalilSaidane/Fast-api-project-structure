from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core import settings
from db.utils import Database

test_database = Database(**settings.DATABASES.get("test"))
engine = create_engine(
    test_database.get_url(), connect_args=test_database.get_connect_args()
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)