# From: https://classes.engineering.wustl.edu/ese205/core/index.php?title=Playing_multiple_sounds_at_once
# Run this on the command line.
# only plays one at a time

from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_wav('../resource/old/alpha.wav')
play(sound)

sound = AudioSegment.from_wav('../resource/old/K2.wav')
play(sound)
