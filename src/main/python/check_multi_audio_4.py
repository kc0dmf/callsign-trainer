# From: https://classes.engineering.wustl.edu/ese205/core/index.php?title=Playing_multiple_sounds_at_once
# Run this on the command line --> does not work
# Running from IntelliJ works --> plays both together; hangs after running

import time
import pygame

pygame.init()
pygame.mixer.init()
firstSound = pygame.mixer.Sound('../resource/old/alpha.wav')
secondSound = pygame.mixer.Sound('../resource/old/K2.wav')
firstSound.play()
secondSound.play()
secondSound = pygame.mixer.Sound('../resource/old/02.wav')
secondSound.play()
time.sleep(0.75)

# This doesn't help with hang.
# pygame.mixer.quit()
# pygame.quit()
