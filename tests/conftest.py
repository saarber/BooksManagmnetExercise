import pytest
from utils.api_client import LibraryClient

@pytest.fixture(scope="module")
def client():
    return LibraryClient()
