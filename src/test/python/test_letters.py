from src.main.python import callsign


#
# Test first letters
#
def test_first_letter_1():
    assert callsign.getFirstLetter(1) == "A"


def test_first_letter_2():
    assert callsign.getFirstLetter(2) == "K"


def test_first_letter_3():
    assert callsign.getFirstLetter(3) == "N"


def test_first_letter_4():
    assert callsign.getFirstLetter(4) == "W"


#
# Test letters
#
def test_letter_01():
    assert callsign.getLetter(1) == "A"


def test_letter_02():
    assert callsign.getLetter(2) == "B"


def test_letter_03():
    assert callsign.getLetter(3) == "C"


def test_letter_04():
    assert callsign.getLetter(4) == "K"


def test_letter_05():
    assert callsign.getLetter(5) == "N"


def test_letter_06():
    assert callsign.getLetter(6) == "W"


def test_get_suffix_count():
    for i in range(1, 50):
        val = callsign.get_suffix_count()
        if val < 1 or val > 3:
            assert val == 0


def test_get_prefix_count():
    for i in range(1, 50):
        val = callsign.get_prefix_count()
        if val < 1 or val > 2:
            assert val == 0


# TODO remove test
def test_arrays():
    str = "abc"
    # convert string to array
    one = list(str)
    two = ['a','b','c']
    print(one)
    assert one == two

    str2 = ""
    for ele in two:
        str2 += ele
    print("str2 = "+str2)
    assert str == str2

    print("str2:")
    for ele in str2:
        print(ele)
