from working import convert
import pytest


def test_basic():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_with_minutes():
    assert convert("9:30 AM to 5:15 PM") == "09:30 to 17:15"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"


def test_invalid():
    with pytest.raises(ValueError):
        convert("9 to 5")
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9:72 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("cat")
