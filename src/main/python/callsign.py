#!/usr/bin/python3

import random
import time
import simpleaudio as sa
import logging


# Python environment
# python3 -m venv /path/to/new/virtual/environment
# python3 -m venv ./env/callsign_trainer
# source ./env/callsign_trainer/bin/activate
#

VERSION = "0.9.2"

letterDict = {
    1: "A", 2: "B", 3: "C", 4: "D", 5: "E"
    , 6: "F", 7: "G", 8: "H", 9: "I", 10: "J"
    , 11: "K", 12: "L", 13: "M", 14: "N", 15: "O"
    , 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T"
    , 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y"
    , 26: "Z"
}

# Use for fast letters only (until all slow letters exist)
tempLetterDict = {
    i: i for i in range(1, 27)
}

# UNCOMMENT ME: to stick to only a subset of audio files for letters.
# You uncomment this to play a subset of either fast or slow letters.
# COMMENT OUT: to stick to all letters that are fast letters.
# See also: getLetter()
# tempLetterDict = {
#        A     B     C     D     E     F     K      N      W
#     1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 11, 8: 14, 9: 23
# }

firstLetterDict = {
    # Letters allowed to be the first letter in a 1x1, 1x2, 1x3 call are on the left
    # K, N, W, A, V
    1: 11, 2: 14, 3: 23, 4: 1, 5: 22
}
firstLetter1xDict = {
    # letters K, N, W
    1: 11, 2: 14, 3: 23
}
firstLetter2xDict = {
    # NOTE: make sure these keys don't overlap with the other first-letter dictionary
    # letters A, V
    4: 1, 5: 22
}
firstLetterMergedDict = firstLetter1xDict | firstLetter2xDict


AUDIO_LOCN_BASE = "../resource/"
AUDIO_LOCN_FAST = "fast/"
AUDIO_LOCN_SLOW = "slow/"

AUDIO_FAST = AUDIO_LOCN_BASE + AUDIO_LOCN_FAST
AUDIO_SLOW = AUDIO_LOCN_BASE + AUDIO_LOCN_SLOW
GAME_STOP = "stop"
GAME_GO = "GO"
GAME_GUESS = "GUESS"
GAME_TEST_CHARS_SLOW = "test chars slow"
GAME_TEST_CHARS_FAST = "test chars fast"
GAME_TEST_CALLS_SLOW = "test calls slow"
GAME_TEST_CALLS_FAST = "test calls fast"
MODE_GAME = "game"
MODE_TEST_CHARS = "test chars"
MODE_TEST_CALLS = "test calls"

PAUSE_SPEED = 750
PAUSE_BETW_CALLSIGNS = 0.50
PAUSE_BETW_LETTERS = 0.10

MAX_NUM_FIRST_LETTER = len(firstLetterDict)
MAX_NUM_ANY_LETTER = len(tempLetterDict)
MAX_CORRECT_MSG = 8

# Statistic variables
total_callsigns = 0
total_user_guesses = 0
stats_callsign_type = "0x0"
stats_current_callsign = ""
stats_guess_streak_current_count = 0
START_SHORTEST_GUESS_STREAK_VALUE = 1000
# Fewest guesses for any single callsign
stats_shortest_guess_streak = START_SHORTEST_GUESS_STREAK_VALUE
stats_shortest_guess_streak_call = ""
# Most guesses for any single callsign
stats_longest_guess_streak = 0
stats_longest_guess_streak_call = ""
# Number of callsigns guessed correctly on first try
stats_first_guess_success = 0

# Initialize histogram
# For example, this means that the 2x3 calls had 5 guesses on the first try, and 1 guess on the 4th try.
# {'1x1': {}, '1x2': {}, '1x3': {}, '2x1': {}, '2x2': {}, '2x3': {1: 5, 4: 1}}
guesses_per_type_hist = {
    "1x1": {},
    "1x2": {},
    "1x3": {},
    "2x1": {},
    "2x2": {},
    "2x3": {}
}


class Config:
    def __init__(self, speed, mode):
        self.speed = speed
        self.mode = mode


def init_stats():
    # Statistic variables
    global total_callsigns
    global total_user_guesses
    global stats_callsign_type
    global stats_current_callsign
    global stats_guess_streak_current_count
    global START_SHORTEST_GUESS_STREAK_VALUE
    # Fewest guesses for any single callsign
    global stats_shortest_guess_streak
    global stats_shortest_guess_streak_call
    # Most guesses for any single callsign
    global stats_longest_guess_streak
    global stats_longest_guess_streak_call
    # Number of callsigns guessed correctly on first try
    global stats_first_guess_success
    # histogram
    global guesses_per_type_hist

    # Statistic variables
    total_callsigns = 0
    total_user_guesses = 0
    stats_callsign_type = "0x0"
    stats_current_callsign = ""
    stats_guess_streak_current_count = 0
    START_SHORTEST_GUESS_STREAK_VALUE = 1000
    # Fewest guesses for any single callsign
    stats_shortest_guess_streak = START_SHORTEST_GUESS_STREAK_VALUE
    stats_shortest_guess_streak_call = ""
    # Most guesses for any single callsign
    stats_longest_guess_streak = 0
    stats_longest_guess_streak_call = ""
    # Number of callsigns guessed correctly on first try
    stats_first_guess_success = 0

    guesses_per_type_hist = {
        "1x1": {},
        "1x2": {},
        "1x3": {},
        "2x1": {},
        "2x2": {},
        "2x3": {}
    }


def getLetter(pos):
    # This (tempLetterDict) allows us to use the game when only a partial set
    # of audio clips are available.
    return letterDict[tempLetterDict[pos]]
    # Otherwise, could use this if we remove all references to tempLetterDict.
    # return letterDict[pos]


def getFirstLetter1x(pos):
    # return first letter for 1x1, 1x2, and 1x3 calls
    return letterDict[firstLetter1xDict[pos]]


def getFirstLetterMerged(pos):
    # return first letter for 2x1, 2x2, and 2x3 calls
    return letterDict[firstLetterMergedDict[pos]]


def getNumber(pos):
    # assumed pos is a number
    return str(pos)


def playPause():
    time.sleep(PAUSE_BETW_CALLSIGNS)


def playLetterPause():
    time.sleep(PAUSE_BETW_LETTERS)


def get_suffix_size():
    # lessen a chance of a 1 being returned
    # 1->1, 2->2, 3->3, 4->(4-2)=2, 5->(5-2)=3
    rnd = random.randint(1, 5)
    if rnd > 3:
        rnd -= 2
    return rnd


def get_prefix_size():
    return random.randint(1, 2)


def randomize_callsign():
    # call signs can be: 1x1, 1x2, 1x3, 2x1, 2x2, 2x3
    result = ""
    # max_number_first_letter = 0

    random.seed(None, 2)
    rndPrefix = get_prefix_size()
    rndSuffix = get_suffix_size()

    # UNCOMMENT ME: to keep all callsigns as 2x3 callsigns.
    # Note: you can change this to be 1x3, 2x2, etc.
    # rndPrefix = 2
    # rndSuffix = 3

    # create prefix letter(s)
    if rndPrefix == 2:
        # allow all first letters
        max_number_first_letter = len(firstLetterMergedDict)
        rnd = random.randint(1, max_number_first_letter)
        result += getFirstLetterMerged(rnd)
        if result == "V":
            # only allow Canadian calls as VA or VE
            rnd = random.randint(1, 2)
            if rnd == 2:
                # set to "E"
                rnd = 5
        else:
            rnd = random.randint(1, MAX_NUM_ANY_LETTER)
        result += getLetter(rnd)
    else:
        # exclude A and V as a first letter
        max_number_first_letter = len(firstLetter1xDict)
        rnd = random.randint(1, max_number_first_letter)
        result += getFirstLetter1x(rnd)

    # number
    rnd = random.randint(0, 9)
    result += getNumber(rnd)

    # suffix letters
    for _ in range(rndSuffix):
        rnd = random.randint(1, MAX_NUM_ANY_LETTER)
        result += getLetter(rnd)

    # set stats
    set_stats_callsign_size(rndPrefix, rndSuffix, result)

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
    characters_to_play = []

    # build the letters with inflection
    for ele in callsign:
        inflection = "-m"
        if cnt == 1:
            inflection = "-h"
        if cnt == size:
            inflection = "-l"
        characters_to_play.append(str(ele) + inflection)
        cnt += 1

    # Now play all characters
    for char_infl in characters_to_play:
        playCharacter(char_infl, speed)

def compare(expected, actual):
    return expected == actual


def playRandomCorrect(locn):
    rnd = random.randint(1, MAX_CORRECT_MSG)
    playCorrect(rnd, locn)


def playCorrect(rnd, locn):
    filename = locn + "correct-" + str(rnd) + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    playLetterPause()


def play_done(locn):
    rnd = 5
    filename = locn + "correct-" + str(rnd) + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    playLetterPause()


def get_input(actual_callsign, speed):
    global total_callsigns
    global total_user_guesses
    user_guess = GAME_GUESS

    while user_guess == GAME_GUESS:
        prompt = str(total_callsigns) + " Callsign? "
        if total_callsigns < 10:
            prompt = "0" + prompt
        user_guess = input(prompt).upper()
        if bool(compare(actual_callsign, user_guess)):
            update_stats_correct()
            playRandomCorrect(AUDIO_LOCN_BASE)
            playPause()
            user_guess = GAME_GO
        elif user_guess != "" and user_guess != "Q":
            update_stats_incorrect()
            play_callsign(actual_callsign, speed)
            user_guess = GAME_GUESS
        else:
            # leaving the game
            finish_up_stats()

    return user_guess


def get_user_input():
    call = "K0XT"
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
        print("SL) Play all slow letters and messages")
        print("FL) Play all fast letters and messages")
        print("SC) Play random slow calls")
        print("FC) Play random fast calls")
        print("Q) Quit")
        print()

        user_selection = input("Speed? ").upper()
        if user_selection == "S":
            result = Config(AUDIO_SLOW, MODE_GAME)
        elif user_selection == "F":
            result = Config(AUDIO_FAST, MODE_GAME)
        elif user_selection == "SL":
            result = Config(AUDIO_SLOW, MODE_TEST_CHARS)
        elif user_selection == "FL":
            result = Config(AUDIO_FAST, MODE_TEST_CHARS)
        elif user_selection == "SC":
            result = Config(AUDIO_SLOW, MODE_TEST_CALLS)
        elif user_selection == "FC":
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
    global total_callsigns
    results = ""
    actual_callsign = ""

    print()
    print("Callsign Trainer v" + VERSION)

    init_stats()
    user_selection = get_user_input()
    speed = user_selection.speed

    if user_selection.speed == GAME_STOP:
        results = GAME_STOP
    elif user_selection.mode == MODE_GAME:
        results = GAME_GO
    else:
        test_the_game(user_selection)

    while results == GAME_GO:
        update_stats_new_callsign()
        actual_callsign = randomize_callsign()
        play_callsign(actual_callsign, speed)
        results = get_input(actual_callsign, speed)

    # finish up the game
    show_stats(actual_callsign)

    return results


def set_stats_callsign_size(prefix_size, suffix_size, callsign):
    global stats_callsign_type
    global stats_current_callsign

    # set stats
    stats_callsign_type = str(prefix_size)+"x"+str(suffix_size)
    stats_current_callsign = callsign

    # Debug. Example: 1x3: N9ABC
    logging.debug(stats_callsign_type+": "+callsign)


def update_stats_correct():
    global total_user_guesses
    global stats_callsign_type
    global stats_guess_streak_current_count
    global stats_shortest_guess_streak
    global stats_shortest_guess_streak_call
    global stats_longest_guess_streak
    global stats_longest_guess_streak_call
    global stats_first_guess_success

    total_user_guesses = total_user_guesses + 1
    if stats_guess_streak_current_count < stats_shortest_guess_streak:
        stats_shortest_guess_streak = stats_guess_streak_current_count
        stats_shortest_guess_streak_call = stats_current_callsign
    if stats_guess_streak_current_count > stats_longest_guess_streak:
        stats_longest_guess_streak = stats_guess_streak_current_count
        stats_longest_guess_streak_call = stats_current_callsign
    if stats_guess_streak_current_count == 1:
        stats_first_guess_success += 1

    guesses_per_type_hist[stats_callsign_type][stats_guess_streak_current_count] = guesses_per_type_hist[stats_callsign_type].get(stats_guess_streak_current_count, 0) + 1


def update_stats_incorrect():
    global total_callsigns
    global total_user_guesses
    global stats_guess_streak_current_count

    total_user_guesses += 1
    stats_guess_streak_current_count += 1


def update_stats_new_callsign():
    global total_callsigns
    global stats_guess_streak_current_count

    total_callsigns += 1

    # reset other stats
    stats_guess_streak_current_count = 1
    stats_callsign_type = "0x0"


def finish_up_stats():
    global total_callsigns

    total_callsigns -= 1


# Distribution of Guesses | Counts of callsigns by number of guesses needed
def show_stats(last_callsign):
    global stats_shortest_guess_streak
    global total_user_guesses
    global total_callsigns
    global stats_first_guess_success
    global stats_shortest_guess_streak
    global stats_longest_guess_streak
    global stats_shortest_guess_streak_call
    global stats_longest_guess_streak_call

    if total_user_guesses == 0:
        # no stats to show
        return

    if logging.getLogger().isEnabledFor(logging.DEBUG):
        # Debugging is enabled
        logging.debug("debug stats")
        total_callsigns = 50
        total_user_guesses = 59
        stats_first_guess_success = 42
        stats_shortest_guess_streak = 1
        stats_shortest_guess_streak_call = "AD3XQU"
        stats_longest_guess_streak = 3
        stats_longest_guess_streak_call = "WT7XYB"
        last_callsign = "KA0XTT"

    # if no guesses then set the shortest guess streak to zero
    if stats_shortest_guess_streak == START_SHORTEST_GUESS_STREAK_VALUE:
        stats_shortest_guess_streak = 0

    calc_average_guesses_per_callsign = round(total_user_guesses / total_callsigns, 1)
    calc_first_guess_success_rate = round(stats_first_guess_success / total_callsigns * 100, 1)

    print()
    print()
    print("Statistics:")
    print("-----------")
    print()
    print("Total # callsigns given:      " + str(total_callsigns))
    print("Total guesses taken:          " + str(total_user_guesses))
    print("Avg guesses per callsign:     " + str(calc_average_guesses_per_callsign))
    print("First guess correct:          " + str(stats_first_guess_success))
    print("First guess success rate:     " + str(calc_first_guess_success_rate) + "%")
    print("Shortest Guess Streak:        " + str(stats_shortest_guess_streak) + "  (fewest guesses for this callsign: " + stats_shortest_guess_streak_call + ")")
    print("Longest Guess Streak:         " + str(stats_longest_guess_streak) +  "  (most guesses for this callsign: " + stats_longest_guess_streak_call + ")")
    # lining up next print with above print()
    #    ("Last callsign (not guessed):  " + last_callsign)
    if last_callsign != "":
        print("Last callsign (not guessed):  " + last_callsign)
    print()

    print_histogram(guesses_per_type_hist)


def print_histogram(p_histogram):
    if logging.getLogger().isEnabledFor(logging.DEBUG):
        # Debugging is enabled
        logging.debug("debug histogram")
        # histogram is: dict_items([('1x1', {}), ('1x2', {1: 7, 3: 3}), ('1x3', {3: 8}), ('2x1', {1: 4, 2: 6, 3: 1}), ('2x2', {1: 9}), ('2x3', {1: 2, 2: 2, 3: 2, 4: 4})])
        p_histogram = {
            '1x1': {},
            '1x2': {1: 7, 3: 3},
            '1x3': {3: 8},
            '2x1': {1: 4, 2: 6, 3: 1},
            '2x2': {1: 9},
            '2x3': {1: 2, 2: 2, 3: 2, 4: 4}
        }

    logging.debug("histogram is: "+str(p_histogram.items()))

    print()
    print("Distribution:")
    print("-------------")
    for ctype, counts in p_histogram.items():
        if counts:  # Only proceed if not empty
            total = sum(counts.values())
            print()
            print(f"{ctype}: {total} call(s)")
            max_guess = max(counts) if counts else 1
            for n in range(1, max_guess + 1):
                pctCorrect = round(counts.get(n, 0) / total * 100)
                if n==1:
                    suffix = "st guess"
                elif n==2:
                    suffix = "nd guess"
                elif n==3:
                    suffix = "rd guess"
                else:
                    suffix = "th guess"

                if (counts.get(n, 0) == 0):
                    print(f"{n}{suffix}: ({pctCorrect}%)")
                else:
                    print(f"{n}{suffix}: {'X' * counts.get(n, 0)} ({pctCorrect}%)")
    print()



def run_the_test_all_chars(config):
    speed = config.speed
    print()

    # play all Correct messages
    for pos in range(1, MAX_CORRECT_MSG+1):
        print("correct: " + str(pos))
        playCorrect(pos, AUDIO_LOCN_BASE)
    print()

    # play all Number messages
    for pos in range(0,10):
        print("number: " + str(pos))
        playCharacter(getNumber(pos) + "-m", speed)
    print()

    # play all Letter-high messages
    for pos in tempLetterDict:
        print("letter-H: " + getLetter(pos) + " " + str(pos))
        playCharacter(getLetter(pos) + "-h", speed)
    print()

    # play all Letter-mid messages
    for pos in tempLetterDict:
        print("letter-M: " + getLetter(pos) + " " + str(pos))
        playCharacter(getLetter(pos) + "-m", speed)
    print()

    # play all Letter-low messages
    for pos in tempLetterDict:
        print("letter-L: " + getLetter(pos) + " " + str(pos))
        playCharacter(getLetter(pos) + "-l", speed)
    print()


def run_the_test_rnd_calls(config):
    speed = config.speed
    print()
    for num in range(0,10):
        actual_callsign = randomize_callsign()
        print(actual_callsign)
        play_callsign(actual_callsign, speed)
        playPause()

    print()


def main():
    # turn on for debugging
    # logging.basicConfig(level=logging.DEBUG)
    # debug - should not comment out next line
    logging.debug("Debugging is turned on")

    results = GAME_GO
    while results != GAME_STOP and results != "":
        results = run_the_game()
    play_done(AUDIO_LOCN_BASE)

main()
