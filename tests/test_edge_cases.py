def test_duplicate_isbn_should_fail(client):
    body = {"title": "dup", "author": "A", "isbn": "123"}
    first = client.add_book(body)
    assert first.status_code == 201
    second = client.add_book(body)
    assert second.status_code == 400

def test_partial_update_keeps_fields(client):
    book = client.add_book({"title": "keep", "author": "stay"}).json()
    bid = book["id"]
    client.update_book(bid, {"title": "changed"})
    latest = next(b for b in client.get_books().json() if b["id"] == bid)
    assert latest["author"] == "stay"
    client.delete_book(bid)

def test_delete_loaned_book_should_fail(client):
    bid = client.add_book({"title": "lock", "author": "A"}).json()["id"]
    client.borrow_book(1, bid)
    r = client.delete_book(bid)
    assert r.status_code in (400, 409)
    client.return_book(1, bid)
    client.delete_book(bid)
