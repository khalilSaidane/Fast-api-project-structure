import os

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

config = Config(".env")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = config('DEBUG', cast=bool, default=True)
DATABASE_URL = config('DATABASE_URL')
SECRET_KEY = config('SECRET_KEY', cast=Secret)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=CommaSeparatedStrings)
APP_NAME = "Catalogapi"
PREFIX = "/v2"
VERSION = "0.0.0.0"
REQUESTER_ID_TEST = "test"
TEST_DATABASE_URL = "sqlite:///./test.db"

DATABASES = {
    "default": {
        "dialect": "sqlite",
        "driver": "",
        "username": "",
        "password": "",
        "host": "",
        "port": None,
        "database": "newdb",
    },
    "test": {
        "dialect": "sqlite",
        "database": "test",
    }
}