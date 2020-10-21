import os
import databases
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

config = Config(".env")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = config('DEBUG', cast=bool, default=True)
TESTING = config('TESTING', cast=bool, default=False)

SECRET_KEY = config('SECRET_KEY', cast=Secret)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=CommaSeparatedStrings)
APP_NAME = "Catalogapi"
PREFIX = "/v2"
VERSION = "0.1.0"

REQUESTER_ID_TEST = "test"

DATABASE_URL = config('DATABASE_URL', cast=databases.DatabaseURL)
if TESTING:
    DATABASE_URL = DATABASE_URL.replace(database='test_' + DATABASE_URL.database)
db_config = {
    "pool_size": 20, "max_overflow": 0
}
