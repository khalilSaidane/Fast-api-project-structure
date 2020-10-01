from functools import lru_cache
from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Catalogapi"
    prefix: str = "v2"
    database_url: str
    allowed_hosts: List[str] = []

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache()
def get_settings():
    return Settings()
