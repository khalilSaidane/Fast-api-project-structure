import pytest
from starlette.testclient import TestClient

from api.dependencies.database import get_db
from main import app
from models.models import Base
from test.utils.overrides import override_get_db
from test.utils.test_db import engine

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="session")
def app_client():
    Base.metadata.create_all(bind=engine)

    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)
