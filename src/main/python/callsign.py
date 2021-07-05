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
    # n             n               n               n               n
    1:"alpha",      2:"bravo",      3:"charlie",    4:"delta",      5:"echo"
    , 6:"foxtrot",  7:"golf",       8:"hotel",      9:"india",      10:"juliett"
    , 11:"kilo",    12:"lima",      13:"mike",      14:"november",  15:"oscar"
    , 16:"papa",    17:"quebec",    18:"romeo",     19:"sierra",    20:"tango"
    , 21:"uniform", 22:"victor",    23:"whiskey",   24:"x-ray",     25:"yankee"
    , 26:"zulu"
}

tempLetterDict = {
    1:1, 2:2, 3:3, 4:11, 5:14, 6:23
}
firstLetterDict = {
    1:1, 2:11, 3:14, 4:23
}


def getLetter(pos):
    return letterDict[tempLetterDict[pos]]
    # return letterDict[pos]

def getFirstLetter(pos):
    return letterDict[firstLetterDict[pos]]

def getNumber(pos):
    # assumed pos is a number
    return str(pos)

def playFirstLetterHigh2(pos, locn):
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
    playFirstLetterHigh2(rnd, speed)
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

def main():
    # callsign_simpleaudio()
    # callsign_simpleaudio_random_1()

    # callsign_simpleaudio_random_2()
    # playPause(PAUSE_SPEED)
    # callsign_simpleaudio_random_2()
    # playPause(PAUSE_SPEED)
    # callsign_simpleaudio_random_2()
    # playPause(PAUSE_SPEED)

    callsign_simpleaudio_random_3(AUDIO_SLOW)
    playPause(PAUSE_SPEED)
    callsign_simpleaudio_random_3(AUDIO_SLOW)
    playPause(PAUSE_SPEED)
    callsign_simpleaudio_random_3(AUDIO_FAST)
    playPause(PAUSE_SPEED)
    callsign_simpleaudio_random_3(AUDIO_FAST)
    playPause(PAUSE_SPEED)

# main()
