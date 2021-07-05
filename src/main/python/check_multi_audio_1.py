# From: https://stackoverflow.com/questions/39298928/play-multiple-sounds-at-the-same-time-in-python
# Run this on the command line.
# This does not run.


from pydub import AudioSegment
from pydub.playback import play

audio1 = AudioSegment.from_file("../resource/old/alpha.wav") #your first audio file
audio2 = AudioSegment.from_file("../resource/old/0.wav") #your second audio file
audio3 = AudioSegment.from_file("../resource/old/K2.wav") #your third audio file

mixed = audio1.overlay(audio2)          #combine , superimpose audio files
mixed1  = mixed.overlay(audio3)          #Further combine , superimpose audio files
#If you need to save mixed file
mixed1.export("mixed.wav", format='wav') #export mixed  audio file
play(mixed1)                             #play mixed audio file