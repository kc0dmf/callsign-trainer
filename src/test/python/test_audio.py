import time

from src.main.python import callsign

AUDIO_LOCN_BASE = "../../main/resource/"


def test_play_numbers_slow():
    time.sleep(0.75)
    for ele in range(0, 10):
        callsign.playCharacter(str(ele) + "-m", AUDIO_LOCN_BASE + callsign.AUDIO_LOCN_SLOW)


def test_play_chars_high_slow():
    time.sleep(0.75)
    for ele in ['A','K','N','W']:
        callsign.playCharacter(str(ele) + "-h", AUDIO_LOCN_BASE + callsign.AUDIO_LOCN_SLOW)


def test_play_chars_mid_slow():
    time.sleep(0.75)
    for ele in ['A','B','C','K','N','W']:
        callsign.playCharacter(str(ele) + "-m", AUDIO_LOCN_BASE + callsign.AUDIO_LOCN_SLOW)


def test_play_chars_low_slow():
    time.sleep(0.75)
    for ele in ['A','B','C','K','N','W']:
        callsign.playCharacter(str(ele) + "-l", AUDIO_LOCN_BASE + callsign.AUDIO_LOCN_SLOW)


def test_play_numbers_fast():
    time.sleep(0.75)
    for ele in range(0, 10):
        callsign.playCharacter(str(ele) + "-m", AUDIO_LOCN_BASE + callsign.AUDIO_LOCN_FAST)


def test_play_chars_high_fast():
    time.sleep(0.75)
    for ele in ['A','K','N','W']:
        callsign.playCharacter(str(ele) + "-h", AUDIO_LOCN_BASE + callsign.AUDIO_LOCN_FAST)


def test_play_chars_mid_fast():
    time.sleep(0.75)
    for ele in ['A','B','C','K','N','W']:
        callsign.playCharacter(str(ele) + "-m", AUDIO_LOCN_BASE + callsign.AUDIO_LOCN_FAST)


def test_play_chars_low_fast():
    time.sleep(0.75)
    for ele in ['A','B','C','K','N','W']:
        callsign.playCharacter(str(ele) + "-l", AUDIO_LOCN_BASE + callsign.AUDIO_LOCN_FAST)


def test_callsigns():
    speed = AUDIO_LOCN_BASE + callsign.AUDIO_LOCN_FAST
    print()
    for i in range(1, 6):
        actual_callsign = callsign.randomize_callsign()
        print(actual_callsign)
        callsign.play_callsign(actual_callsign, speed)
        callsign.playPause()

