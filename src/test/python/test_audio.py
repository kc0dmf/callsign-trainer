import time

from src.main.python import callsign

AUDIO_LOCN_BASE = "../../main/resource/"

def test_medium_letters_high():
    time.sleep(0.75)
    for x in range(1,5):
        callsign.playFirstLetterHigh2(x, AUDIO_LOCN_BASE + callsign.AUDIO_SPEED_SLOW)

def test_medium_letters_mid():
    time.sleep(0.75)
    for x in range(1,7):
        callsign.playLetterMid2(x, AUDIO_LOCN_BASE + callsign.AUDIO_SPEED_SLOW)

def test_medium_letters_low():
    time.sleep(0.75)
    for x in range(1,7):
        callsign.playLetterLow2(x, AUDIO_LOCN_BASE + callsign.AUDIO_SPEED_SLOW)

def test_medium_numbers():
    time.sleep(0.75)
    for x in range(0,10):
        callsign.playNumberMid2(x, AUDIO_LOCN_BASE + callsign.AUDIO_SPEED_SLOW)

def test_fast_letters_high():
    time.sleep(0.75)
    for x in range(1,5):
        callsign.playFirstLetterHigh2(x, AUDIO_LOCN_BASE + callsign.AUDIO_SPEED_FAST)

def test_fast_letters_mid():
    time.sleep(0.75)
    for x in range(1,7):
        callsign.playLetterMid2(x, AUDIO_LOCN_BASE + callsign.AUDIO_SPEED_FAST)

def test_fast_letters_low():
    time.sleep(0.75)
    for x in range(1,7):
        callsign.playLetterLow2(x, AUDIO_LOCN_BASE + callsign.AUDIO_SPEED_FAST)

def test_fast_numbers():
    time.sleep(0.75)
    for x in range(0,10):
        callsign.playNumberMid2(x, AUDIO_LOCN_BASE + callsign.AUDIO_SPEED_FAST)


