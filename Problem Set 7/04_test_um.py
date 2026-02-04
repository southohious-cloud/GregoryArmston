from um import count


def test_basic():
    assert count("Um, thanks") == 1
    assert count("um? um! UM.") == 3


def test_embedded():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrella") == 0


def test_spacing():
    assert count("um um um") == 3
    assert count(" um ") == 1
