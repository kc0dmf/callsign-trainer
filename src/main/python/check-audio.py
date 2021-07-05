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


def playLetters(pos, locn):
    filename = locn + "alpha" + "-h" + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    filename = locn + "bravo" + "-m" + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    filename = locn + "charlie" + "-l" + ".wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()



def main():
    playLetters(0, AUDIO_SLOW)


main()
