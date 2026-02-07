from seasons import minutes_lived
from datetime import date
import pytest

def test_valid_date():
    # Fixed date to make the test deterministic
    dob = "2000-01-01"
    today = date.today()
    delta = today - date(2000, 1, 1)
    expected = delta.days * 24 * 60
    assert minutes_lived(dob) == expected

def test_invalid_format():
    with pytest.raises(SystemExit):
        minutes_lived("January 1, 2000")

def test_invalid_month():
    with pytest.raises(SystemExit):
        minutes_lived("2000-13-01")

def test_invalid_day():
    with pytest.raises(SystemExit):
        minutes_lived("2000-02-31")

def test_future_date():
    future = f"{date.today().year + 1}-01-01"
    with pytest.raises(SystemExit):
        minutes_lived(future)
