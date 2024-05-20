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

class Guitar(Song):
    def __init__(self, track, key, tempo, bar, len):
        super().__init__(track, key, tempo, bar, len)

null = am.silent(duration=100)

guitar = Guitar(null, song.key, song.tempo, song.bar, song.len)

Score = []

for line in file:
    while line.find(" ")!= -1:
        tmp = []
        for i in range(3):
            index = line.find(" ")
            tmp.append(line[:index])
            line = line[index+1:]
        tmpchord = Chord(tmp[0], tmp[1], tmp[2])
        Score.append(tmpchord)

for chord in Score:

    pitch = 0
    if chord.root == "C":
        pitch = 0
    elif chord.chord == "D":
        pitch = 2
    elif chord.chord == "E":
        pitch = 4
    elif chord.chord == "F":
        pitch = 5
    elif chord.chord == "G":
        pitch = 7
    elif chord.chord == "A":
        pitch = 9
    elif chord.chord == "B":
        pitch = 11
    pitch += song.key

    y, sr = lr.load(f'../audio/piano/{chord.type}.WAV')
    y1 = lr.effects.pitch_shift(y, sr=sr, n_steps = pitch)

    position = (chord.position - 1) * 60 / guitar.tempo * 1000

    sf.write('../data/cache/audio/t.WAV', y1, sr)
    sound = am.from_wav('../data/cache/audio/t.WAV')
    guitar.track = guitar.track.overlay(sound, position)