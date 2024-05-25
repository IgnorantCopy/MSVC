from pydub import AudioSegment as am
import librosa as lr
import soundfile as sf
import random
import os
from utils import common

file = open("../data/cache/text/track_guitar.txt", "r")


class Chord:
    def __init__(self, type, position):
        self.type = type
        self.position = position
# 这里的position代表的是小节号。


class Guitar:
    def __init__(self, track, key, tempo, bar, len):
        self.track = track * (len * ((600 // int(tempo)) + 1))
        self.key = key
        self.tempo = tempo
        self.bar = bar
        self.len = len


null = am.silent(duration=100)


def text_to_guitar(key, tempo, bar, len):
    guitar = Guitar(null, key, tempo, bar, len)
    Score = []
    for line in file:
        while line.find(" ") != -1:
            tmp = []
            index = line.find(" ")
            tmp.append(line[:index])
            tmp.append(line[index+1:])
            tmp_chord = Chord(tmp[0], int(tmp[1]))
            Score.append(tmp_chord)

    for chord in Score:
        pitch = 0
        pitch += key

        if os.path.exists(f'../audio/guitar/{chord.type}.WAV'):
            y, sr = lr.load(f'../audio/guitar/{chord.type}.WAV')
        elif os.path.exists(f'../audio/guitar/{str(chord.type[0])}.WAV'):
            y, sr = lr.load(f'../audio/guitar/{str(chord.type[0])}.wav')
        else:
            y, sr = lr.load(f'../audio/guitar/none.WAV')

        y1 = lr.effects.pitch_shift(y, sr=sr, n_steps = pitch)

        position = (chord.position - 1) * 60 * bar / guitar.tempo * 1000

        sf.write('../data/cache/audio/t.WAV', y1, sr)
        sound = am.from_wav('../data/cache/audio/t.WAV')
        guitar.track = guitar.track.overlay(sound, position)

    guitar.track.export('../data/cache/audio/track_guitar.WAV', format='WAV')
    print("Guitar arrangement Done!")


def text_to_coordinate(line):
    tmp = []
    index = line.find(" ")
    tmp.append(0)
    tmp.append(int(line[index+1:]))

    tmp.append(line[:index])
    return tmp

# 这里的line代表的是文本中的一行
# tmp[0]代表纵轴（只有0！！！）
# tmp[1]代表横轴（位置，单位是小节）
# tmp[2]代表类型（一个string，由于和弦很多，我想给用户开放自定义输入）


def coordinate_to_text(chord):
    line = ''
    line += str(chord[2])
    line += ' ' + str(chord[1])
    return line


if __name__ == '__main__':
    common.llm_to_text("请写一首流行风格的曲子", "guitar", 1000)
    text_to_guitar(0, 90, 4, 0)
