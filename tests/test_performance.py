import time

def test_create_100_books_under_three_seconds(client):
    payloads = [{"title": f"bulk{i}", "author": "perf"} for i in range(100)]
    start = time.time()
    for p in payloads:
        assert client.add_book(p).status_code == 201
    assert time.time() - start < 3.0
    for b in client.get_books().json():
        if str(b["title"]).startswith("bulk"):
            client.delete_book(b["id"])
