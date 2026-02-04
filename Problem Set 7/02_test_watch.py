from watch import parse


def test_valid():
    assert parse("https://www.youtube.com/watch?v=dQw4w9WgXcQ") == "https://youtu.be/dQw4w9WgXcQ"
    assert parse("http://youtube.com/watch?v=abc123") == "https://youtu.be/abc123"


def test_invalid():
    assert parse("https://www.youtube.com/watch?v=") is None
    assert parse("https://youtu.be/dQw4w9WgXcQ") is None
    assert parse("https://www.youtube.com/") is None
    assert parse("cat") is None
