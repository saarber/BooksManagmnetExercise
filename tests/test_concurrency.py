import threading

def test_simultaneous_borrow_only_one_succeeds(client):
    bid = client.add_book({"title": "race", "author": "R"}).json()["id"]
    results = []

    def attempt(uid):
        results.append(client.borrow_book(uid, bid).status_code)

    t1 = threading.Thread(target=attempt, args=(1,))
    t2 = threading.Thread(target=attempt, args=(2,))
    t1.start(); t2.start(); t1.join(); t2.join()
    assert sorted(results) == [200, 400] or sorted(results) == [200, 409]
    if 200 in results:
        succ_user = 1 if results[0] == 200 else 2
        client.return_book(succ_user, bid)
    client.delete_book(bid)
