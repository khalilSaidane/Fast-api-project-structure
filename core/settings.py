from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

config = Config(".env")

DEBUG = config('DEBUG', cast=bool, default=True)
DATABASE_URL = config('DATABASE_URL')
SECRET_KEY = config('SECRET_KEY', cast=Secret)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=CommaSeparatedStrings)
APP_NAME = "Catalogapi"
PREFIX = "/v2"
VERSION = "0.0.0.0"
REQUESTER_ID_TEST = "test"
