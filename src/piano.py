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
        self.key = key
        self.tempo = tempo
        self.bar = bar
        self.len = len
        self.track = am.silent(duration = 60000 / tempo * len + 3000)

def change():
    file = "../data/cache/text/piano_text.txt"
    f = open(file, "r", encoding="utf-8")
    newf = ""
    num = 0
    for line in f:
        index = line.find(" ")
        if(index == -1):
            continue
        num += 1
        lline = line[index+1:]
        iindex = lline.find(" ")
        if(iindex == -1):
            continue
        tmp = lline[:iindex]
        if(tmp.isdigit() == False):
            continue
        while(int(tmp) > num):
            newf += "\n"
            num += 1
        newf += line
    
    f.close()
    f = open(file, "w", encoding="utf-8")
    f.write(newf)
    f.close()

def text_to_piano(key, tempo, bar, llen):
    deviation = 500
    maxpos = 0
    repete = 2
    tempo *= repete
    llen *= repete
    file = open("../data/cache/text/piano_text.txt", "r")
    piano = Piano(None, key, tempo, bar, llen)
    Score = []
    for line in file:
        while line.find(" ") != -1:
            tmp = []

            for i in range(3):
                index = line.find(" ")
                tmp.append(line[:index])
                line = line[index + 1:]

            tmpNote = Note(str(tmp[0]), int(tmp[1]), tmp[2])
            if int(tmp[1]) > maxpos:
                maxpos = int(tmp[1])
            Score.append(tmpNote)
    # Score[i] : 第 i 个音符
    # tmp[0] : 音调
    # tmp[1] : 位置
    # tmp[2] : 持续时间
    for i in range(repete * 4):
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
            position = (note.position - 1 + i * (maxpos + (maxpos&1))) * 60000 / piano.tempo + deviation
            if position > len(piano.track) - 2900:
                break
            # 保存音频
            sf.write('../data/cache/audio/t.WAV', y1, sr)

            # 处理音轨
            sound = am.from_wav('../data/cache/audio/t.WAV')
            piano.track = piano.track.overlay(sound, position)

    piano.track.export('../data/cache/audio/track_piano.WAV', format='WAV')
    print("Piano arrangement Done!")

def text_to_coordinate(line):
    tmp = []
    pitch = 7
    index = line.find(" ")
    pitch += int(line[0]) - 1
    if index != 1:
        if line[1] == "i":
            pitch += 7
        elif line[1] == "b":
            pitch -= 7

    tmp.append(pitch)
    line = line[index + 1:]
    index = line.find(" ")
    tmp.append(int(line[:index]))
    line = line[index + 1:]
    tmp.append(line)
    return tmp


# tmp[0] 代表纵坐标（{C0~B0,C1~B1,C2~B2}对应{0~6,7~13,14~20}）
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
    tmp += coordinate[2] + '\n'
    return tmp

if __name__ == '__main__':
    text_to_piano(4, 90, 4, 32)