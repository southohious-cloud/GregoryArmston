from bank import value

def test_hello_variants():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0
    assert value("Hello, friend") == 0

def test_h_variants():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("hola") == 20
    assert value("howdy") == 20
    assert value("Hi there") == 20

def test_other_greetings():
    assert value("good morning") == 100
    assert value("yo") == 100
    assert value("sup") == 100
    assert value("greetings") == 100

def test_case_insensitivity():
    assert value("HELLO") == 0
    assert value("hElLo") == 0
    assert value("Hi") == 20
    assert value("HEY") == 20

def test_whitespace_handling():
    assert value("   hello") == 0
    assert value("hello   ") == 0
    assert value("   hi   ") == 20
    assert value("  good morning  ") == 100
