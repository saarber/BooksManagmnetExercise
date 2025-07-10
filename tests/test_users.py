def test_get_users_success(client):
    r = client.get_users()
    assert r.status_code == 200
    assert isinstance(r.json(), list)
