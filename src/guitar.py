from pydub import AudioSegment as am
import librosa as lr
import soundfile as sf
import random

file = open("../data/cache/text/track_guitar.txt", "r")


class Chord:
    def __init__(self, root, type, position):
        self.type = type
        self.root = root
        self.position = position


# 这里的position代表的是小节号。


class Guitar:
    def __init__(self, track, key, tempo, bar, llen):
        self.track = track * (llen * ((600 // int(tempo)) + 1))
        self.key = key
        self.tempo = tempo
        self.bar = bar
        self.len = llen


null = am.silent(duration=100)


def text_to_guitar(key, tempo, bar, len):
    guitar = Guitar(null, key, tempo, bar, len)
    score = []
    for line in file:
        while line.find(" ") != -1:
            tmp = []
            index = line.find(" ")
            tmp.append(line[0])
            if index == 1:
                tmp.append("M")
            else:
                tmp.append(line[1:index])
            tmp.append(line[index + 1:])
            tmp_chord = Chord(tmp[0], tmp[1], int(tmp[2]))
            score.append(tmp_chord)

    for chord in score:
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
        pitch += key

        y, sr = lr.load(f'../audio/piano/{chord.type}.WAV')
        y1 = lr.effects.pitch_shift(y, sr=sr, n_steps=pitch)

        position = (chord.position - 1) * 60 * bar / guitar.tempo * 1000

        sf.write('../data/cache/audio/t.WAV', y1, sr)
        sound = am.from_wav('../data/cache/audio/t.WAV')
        guitar.track = guitar.track.overlay(sound, position)

    guitar.track.export('../data/cache/audio/track_guitar.WAV', format='WAV')
    print("Guitar arrangement Done!")


def text_to_coordinate(line):
    tmp = []
    index = line.find(" ")
    r = line[0]
    pitch = 0
    if r == "C":
        pitch = 0
    elif r == "D":
        pitch = 1
    elif r == "E":
        pitch = 2
    elif r == "F":
        pitch = 3
    elif r == "G":
        pitch = 4
    elif r == "A":
        pitch = 5
    elif r == "B":
        pitch = 6
    tmp.append(pitch)

    tmp.append(int(line[index + 1:]))

    if index == 1:
        tmp.append("M")
    else:
        tmp.append(line[1:index])
    return tmp


# 这里的line代表的是一行音符
# tmp[0]代表纵轴（CDEFGAB 对应 0123456）
# tmp[1]代表横轴（位置，单位是小节）
# tmp[2]代表类型（M, m, dim7, sus2, sus4, 目前这些应该够了）

def coordinate_to_text(chord):
    line = ''
    tnum = chord[0]
    if tnum == "0":
        pitch = 'C'
    elif tnum == "1":
        pitch = 'D'
    elif tnum == "2":
        pitch = 'E'
    elif tnum == "3":
        pitch = 'F'
    elif tnum == "4":
        pitch = 'G'
    elif tnum == "5":
        pitch = 'A'
    elif tnum == "6":
        pitch = 'B'
    line += pitch
    if chord[2] == "M":
        line += ''
    else:
        line += str(chord[2])
    line += ' ' + str(chord[1])
    return line
