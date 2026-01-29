from plates import is_valid

def test_valid_examples():
    assert is_valid("CS50") is True
    assert is_valid("HELLO") is True
    assert is_valid("WORLD1") is True
    assert is_valid("AB123") is True

def test_length_rules():
    assert is_valid("A") is False          # too short
    assert is_valid("ABCDEFG") is False    # too long
    assert is_valid("AB") is True          # minimum valid
    assert is_valid("ABCDEF") is True      # maximum valid

def test_starts_with_two_letters():
    assert is_valid("A1") is False
    assert is_valid("1A") is False
    assert is_valid("12AB") is False
    assert is_valid("AB") is True
    assert is_valid("XY123") is True

def test_numbers_only_at_end():
    assert is_valid("CS50P") is False      # number in middle
    assert is_valid("AB1C") is False       # number then letter
    assert is_valid("AAA22") is True
    assert is_valid("AB123") is True

def test_first_number_not_zero():
    assert is_valid("AB0") is False
    assert is_valid("AB01") is False
    assert is_valid("AB10") is True
    assert is_valid("XY05") is False

def test_alphanumeric_only():
    assert is_valid("PI3.14") is False
    assert is_valid("HELLO!") is False
    assert is_valid("GOOD-BYE") is False
    assert is_valid("CS50") is True



def test_edge_cases():
    assert is_valid("AA0") is False        # zero cannot be first digit
    assert is_valid("A1A") is False        # number in middle
    assert is_valid("AAA222") is True
    assert is_valid("AB999") is True
