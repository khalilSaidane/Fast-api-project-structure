import pathlib
from typing import Optional

from pydantic import BaseModel
from core.settings import BASE_DIR

class Database(BaseModel):
    dialect: str
    driver: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    host: Optional[str] = None
    port: Optional[int] = None
    database: str

    def get_url(self):
        if self.dialect == "sqlite":
            url = self.dialect + ":///" + BASE_DIR + '/' + self.database + '.db'
            return url
        else:
            url = "{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}"
            if not self.driver:
                url.replace('+', '')
                url = url.format(
                    dialect=self.dialect,
                    driver=self.driver,
                    username=self.username,
                    password=self.password,
                    host=self.host,
                    port=self.port,
                    database=self.database
                )
            return url

    def get_connect_args(self):
        if self.dialect == 'sqlite':
            return {"check_same_thread": False}
