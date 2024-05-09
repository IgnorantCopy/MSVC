from pydub import AudioSegment as am
import librosa as lr
import soundfile as sf
from arrange import *

file = open("../cache/text/piano.txt", "r")
class Note:
    def __init__(self, pitch, position, duration):
        self.pitch = pitch
        self.time = position
        self.duration = duration

Score = []

for line in file:
    while line.find(" ")!= -1:
        tmp = []

        for i in range(3):
            index = line.find(" ")
            tmp[i] = line[:index]
            line = line[index+1:]

        tmpNote = Note(tmp[0], tmp[1], tmp[2])
        Score.append(tmpNote)

for note in Score: 
    # 处理音调
    pitch = 0
    if note.pitch[0] == "C":
        pitch = 0
    elif note.pitch[0] == "D":
        pitch = 2
    elif note.pitch[0] == "E":
        pitch = 4
    elif note.pitch[0] == "F":
        pitch = 5
    elif note.pitch[0] == "G":
        pitch = 7
    elif note.pitch[0] == "A":
        pitch = 9
    elif note.pitch[0] == "B":
        pitch = 11

    pitch += 12 * int(note.pitch[1])
    pitch += Song.key

    # 处理速度
    y, sr = lr.load('../audio/piano.WAV')
    y1 = lr.effects.pitch_shift(y, sr=sr, n_steps = pitch)
    y2 = lr.effects.time_stretch(y1, note.duration)
    sf.write('../data/cache/audio/t.WAV', y2, sr)
    
    # 处理位置
    position = note.position * Song.tempo*1000/60

    # 处理音轨
    sound = am.from_wav('../data/cache/audio/t.WAV')
    Song.track = Song.track.overlay(sound, position)

file.close()

