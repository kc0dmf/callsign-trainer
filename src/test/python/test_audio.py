from src.main.python import hello

AUDIO_LOCN_BASE = "../../main/resource/"

def test_letter_1():
    assert hello.getLetter(1) == "alpha"

def test_medium_letters_high():
    for x in range(1,5):
        hello.playFirstLetterHigh2(x, AUDIO_LOCN_BASE + hello.AUDIO_SPEED_MID)

def test_medium_letters_mid():
    for x in range(1,6):
        hello.playLetterMid2(x, AUDIO_LOCN_BASE + hello.AUDIO_SPEED_MID)

def test_medium_letters_low():
    for x in range(1,6):
        hello.playLetterLow2(x, AUDIO_LOCN_BASE + hello.AUDIO_SPEED_MID)

def test_medium_numbers():
    for x in range(0,10):
        hello.playNumberMid2(x, AUDIO_LOCN_BASE + hello.AUDIO_SPEED_MID)

def test_fast_letters_high():
    for x in range(1,5):
        hello.playFirstLetterHigh2(x, AUDIO_LOCN_BASE + hello.AUDIO_SPEED_FAST)

def test_fast_letters_mid():
    for x in range(1,6):
        hello.playLetterMid2(x, AUDIO_LOCN_BASE + hello.AUDIO_SPEED_FAST)

def test_fast_letters_low():
    for x in range(1,6):
        hello.playLetterLow2(x, AUDIO_LOCN_BASE + hello.AUDIO_SPEED_FAST)

def test_fast_numbers():
    for x in range(0,10):
        hello.playNumberMid2(x, AUDIO_LOCN_BASE + hello.AUDIO_SPEED_FAST)


