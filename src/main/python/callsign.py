import random
import time

import simpleaudio as sa
from playsound import playsound
import pygame

AUDIO_LOCN_BASE = "../resource/"
AUDIO_SPEED_FAST = "fast/"
AUDIO_SPEED_SLOW = "mid/"

AUDIO_FAST = AUDIO_LOCN_BASE + AUDIO_SPEED_FAST
AUDIO_SLOW = AUDIO_LOCN_BASE + AUDIO_SPEED_SLOW

PAUSE_SPEED = 750
PAUSE_BETW_CALLSIGNS = 0.75
PAUSE_BETW_LETTERS = 0.10

letterDict = {
    1: "A", 2: "B", 3: "C", 4: "D", 5: "E"
    , 6: "F", 7: "G", 8: "H", 9: "I", 10: "J"
    , 11: "K", 12: "L", 13: "M", 14: "N", 15: "O"
    , 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T"
    , 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y"
    , 26: "Z"
}

tempLetterDict = {
    1: 1, 2: 2, 3: 3, 4: 11, 5: 14, 6: 23
}
firstLetterDict = {
    1: 1, 2: 11, 3: 14, 4: 23
}


def getLetter(pos):
    return letterDict[tempLetterDict[pos]]
    # TODO: fix
    # return letterDict[pos]


def getFirstLetter(pos):
    return letterDict[firstLetterDict[pos]]


def getNumber(pos):
    # assumed pos is a number
    return str(pos)


def playLetterHigh2(pos, locn):
    filename = locn + getFirstLetter(pos) + "-h" + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def playLetterMid2(pos, locn):
    filename = locn + getLetter(pos) + "-m" + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def playLetterLow2(pos, locn):
    filename = locn + getLetter(pos) + "-l" + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def playNumberMid2(pos, locn):
    filename = locn + getNumber(pos) + "-m" + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def playPause(wait):
    time.sleep(PAUSE_BETW_CALLSIGNS)


def playLetterPause():
    time.sleep(PAUSE_BETW_LETTERS)


def callsign_simpleaudio_random_3(speed):
    random.seed(None, 2)

    rnd = random.randint(1, 4)
    # TODO - remove Alpha
    rnd = random.randint(2, 4)
    playLetterHigh2(rnd, speed)
    playLetterPause()

    if rnd == 1:
        rnd = random.randint(1, 5)
        playLetterMid2(rnd, speed)
        playLetterPause()

    rnd = random.randint(0, 9)
    playNumberMid2(rnd, speed)
    playLetterPause()

    rndLtr = random.randint(1, 3)
    # TODO - do a 1x3
    rndLtr = 3
    while rndLtr > 1:
        rnd = random.randint(1, 5)
        playLetterMid2(rnd, speed)
        playLetterPause()
        rndLtr = rndLtr - 1

    rnd = random.randint(1, 5)
    playLetterLow2(rnd, speed)
    playLetterPause()


def randomize_callsign(speed):
    # call signs can be: 1x1, 1x2, 1x3, 2x1, 2x2, 2x3
    random.seed(None, 2)
    rndPrefix = random.randint(1, 2)
    rndSuffix = random.randint(1, 3)

    # TODO: remove; force to be 1x3
    rndPrefix = 1
    rndSuffix = 3


def main():
    callsign_simpleaudio_random_3(AUDIO_SLOW)
    playPause(PAUSE_SPEED)
    callsign_simpleaudio_random_3(AUDIO_SLOW)
    playPause(PAUSE_SPEED)
    callsign_simpleaudio_random_3(AUDIO_FAST)
    playPause(PAUSE_SPEED)
    callsign_simpleaudio_random_3(AUDIO_FAST)
    playPause(PAUSE_SPEED)

# main()
