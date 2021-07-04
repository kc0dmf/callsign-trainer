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


def getLetter(pos):
    result = "noletter"
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
    result = "noletter"
    if pos == 1:
        result = "alpha"
    # elif pos == 2:
    #     result = "kilo"
    elif pos == 2:
        result = "november"
    elif pos == 3:
        result = "whiskey"

    return result

def getNumber(pos):
    result = "nonumber"
    if pos == 0:
        result = "zero"
    elif pos == 1:
        result = "one"
    elif pos == 2:
        result = "two"
    elif pos == 3:
        result = "three"
    elif pos == 4:
        result = "four"
    elif pos == 5:
        result = "five"
    elif pos == 6:
        result = "six"
    elif pos == 7:
        result = "seven"
    elif pos == 8:
        result = "eight"
    elif pos == 9:
        result = "nine"

    return result

def callsign_simpleaudio_random():
    random.seed(None, 2)
    rnd = random.randint(1, 5)
    filename = "../resource/" + getFirstLetter(random.randint(1, 3)) + "-h" + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    filename = "../resource/" + getNumber(random.randint(0, 9)) + "-m" + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    filename = "../resource/" + getLetter(random.randint(1, 5)) + "-m" + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    filename = "../resource/" + getLetter(random.randint(1, 5)) + "-l" + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

print("hello python world!!")
x = myFunction("x")
print("func: "+x)
# callsign_simpleaudio()
callsign_simpleaudio_random()
