def test_has_permission(client):
    response = client.get("/v2/users", headers={"requester-id": "test"})
    assert response.status_code == 200


def test_no_permission(client):
    response = client.get("/v2/users")
    assert response.status_code == 403
    assert response.json() == {
        "detail": "Not authenticated"
    }
