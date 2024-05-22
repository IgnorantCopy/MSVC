from pydub import AudioSegment as am
import librosa as lr
import soundfile as sf
import random
from arrange import *

file = open("../data/cache/text/guitar.txt", "r")


class Chord:
    def __init__(self, type, root, position):
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
    while line.find(" ") != -1:
        tmp = []
        for i in range(3):
            index = line.find(" ")
            tmp.append(line[:index])
            line = line[index + 1:]
        tmpchord = Chord(tmp[0], tmp[1], tmp[2])
        Score.append(tmpchord)

for chord in Score:
    pass
