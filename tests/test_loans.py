def test_borrow_and_return_flow(client):
    book_id = client.add_book({"title": "borrow-me", "author": "X"}).json()["id"]
    user_id = 1
    borrow = client.borrow_book(user_id, book_id)
    assert borrow.status_code == 200
    return_ = client.return_book(user_id, book_id)
    assert return_.status_code == 200
    client.delete_book(book_id)

def test_borrow_book_already_borrowed(client):
    book_id = client.add_book({"title": "double", "author": "Y"}).json()["id"]
    user1, user2 = 1, 2
    assert client.borrow_book(user1, book_id).status_code == 200
    r = client.borrow_book(user2, book_id)
    assert r.status_code == 400
    client.return_book(user1, book_id)
    client.delete_book(book_id)

def test_return_book_not_borrowed_by_user(client):
    book_id = client.add_book({"title": "not-mine", "author": "Z"}).json()["id"]
    user_id = 1
    r = client.return_book(user_id, book_id)
    assert r.status_code == 400
    client.delete_book(book_id)
