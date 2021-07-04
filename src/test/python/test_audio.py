from src.main.python import callsign

AUDIO_LOCN_BASE = "../../main/resource/"

def test_letter_1():
    assert callsign.getLetter(1) == "alpha"

def test_medium_letters_high():
    for x in range(1,5):
        callsign.playFirstLetterHigh2(x, AUDIO_LOCN_BASE + callsign.AUDIO_SPEED_SLOW)

def test_medium_letters_mid():
    for x in range(1,6):
        callsign.playLetterMid2(x, AUDIO_LOCN_BASE + callsign.AUDIO_SPEED_SLOW)

def test_medium_letters_low():
    for x in range(1,6):
        callsign.playLetterLow2(x, AUDIO_LOCN_BASE + callsign.AUDIO_SPEED_SLOW)

def test_medium_numbers():
    for x in range(0,10):
        callsign.playNumberMid2(x, AUDIO_LOCN_BASE + callsign.AUDIO_SPEED_SLOW)

def test_fast_letters_high():
    for x in range(1,5):
        callsign.playFirstLetterHigh2(x, AUDIO_LOCN_BASE + callsign.AUDIO_SPEED_FAST)

def test_fast_letters_mid():
    for x in range(1,6):
        callsign.playLetterMid2(x, AUDIO_LOCN_BASE + callsign.AUDIO_SPEED_FAST)

def test_fast_letters_low():
    for x in range(1,6):
        callsign.playLetterLow2(x, AUDIO_LOCN_BASE + callsign.AUDIO_SPEED_FAST)

def test_fast_numbers():
    for x in range(0,10):
        callsign.playNumberMid2(x, AUDIO_LOCN_BASE + callsign.AUDIO_SPEED_FAST)


