from twttr import shorten

def test_lowercase_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"
    assert shorten("computer") == "cmptr"

def test_uppercase_vowels():
    assert shorten("HELLO") == "HLL"
    assert shorten("EMAIL") == "ML"
    assert shorten("TWITTER") == "TWTTR"

def test_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"
    assert shorten("HeLLo") == "HLL"

def test_no_vowels():
    assert shorten("rhythm") == "rhythm"
    assert shorten("crypt") == "crypt"

def test_only_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("aEiOuAEIOU") == ""

def test_symbols_and_numbers():
    assert shorten("CS50!") == "CS50!"
    assert shorten("123abc") == "123bc"
    assert shorten("hello123") == "hll123"

def test_empty_string():
    assert shorten("") == ""

def test_punctuation():
    assert shorten("h.e.l.l.o") == "h..l.l."
    assert shorten("a!e?i,o.u") == "!?,."
