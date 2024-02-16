from app import data

def test_return_check():
    assert data.return_check() == b'Hello, World!'
