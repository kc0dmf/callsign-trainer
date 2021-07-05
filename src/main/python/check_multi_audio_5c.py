import multiprocessing
import time
import simpleaudio as sa

# From: https://www.youtube.com/watch?v=35yYObtZ95o
# Run this on the command line --> plays both together
# Running from IntelliJ works --> plays both together; hangs after running
# ('../resource/old/alpha.wav')
# ('../resource/old/K2.wav')

lightlevell = 900
lightlevel2 = 900

def play1():
    filename = "../resource/old/alpha.wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def play2():
    filename = "../resource/old/K2.wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()


# p1 = multiprocessing.Process(target=play1,args=[1])
p1 = multiprocessing.Process(target=play1)
p2 = multiprocessing.Process(target=play2)
if __name__ == '__main__':
    p1.start()
    p2.start()

finish = time.perf_counter()
print("finished after: ", finish)
