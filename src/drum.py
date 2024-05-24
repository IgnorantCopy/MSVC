from utils import common
from utils import save
from pydub import AudioSegment as am

# 军鼓
snare = am.from_wav("../audio/drum/snare.WAV")
snare_side = am.from_wav("../audio/drum/snare_side.WAV")
# 嗵鼓
tom1 = am.from_wav("../audio/drum/tom1.WAV")
tom2 = am.from_wav("../audio/drum/tom2.WAV")
tom3 = am.from_wav("../audio/drum/tom3.WAV")
# 落地嗵鼓
ground = am.from_wav("../audio/drum/ground.WAV")
# 踩镲
hihi_close = am.from_wav("../audio/drum/hihi_close.WAV")
hihi_open = am.from_wav("../audio/drum/hihi_open.WAV")
# 叮叮
ding = am.from_wav("../audio/drum/ding.WAV")
dang = am.from_wav("../audio/drum/dang.WAV")
# 吊镲
cymbal1 = am.from_wav("../audio/drum/cymbal1.WAV")
cymbal2 = am.from_wav("../audio/drum/cymbal2.WAV")

drum_list = [snare, snare_side, tom1, tom2, tom3, ground, hihi_close, hihi_open, ding, dang, cymbal1, cymbal2]


def get_note(note):
    if note == 'A':
        return 0
    elif note == 'B':
        return 2
    elif note == 'C':
        return 3
    elif note == 'D':
        return 4
    elif note == 'E':
        return 6
    elif note == 'F':
        return 7
    elif note == 'G':
        return 5
    elif note == 'H':
        return 10
    elif note == 'I':
        return 11
    elif note == 'J':
        return 8
    elif note == 'K':
        return 9
    elif note == 'L':
        return 1
    return -1


def text_to_drum(text, speed):
    lines = text.split('\n')
    rate = 120 / speed
    duration = 500 * rate
    deviation = 500
    song = am.silent(duration=duration * len(lines) + deviation)
    for i in range(len(lines)):
        line = lines[i]
        notes = line.split(' ')
        for j in notes:
            if len(j) == 0:
                continue
            note = j[0]
            times = j[2:]
            index = get_note(note)
            if index == -1:
                continue
            for k in range(len(times)):
                if times[k] == '0':
                    continue
                elif times[k] == '1':
                    song = song.overlay(drum_list[index], position=(i + k / len(times)) * duration + deviation)
    song.export('../data/cache/audio/track_drum.WAV', format='WAV')


if __name__ == '__main__':
    genre = "爵士"
    path = common.llm_to_text("请写一个{}风格的鼓谱。".format(genre), "drum", 20)
    text = common.read_text(path)
    print(text)
    text_dict = {0: "A_1111", 1: "A_1111", 2: "A_1111", 3: "A_1111"}
    text = common.modify_text(path, text_dict)
    print(text)
    text_to_drum(text, 120)
    