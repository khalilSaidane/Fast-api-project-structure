import pytest

from test.utils.vcr_helper import vcr
import requests
from urllib.request import urlopen


def test_create_user(client):
    response = client.post(
        "/v2/users/",
        json={"email": "newemail@gmail.com", "password": "123123"},
        headers={'requester-id': "test"}
    )
    assert response.status_code == 200, response.text
    assert response.json() == {"email": "newemail@gmail.com", "id": 1, "is_active": True, "items": []}


def test_read_user(client):
    response = client.get(
        "/v2/users/1",
        headers={'requester-id': "test"}
    )
    assert response.status_code == 200
    assert response.json() == {"email": "newemail@gmail.com", "id": 1, "is_active": True, "items": []}


def test_read_all_users(client):
    response = client.get(
        "/v2/users/",
        headers={'requester-id': "test"}
    )
    assert response.status_code == 200
    assert response.json() == [
        {"email": "newemail@gmail.com", "id": 1, "is_active": True, "items": []}
    ]


@vcr.use_cassette()
def test_do_nothing():
    print("Doing nothing")
    resp = requests.get("https://reqres.in/api/users")

    assert resp.status_code == 200


# @vcr.use_cassette()
# def test_iana():
#     response = urlopen('http://www.iana.org/domains/reserved').read()
#     assert 'Example domains' in response
