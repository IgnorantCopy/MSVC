from pydub import AudioSegment as am
import librosa as lr
import soundfile as sf
import random
from arrange import Song, song

file = open("../data/cache/text/piano.txt", "r")


class Note:
    def __init__(self, pitch, position, duration):
        self.pitch = pitch
        self.position = position
        self.duration = duration


class Piano(Song):
    def __init__(self, track, key, tempo, bar, len):
        super().__init__(track * 1, key, tempo, bar, len)


null = am.silent(duration=100)

piano = Piano(null, song.key, song.tempo, song.bar, song.len)

Score = []

for line in file:
    while line.find(" ") != -1:
        tmp = []

        for i in range(3):
            index = line.find(" ")
            tmp.append(line[:index])
            line = line[index + 1:]

        tmpNote = Note(tmp[0], int(tmp[1]), float(tmp[2]) + 0.2)
        Score.append(tmpNote)

# Score[i] : 第 i 个音符
# tmp[0] : 音调
# tmp[1] : 位置
# tmp[2] : 持续时间

for note in Score:
    y, sr = lr.load('../audio/piano/do.WAV')
    note_len = lr.get_duration(path='../audio/piano/do.WAV')
    # 处理音调
    # print(notelen)
    # print(notelen)
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

    pitch += 12 * (int(note.pitch[1]) - 1)
    pitch += song.key
    y1 = lr.effects.pitch_shift(y, sr=sr, n_steps = pitch)

    # 处理时长
    # rate = 60.0 / float(piano.tempo) * note.duration
    # # print(rate)
    # y2 = lr.effects.time_stretch(y1, rate = notelen / rate)
    y2 = y1

    # 处理位置
    position = (note.position - 1) * 60 / piano.tempo * 1000

    # 保存音频
    sf.write('../data/cache/audio/t.WAV', y2, sr)

    # 处理音轨
    sound = am.from_wav('../data/cache/audio/t.WAV')
    piano.track = piano.track.overlay(sound, position)

piano.track.export('../data/cache/audio/track_piano.WAV', format='WAV')
file.close()
print("Piano arrangement Done!")