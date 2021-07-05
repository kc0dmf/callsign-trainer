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


def test_callsign_generation():
    callA = False
    callAX = False
    callK = False
    callKX = False
    callN = False
    callNX = False
    callW = False
    callWX = False
    call1x1 = False
    call1x2 = False
    call1x3 = False
    call2x1 = False
    call2x2 = False
    call2x3 = False

    print("")
    for i in range(1, 50):
        call = callsign.randomize_callsign()
        print(call)
        callarray = list(call)
        leng = len(call)
        print("leng is " + str(leng))

        # find digit
        cnt = 0
        pos = 0
        for i in range(0, leng):
            if str(callarray[i]).isdigit():
                cnt += 1
                pos = i

        if cnt < 1 or cnt > 1:
            # not the right number of digits
            assert cnt == 1

        print ("pos is " + str(pos))
        if pos == 1 and leng == 3:
            call1x1 = True
            print("-- call1x1")
            if callarray[0] == "A":
                callA = True
                print("-- callA")
            elif callarray[0] == "K":
                callK = True
                print("-- callK")
            elif callarray[0] == "N":
                callN = True
                print("-- callN")
            elif callarray[0] == "W":
                callW = True
                print("-- callW")
        elif pos == 1 and leng == 4:
            call1x2 = True
            print("-- call1x2")
            if callarray[0] == "A":
                callA = True
                print("-- callA")
            elif callarray[0] == "K":
                callK = True
                print("-- callK")
            elif callarray[0] == "N":
                callN = True
                print("-- callN")
            elif callarray[0] == "W":
                callW = True
                print("-- callW")
        elif pos == 1 and leng == 5:
            call1x3 = True
            print("-- call1x3")
            if callarray[0] == "A":
                callA = True
                print("-- callA")
            elif callarray[0] == "K":
                callK = True
                print("-- callK")
            elif callarray[0] == "N":
                callN = True
                print("-- callN")
            elif callarray[0] == "W":
                callW = True
                print("-- callW")
        elif pos == 2 and leng == 4:
            call2x1 = True
            print("-- call2x1")
            if callarray[0] == "A":
                callAX = True
                print("-- callAX")
            elif callarray[0] == "K":
                callKX = True
                print("-- callKX")
            elif callarray[0] == "N":
                callNX = True
                print("-- callNX")
            elif callarray[0] == "W":
                callWX = True
                print("-- callWX")
        elif pos == 2 and leng == 5:
            call2x2 = True
            print("-- call2x2")
            if callarray[0] == "A":
                callAX = True
                print("-- callAX")
            elif callarray[0] == "K":
                callKX = True
                print("-- callKX")
            elif callarray[0] == "N":
                callNX = True
                print("-- callNX")
            elif callarray[0] == "W":
                callWX = True
                print("-- callWX")
        elif pos == 2 and leng == 6:
            call2x3 = True
            print("-- call2x3")
            if callarray[0] == "A":
                callAX = True
                print("-- callAX")
            elif callarray[0] == "K":
                callKX = True
                print("-- callKX")
            elif callarray[0] == "N":
                callNX = True
                print("-- callNX")
            elif callarray[0] == "W":
                callWX = True
                print("-- callWX")
        else:
            assert "1" == "should not get here" + str(pos) + "-" + str(leng)

    assert not callA
    assert callAX
    assert callK
    assert callKX
    assert callN
    assert callNX
    assert callW
    assert callWX
    assert call1x1
    assert call1x2
    assert call1x3
    assert call2x1
    assert call2x2
    assert call2x3




# TODO remove test
def test_arrays():
    str = "abc"
    # convert string to array
    one = list(str)
    two = ['a','b','c']
    print("")
    print("one:")
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
