from pydub import AudioSegment
from pydub.playback import play

audio = AudioSegment.from_wav("tada.wav")

audio = audio[500:] + audio[:800] # Index certain msec values of the file

audio -= 10 # Decrease volume by 10 decibels
#              or _out
audio = audio.fade_in(5000) # Fade audio1 in for 5 sec

#print(audio1.dBFS) # Get volume in decibels
#print(audio1.duration_seconds) # Get duration in seconds
play(audio)