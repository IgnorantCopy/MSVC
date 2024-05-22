from pydub import AudioSegment as am
import librosa as lr
import soundfile as sf
import random
from arrange import *

file = open("../data/cache/text/guitar.txt", "r")

class Chord:
    def __init__(self, root, type, position):
        self.type = type
        self.root = root
        self.position = position
# 这里的position代表的是小节号。

class Guitar(Song):
    def __init__(self, track, key, tempo, bar, len):
        super().__init__(track, key, tempo, bar, len)

null = am.silent(duration=100)

guitar = Guitar(null, song.key, song.tempo, song.bar, song.len)

Score = []

for line in file:
    while line.find(" ")!= -1:
        tmp = []
        index = line.find(" ")
        tmp.append(line[0])
        if index == 1:
            tmp.append("M")
        else:
            tmp.append(line[1:index])
        tmp.append(line[index+1:])
        tmpchord = Chord(tmp[0], tmp[1], int(tmp[2]))
        Score.append(tmpchord)

for chord in Score:

    pitch = 0
    if chord.root == "C":
        pitch = 0
    elif chord.root == "D":
        pitch = 2
    elif chord.root == "E":
        pitch = 4
    elif chord.root == "F":
        pitch = 5
    elif chord.root == "G":
        pitch = 7
    elif chord.root == "A":
        pitch = 9
    elif chord.root == "B":
        pitch = 11
    pitch += song.key

    y, sr = lr.load(f'../audio/piano/{chord.type}.WAV')
    y1 = lr.effects.pitch_shift(y, sr=sr, n_steps = pitch)

    position = (chord.position - 1) * 60 * bar / guitar.tempo * 1000

    sf.write('../data/cache/audio/t.WAV', y1, sr)
    sound = am.from_wav('../data/cache/audio/t.WAV')
    guitar.track = guitar.track.overlay(sound, position)

    
guitar.track.export('../data/cache/audio/track_guitar.WAV', format='WAV')
file.close()
print("Guitar arrangement Done!")