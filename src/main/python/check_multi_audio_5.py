import pygame
from threading import Thread

# From: https://classes.engineering.wustl.edu/ese205/core/index.php?title=Playing_multiple_sounds_at_once
# Run this on the command line --> does not work
# Running from IntelliJ works --> plays both together; hangs after running
# ('../resource/old/alpha.wav')
# ('../resource/old/K2.wav')

lightlevell = 900
lightlevel2 = 900

def play1():
    if(lightlevell > 800):
        pygame.mixer.init()
        s = pygame.mixer.Sound('../resource/old/alpha.wav')
        pygame.mixer.Sound.play(s)


def play2():
    if(lightlevel2 > 800):
        pygame.mixer.init()
        s = pygame.mixer.Sound('../resource/old/K2.wav')
        pygame.mixer.Sound.play(s)


threads = []
if __name__=='__main__':
    threads.append(Thread(target = play1()))
    threads.append(Thread(target = play2))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
