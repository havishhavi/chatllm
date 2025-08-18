from app.utils.validators import sanitize_input

def test_sanitize_valid():
    assert sanitize_input("Hello, how are you?") == "Hello, how are you?"

def test_sanitize_special_characters():
    assert sanitize_input("DROP TABLE users; --") == "DROP TABLE users "

def test_sanitize_none():
    assert sanitize_input(None) == ""

def test_sanitize_int():
    assert sanitize_input(1234) == ""