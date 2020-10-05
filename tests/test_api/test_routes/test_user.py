from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_user():
    response = client.post(
        "/v2/users/",
        json={
            "email": "khalil.saidane@gmail.tn",
            "password": "123"
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "email": "khalil.saidane@gmail.tn",
        "id": 6,
        "is_active": True,
        "items": [
            {
                "title": "string",
                "description": "string",
                "id": 0,
                "owner_id": 0
            }
        ]
    }
