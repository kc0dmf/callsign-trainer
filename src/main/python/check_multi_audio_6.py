# From: https://classes.engineering.wustl.edu/ese205/core/index.php?title=Playing_multiple_sounds_at_once
# Run this on the command line --> does not work
# Running from IntelliJ works --> plays both together; hangs after running
# ('../resource/old/alpha.wav')
# ('../resource/old/K2.wav')


import pygame

light_level = 900
light_level2 = 900

#this is code from the final version of code used to program the Laser Harp. This is saying that if lasers 1 and/or 2 are broken, the wav file associated with that file will be played.
import pygame
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.init()

if (light_level > 800):  # state 1
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('../resource/old/alpha.wav'))
if (light_level2 > 800):  # state 2
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('../resource/old/K2.wav'))