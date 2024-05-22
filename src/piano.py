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

        tmpNote = Note(tmp[0], int(tmp[1]), tmp[2])
        Score.append(tmpNote)

# Score[i] : 第 i 个音符
# tmp[0] : 音调
# tmp[1] : 位置
# tmp[2] : 持续时间

for note in Score:

    # 处理时长
    dur=note.duration
    y, sr = lr.load(f'../audio/piano/do.WAV')
    # y, sr = lr.load(f'../audio/piano/do{dur}.WAV')

    # 处理音调
    # print(notelen)
    # print(notelen)
    pitch = 0
    if note.pitch[0] == "1":
        pitch = 0
    elif note.pitch[0] == "2":
        pitch = 2
    elif note.pitch[0] == "3":
        pitch = 4
    elif note.pitch[0] == "4":
        pitch = 5
    elif note.pitch[0] == "5":
        pitch = 7
    elif note.pitch[0] == "6":
        pitch = 9
    elif note.pitch[0] == "7":
        pitch = 11
    if(len(note.pitch) == 2):
        if note.pitch[1] == "i":
            pitch += 12
        elif note.pitch[1] == "b":
            pitch -= 12
    pitch += song.key
    y1 = lr.effects.pitch_shift(y, sr=sr, n_steps = pitch)

    # 处理位置
    position = (note.position - 1) * 60 / piano.tempo * 1000

    # 保存音频
    sf.write('../data/cache/audio/t.WAV', y1, sr)

    # 处理音轨
    sound = am.from_wav('../data/cache/audio/t.WAV')
    piano.track = piano.track.overlay(sound, position)

piano.track.export('../data/cache/audio/track_piano.WAV', format='WAV')
file.close()
print("Piano arrangement Done!")