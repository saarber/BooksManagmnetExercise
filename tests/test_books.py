def test_get_books_returns_list(client):
    r = client.get_books()
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_add_book_and_delete(client):
    payload = {"title": "pytest-book", "author": "QA", "year": 2025}
    add = client.add_book(payload)
    assert add.status_code == 201
    book_id = add.json()["id"]
    delete = client.delete_book(book_id)
    assert delete.status_code == 200

def test_add_book_missing_title_fails(client):
    r = client.add_book({"author": "NoTitle"})
    assert r.status_code == 400

def test_update_book_success(client):
    new = client.add_book({"title": "to-update", "author": "me"}).json()
    bid = new["id"]
    up = client.update_book(bid, {"title": "updated"})
    assert up.status_code == 200
    assert up.json()["title"] == "updated"
    client.delete_book(bid)

def test_update_nonexistent_book_404(client):
    r = client.update_book(99999, {"title": "ghost"})
    assert r.status_code == 404
