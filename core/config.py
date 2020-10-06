from functools import lru_cache
from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Catalogapi"
    prefix: str = "/v2"
    database_url: str
    secret_key: str
    allowed_hosts: List[str] = []
    debug: bool = True
    version: str = "0.0.0"
    valid_requestor_ids = ['test']

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache()
def get_settings():
    return Settings()
