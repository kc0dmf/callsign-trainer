import random

import simpleaudio as sa
from playsound import playsound
import pygame

def myFunction(myParam):
    print("love my functions")
    return "param-" + myParam

def callsign_simpleaudio():
    # using simpleaudio
    #
    filename = '../resource/alpha-h.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    filename = '../resource/bravo-m.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    filename = '../resource/eight-m.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    filename = '../resource/november-l.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

    # using playsound
    # filename = '../resource/0.wav'
    # playsound(filename)

    # using pygame -- DOESN'T SEEM TO WORK
    # pygame.init()
    #
    # filename = '../resource/alpha-h.wav'
    # pygame.mixer.music.load(filename)
    # pygame.mixer.music.play()
    # pygame.event.wait()
    #
    # filename = '../resource/whiskey-m.wav'
    # pygame.mixer.music.load(filename)
    # pygame.mixer.music.play()
    # pygame.event.wait()
    #
    # filename = '../resource/eight-m.wav'
    # pygame.mixer.music.load(filename)
    # pygame.mixer.music.play()
    # pygame.event.wait()
    #
    # filename = '../resource/whiskey-l.wav'
    # pygame.mixer.music.load(filename)
    # pygame.mixer.music.play()
    # pygame.event.wait()

# def noWorkingSwitch():
# no switch?
# switchee(i){
#     case 1:
# result = "alpha"
# break;
# }

# switcher={
#     case 1:
#     result = "alpha"
#     break;
# }
# return switcher.get(pos,"invalid")
#
# switch (pos) {
#     case 1:
#         result = "alpha"
#         break;
#     default:
#         result = "no-way"
# }
# return result

AUDIO_LOCN_BASE = "../resource/"
AUDIO_SPEED_FAST = "fast/"
AUDIO_SPEED_MID = "mid/"
AUDIO_SPEED = AUDIO_SPEED_FAST
AUDIO_LOCN = AUDIO_LOCN_BASE + AUDIO_SPEED
PAUSE_SPEED = 750

def getLetter(pos):
    result = "noletter-" + str(pos)
    if pos == 1:
        result = "alpha"
    elif pos == 2:
        result = "bravo"
    elif pos == 3:
        result = "charlie"
    elif pos == 4:
        result = "november"
    elif pos == 5:
        result = "whiskey"

    return result

def getFirstLetter(pos):
    result = "noletter-" + str(pos)
    if pos == 1:
        result = "alpha"
    elif pos == 2:
        result = "kilo"
    elif pos == 3:
        result = "november"
    elif pos == 4:
        result = "whiskey"

    return result

def getNumber(pos):
    # assumed pos is a number
    return str(pos)

def playFirstLetterHigh2(pos, locn):
    filename = locn + getFirstLetter(pos) + "-h" + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def playFirstLetterHigh(pos):
    playFirstLetterHigh2(pos, AUDIO_LOCN)

# def playLetterHigh2(pos, locn):
#     filename = locn + getLetter(pos) + "-h" + ".wav"
#     wave_obj = sa.WaveObject.from_wave_file(filename)
#     play_obj = wave_obj.play()
#     play_obj.wait_done()
#
# def playLetterHigh(pos):
#     playLetterHigh2(pos, AUDIO_LOCN)

def playLetterMid2(pos, locn):
    filename = locn + getLetter(pos) + "-m" + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def playLetterMid(pos):
    playLetterMid2(pos, AUDIO_LOCN)

def playLetterLow2(pos, locn):
    filename = locn + getLetter(pos) + "-l" + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def playLetterLow(pos):
    playLetterLow2(pos, AUDIO_LOCN)

def playNumberMid2(pos, locn):
    filename = locn + getNumber(pos) + "-m" + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def playNumberMid(pos):
    playNumberMid2(pos, AUDIO_LOCN)

def playPause(wait):
    filename = AUDIO_LOCN_BASE + "pause-" + str(wait) + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def callsign_simpleaudio_random_1():
    random.seed(None, 2)
    rnd = random.randint(1, 4)
    filename = AUDIO_LOCN + getFirstLetter(rnd) + "-h" + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    filename = AUDIO_LOCN + getNumber(random.randint(0, 9)) + "-m" + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    filename = AUDIO_LOCN + getLetter(random.randint(1, 5)) + "-m" + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    filename = AUDIO_LOCN + getLetter(random.randint(1, 5)) + "-l" + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def callsign_simpleaudio_random_2():
    random.seed(None, 2)

    rnd = random.randint(1, 4)
    playFirstLetterHigh(rnd)

    if rnd == 1:
        rnd = random.randint(1, 5)
        playLetterMid(rnd)

    rnd = random.randint(0, 9)
    playNumberMid(rnd)

    rndLtr = random.randint(1, 3)
    while rndLtr > 1:
        rnd = random.randint(1, 5)
        playLetterMid(rnd)
        rndLtr = rndLtr - 1

    rnd = random.randint(1, 5)
    playLetterLow(rnd)

def main():
    # callsign_simpleaudio()
    # callsign_simpleaudio_random_1()
    callsign_simpleaudio_random_2()
    playPause(PAUSE_SPEED)
    callsign_simpleaudio_random_2()
    playPause(PAUSE_SPEED)
    callsign_simpleaudio_random_2()

main()