from src.main.python import callsign

AUDIO_LOCN_BASE = "../../main/resource/"

#
# Test first letters
#
def test_first_letter_1():
    assert callsign.getFirstLetter(1) == "alpha"

def test_first_letter_2():
    assert callsign.getFirstLetter(2) == "kilo"

def test_first_letter_3():
    assert callsign.getFirstLetter(3) == "november"

def test_first_letter_4():
    assert callsign.getFirstLetter(4) == "whiskey"

#
# Test letters
#
def test_letter_01():
    assert callsign.getLetter(1) == "alpha"

def test_letter_02():
    assert callsign.getLetter(2) == "bravo"

def test_letter_03():
    assert callsign.getLetter(3) == "charlie"

def test_letter_04():
    assert callsign.getLetter(4) == "kilo"

def test_letter_05():
    assert callsign.getLetter(5) == "november"

def test_letter_06():
    assert callsign.getLetter(6) == "whiskey"
