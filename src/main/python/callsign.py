#!/usr/bin/python3

import random
import time
import simpleaudio as sa

# Python environment
# python3 -m venv /path/to/new/virtual/environment
# python3 -m venv ./env/callsign_trainer
# source ./env/callsign_trainer/bin/activate
#

VERSION = "0.7.1"

AUDIO_LOCN_BASE = "../resource/"
AUDIO_LOCN_FAST = "fast/"
AUDIO_LOCN_SLOW = "slow/"

AUDIO_FAST = AUDIO_LOCN_BASE + AUDIO_LOCN_FAST
AUDIO_SLOW = AUDIO_LOCN_BASE + AUDIO_LOCN_SLOW
GAME_STOP = "stop"
GAME_TEST_CHARS_SLOW = "test chars slow"
GAME_TEST_CHARS_FAST = "test chars fast"
GAME_TEST_CALLS_SLOW = "test calls slow"
GAME_TEST_CALLS_FAST = "test calls fast"
MODE_GAME = "game"
MODE_TEST_CHARS = "test chars"
MODE_TEST_CALLS = "test calls"

PAUSE_SPEED = 750
PAUSE_BETW_CALLSIGNS = 0.75
PAUSE_BETW_LETTERS = 0.10

user_attempts = 0
user_correct = 0

letterDict = {
    1: "A", 2: "B", 3: "C", 4: "D", 5: "E"
    , 6: "F", 7: "G", 8: "H", 9: "I", 10: "J"
    , 11: "K", 12: "L", 13: "M", 14: "N", 15: "O"
    , 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T"
    , 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y"
    , 26: "Z"
}

tempLetterDict = {
    1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 11, 8: 14, 9: 23
}
firstLetterDict = {
    1: 1, 2: 11, 3: 14, 4: 23
}

MAX_NUM_FIRST_LETTER = len(firstLetterDict)
MAX_NUM_ANY_LETTER = len(tempLetterDict)
MAX_CORRECT_MSG = 8

class Config:
    def __init__(self, speed, mode):
        self.speed = speed
        self.mode = mode

def getLetter(pos):
    return letterDict[tempLetterDict[pos]]
    # TODO: fix
    # return letterDict[pos]


def getFirstLetter(pos):
    return letterDict[firstLetterDict[pos]]


def getNumber(pos):
    # assumed pos is a number
    return str(pos)


def playPause():
    time.sleep(PAUSE_BETW_CALLSIGNS)


def playLetterPause():
    time.sleep(PAUSE_BETW_LETTERS)


def get_suffix_count():
    return random.randint(1, 3)


def get_prefix_count():
    return random.randint(1, 2)


def randomize_callsign():
    # call signs can be: 1x1, 1x2, 1x3, 2x1, 2x2, 2x3
    result = ""

    random.seed(None, 2)
    rndPrefix = get_prefix_count()
    rndSuffix = get_suffix_count()

    # TODO: force to be 1x3, 2x3, etc
    # rndPrefix = 2
    # rndSuffix = 3

    # prefix letter(s)
    if rndPrefix == 2:
        # allow all first letters
        rnd = random.randint(1, MAX_NUM_FIRST_LETTER)
        result += getFirstLetter(rnd)
        rnd = random.randint(1, MAX_NUM_ANY_LETTER)
        result += getLetter(rnd)
    else:
        # exclude A as a first letter
        rnd = random.randint(2, MAX_NUM_FIRST_LETTER)
        result += getFirstLetter(rnd)

    # number
    rnd = random.randint(0, 9)
    result += getNumber(rnd)

    # suffix letters
    while rndSuffix > 1:
        rnd = random.randint(1, MAX_NUM_ANY_LETTER)
        result += getLetter(rnd)
        rndSuffix = rndSuffix - 1
    rnd = random.randint(1, MAX_NUM_ANY_LETTER)
    result += getLetter(rnd)

    return result


def playCharacter(theChar, locn):
    filename = locn + theChar + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    if locn == AUDIO_SLOW:
        playLetterPause()


def play_callsign(callsign, speed):
    size = len(callsign)
    cnt = 1

    for ele in callsign:
        inflection = "-m"
        if cnt == 1:
            inflection = "-h"
        if cnt == size:
            inflection = "-l"
        cnt += 1
        playCharacter(str(ele) + inflection, speed)


def compare(expected, actual):
    return expected == actual


def playCorrect(locn):
    rnd = random.randint(1, MAX_CORRECT_MSG)
    filename = locn + "correct-" + str(rnd) + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    playLetterPause()


def playCorrect_done(locn):
    rnd = 5
    filename = locn + "correct-" + str(rnd) + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    playLetterPause()


def get_input(actual_callsign, speed):
    global user_attempts
    global user_correct
    user_guess = "GUESS"
    while user_guess == "GUESS":
        user_guess = input("Callsign? ").upper()
        user_attempts = user_attempts + 1
        if bool(compare(actual_callsign, user_guess)):
            playCorrect(AUDIO_LOCN_BASE)
            playPause()
            user_guess = "GO"
            user_correct = user_correct + 1
        elif user_guess != "" and user_guess != "Q":
            play_callsign(actual_callsign, speed)
            user_guess = "GUESS"
        else:
            user_attempts = user_attempts - 1

    return user_guess


def get_user_input():
    call = "N9ABC"
    user_selection = ""
    result = ""

    print()
    print("Note:")
    print("  A correct response will move you on to the next callsign.")
    print("  An incorrect response will repeat the same callsign again.")
    print("  Pressing the Enter key without any value will end the program.")
    print()
    while user_selection == "":
        print("S) Slow (" + call + ")")
        play_callsign(call, AUDIO_SLOW)
        print("F) Fast (" + call + ")")
        play_callsign(call, AUDIO_FAST)
        print("TCS) Test slow characters")
        print("TCF) Test fast characters")
        print("TRS) Test random slow calls")
        print("TRF) Test random fast calls")
        print("Q) Quit")
        print()

        user_selection = input("Speed? ").upper()
        if user_selection == "S":
            result = Config(AUDIO_SLOW, MODE_GAME)
        elif user_selection == "F":
            result = Config(AUDIO_FAST, MODE_GAME)
        elif user_selection == "TCS":
            result = Config(AUDIO_SLOW, MODE_TEST_CHARS)
        elif user_selection == "TCF":
            result = Config(AUDIO_FAST, MODE_TEST_CHARS)
        elif user_selection == "TRS":
            result = Config(AUDIO_SLOW, MODE_TEST_CALLS)
        elif user_selection == "TRF":
            result = Config(AUDIO_FAST, MODE_TEST_CALLS)
        elif user_selection == "Q":
            result = Config(GAME_STOP, MODE_GAME)
        else:
            user_selection = ""

    return result


def test_the_game(config):
    if config.mode == MODE_TEST_CHARS:
        run_the_test_all_chars(config)
    if config.mode == MODE_TEST_CALLS:
        run_the_test_rnd_calls(config)


def run_the_game():
    speed = ""
    results = ""
    actual_callsign = ""

    print()
    print("Callsign Trainer v" + VERSION)

    user_selection = get_user_input()
    speed = user_selection.speed

    if user_selection.mode == MODE_GAME:
        results = "GO"
    else:
        test_the_game(user_selection)

    while results == "GO":
        actual_callsign = randomize_callsign()
        play_callsign(actual_callsign, speed)
        results = get_input(actual_callsign, speed)

    # print the last callsign
    print()
    show_stats(actual_callsign)
    playCorrect_done(AUDIO_LOCN_BASE)


def show_stats(actual_callsign):
    print("last callsign: " + actual_callsign)
    print()
    print("Total callsigns guessed: " + str(user_correct))
    print("Total attempts made:     " + str(user_attempts))
    print()


def run_the_test_all_chars(config):
    speed = config.speed
    print()
    # letterDict[tempLetterDict[pos]]
    for ltr in tempLetterDict:
        print("letter: " + str(ltr))
        playCharacter(getLetter(ltr) + "-h", speed)
    for ltr in tempLetterDict:
        print("letter: " + str(ltr))
        playCharacter(getLetter(ltr) + "-m", speed)
    for ltr in range(0,10):
        print("number: " + str(ltr))
        playCharacter(getNumber(ltr) + "-m", speed)
    for ltr in tempLetterDict:
        print("letter: " + str(ltr))
        playCharacter(getLetter(ltr) + "-l", speed)

    print()

def run_the_test_rnd_calls(config):
    speed = config.speed
    print()
    for num in range(0,10):
        actual_callsign = randomize_callsign()
        print(actual_callsign)
        play_callsign(actual_callsign, speed)

    print()


def main():
    run_the_game()
    # TODO add flag to do only 1x3 calls


main()
