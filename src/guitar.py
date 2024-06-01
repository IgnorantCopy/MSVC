from pydub import AudioSegment as am
import librosa as lr
import soundfile as sf
import random
import os

slc = am.silent(duration=3000)
slc.export('../audio/guitar/none.wav', format='WAV')

class Chord:
    def __init__(self, type, position):
        self.type = type
        self.position = position
# 这里的position代表的是小节号。


class Guitar:
    def __init__(self, track, key, tempo, bar, len):
        self.key = key
        self.tempo = tempo
        self.bar = bar
        self.len = len
        self.track = am.silent(duration = 60000 / tempo * len + 3000)




def text_to_guitar(key, tempo, bar, llen):
    tempo /= 4
    deviation = 500
    file = open("../data/cache/text/guitar_text.txt", "r")
    guitar = Guitar(None, key, tempo, bar, llen)
    # print(len(guitar.track))
    Score = []
    for line in file:
        tmp = []
        index = line.find(" ")
        tmp.append(line[:index])
        tmp.append(line[index+1:])
        tmp_chord = Chord(tmp[0], int(tmp[1]))
        Score.append(tmp_chord)

    for chord in Score:
        # print(chord.type, chord.position,'\n')
        pitch = key

        if os.path.exists(f'../audio/guitar/{chord.type}.wav'):
            y, sr = lr.load(f'../audio/guitar/{chord.type}.WAV')
        elif os.path.exists(f'../audio/guitar/{str(chord.type[0])}.wav'):
            y, sr = lr.load(f'../audio/guitar/{str(chord.type[0])}.wav')
        else:
            y, sr = lr.load('../audio/guitar/none.wav')

        y1 = lr.effects.pitch_shift(y, sr=sr, n_steps = pitch)

        position = (chord.position - 1) * 60000 / guitar.tempo * bar + deviation
        
        if position > len(guitar.track) - 2900:
            break
        
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
    line += ' ' + str(chord[1]) + '\n'
    return line


if __name__ == '__main__':
    # common.llm_to_text("请写一首流行风格的曲子", "guitar", 48)
    text_to_guitar(0, 90, 4, 13)
