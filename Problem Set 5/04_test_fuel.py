import pytest
from fuel import convert, gauge

# -------------------------
# Tests for convert()
# -------------------------

def test_convert_valid_fractions():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("99/100") == 99

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("3/")
    with pytest.raises(ValueError):
        convert("/4")
    with pytest.raises(ValueError):
        convert("five/ten")

def test_convert_out_of_range():
    with pytest.raises(ValueError):
        convert("5/4")      # numerator > denominator
    with pytest.raises(ValueError):
        convert("-1/2")     # negative numerator
    with pytest.raises(ValueError):
        convert("1/-2")     # negative denominator

# -------------------------
# Tests for gauge()
# -------------------------

def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_middle_values():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(73) == "73%"

if __name__ == "__main__":
    main()
