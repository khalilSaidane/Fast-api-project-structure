def test_create_user(app_client):
    response = app_client.post(
        "/v2/users/",
        json={"email": "newemail@gmail.com", "password": "123123"},
        headers={'requester-id': "test"}
    )
    assert response.status_code == 200, response.text
    assert response.json() == {"email": "newemail@gmail.com", "id": 1, "is_active": True, "items": []}


def test_read_user(app_client):
    response = app_client.get(
        "/v2/users/1",
        headers={'requester-id': "test"}
    )
    assert response.status_code == 200
    assert response.json() == {"email": "newemail@gmail.com", "id": 1, "is_active": True, "items": []}


def test_read_all_users(app_client):
    response = app_client.get(
        "/v2/users/",
        headers={'requester-id': "test"}
    )
    assert response.status_code == 200
    assert response.json() == [
        {"email": "newemail@gmail.com", "id": 1, "is_active": True, "items": []}
    ]
