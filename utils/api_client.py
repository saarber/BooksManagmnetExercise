import requests
#Uses the https://github.com/LBS720/library-management-api/blob/main/python/app.py API under the assumption it runs in flask
BASE_URL = "http://127.0.0.1:5000"

class LibraryClient:
    def get_books(self):
        return requests.get(f"{BASE_URL}/books")

    def add_book(self, data):
        return requests.post(f"{BASE_URL}/books", json=data)

    def update_book(self, book_id, data):
        return requests.put(f"{BASE_URL}/books/{book_id}", json=data)

    def delete_book(self, book_id):
        return requests.delete(f"{BASE_URL}/books/{book_id}")

    def get_users(self):
        return requests.get(f"{BASE_URL}/users")

    def borrow_book(self, user_id, book_id):
        return requests.post(f"{BASE_URL}/users/{user_id}/borrow/{book_id}")

    def return_book(self, user_id, book_id):
        return requests.post(f"{BASE_URL}/users/{user_id}/return/{book_id}")
