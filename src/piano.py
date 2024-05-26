from pydub import AudioSegment as am
import librosa as lr
import soundfile as sf
import random


class Note:
    def __init__(self, pitch, position, duration):
        self.pitch = pitch
        self.position = position
        self.duration = duration


class Piano():
    def __init__(self, track, key, tempo, bar, len):
        self.track = track * (len * ((600 // int(tempo)) + 1))
        self.key = key
        self.tempo = tempo
        self.bar = bar
        self.len = len


null = am.silent(duration=100)


def text_to_piano(key, tempo, bar, llen):
    # tempo *= 4
    file = open("../data/cache/text/piano_text.txt", "r")
    piano = Piano(null, key, tempo, bar, llen)
    Score = []
    for line in file:
        while line.find(" ") != -1:
            tmp = []

            for i in range(3):
                index = line.find(" ")
                tmp.append(line[:index])
                line = line[index + 1:]

            tmpNote = Note(str(tmp[0]), int(tmp[1]), tmp[2])
            Score.append(tmpNote)

    # Score[i] : 第 i 个音符
    # tmp[0] : 音调
    # tmp[1] : 位置
    # tmp[2] : 持续时间

    for note in Score:

        # 处理时长
        dur=note.duration
        # y, sr = lr.load(f'../audio/piano/do.WAV')
        pitch = 0

        if len(note.pitch) == 2:
            if note.pitch[1] == "i":
                y, sr = lr.load(f'../audio/piano/doi_{dur}.WAV')
            else:
                y, sr = lr.load(f'../audio/piano/do_{dur}.WAV')
                pitch -= 12
        else:
            y, sr = lr.load(f'../audio/piano/do_{dur}.WAV')

        # 处理音调
        # print(notelen)
        # print(notelen)
        if note.pitch[0] == "1":
            pitch += 0
        elif note.pitch[0] == "2":
            pitch += 2
        elif note.pitch[0] == "3":
            pitch += 4
        elif note.pitch[0] == "4":
            pitch += 5
        elif note.pitch[0] == "5":
            pitch += 7
        elif note.pitch[0] == "6":
            pitch += 9
        elif note.pitch[0] == "7":
            pitch += 11

        pitch += key
        y1 = lr.effects.pitch_shift(y, sr=sr, n_steps=pitch)

        # 处理位置
        position = (note.position - 1) * 60000 / piano.tempo

        # 保存音频
        sf.write('../data/cache/audio/t.WAV', y1, sr)

        # 处理音轨
        sound = am.from_wav('../data/cache/audio/t.WAV')
        piano.track = piano.track.overlay(sound, position)

    piano.track.export('../data/cache/audio/track_piano.WAV', format='WAV')
    print("Piano arrangement Done!")

def text_to_coordinate(line):
    tmp = []
    pitch = 12
    index = line.find(" ")
    pitch += int(line[0]) - 1
    if index != 1:
        if line[1] == "i":
            pitch += 8
        elif line[1] == "b":
            pitch -= 8

    tmp.append(pitch)
    line = line[index + 1:]
    index = line.find(" ")
    tmp.append(int(line[:index]))
    line = line[index + 1:]
    index = line.find(" ")
    tmp.append(line[:index])
    return tmp

# tmp[0] 代表纵坐标（{C0~B0,C1~B1,C2~B2}对应{0~7,8~15,16~23}）
# tmp[1] 代表横坐标（位置，按拍划分）
# tmp[2] 代表属性（ll, l, s, ss）

def coordinate_to_text(coordinate):
    tmp = ""
    p1 = coordinate[0] % 8 + 1
    tmp += str(p1)
    if coordinate[0] // 8 == 0:
        tmp += "b"
    elif coordinate[0] // 8 == 2:
        tmp += "i"
    tmp += " "
    tmp += str(coordinate[1]) + " "
    tmp += coordinate[2]
    return tmp