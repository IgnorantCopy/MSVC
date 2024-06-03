import os

from pydub import AudioSegment as am
from src.utils import common

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


def get_index(index):
    if index == 0:
        return 'A'
    elif index == 2:
        return 'B'
    elif index == 3:
        return 'C'
    elif index == 4:
        return 'D'
    elif index == 6:
        return 'E'
    elif index == 7:
        return 'F'
    elif index == 5:
        return 'G'
    elif index == 10:
        return 'H'
    elif index == 11:
        return 'I'
    elif index == 8:
        return 'J'
    elif index == 9:
        return 'K'
    elif index == 1:
        return 'L'
    else:
        return 'O'


def text_to_drum(speed):
    text = common.read_text("../data/cache/text/drum_text.txt")
    if text is None:
        return 0
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
    if os.path.isfile("../data/cache/drum/track_drum.WAV"):
        song.export('../data/cache/audio/track_drum.WAV', format='wav')
    return 1


def text_to_coordinate(text):
    line = text.split(' ')
    x = int(line[0])
    y_dict = {}
    for i in range(len(line) - 1):
        key = get_note(line[i + 1][0])
        value = line[i + 1][2:]
        y_dict[key] = value
    return [x, y_dict]


def text_to_array(text):
    lines = text.split('\n')
    array = []
    for line in lines:
        if len(line) != 0:
            array.append(text_to_coordinate(line)[1])
    return array


def modify_text(filename, text_dict):
    with open(filename, "r", encoding="utf-8") as f:
        old_text = f.read()
    new_text = old_text.split('\n')
    for k, v in text_dict.items():
        if 0 <= k < len(new_text):
            new_text[k] = str(k) + ' ' + v
    result = ''
    with open(filename, "w", encoding="utf-8") as f:
        for line in new_text:
            f.write(line + '\n')
            result += line + '\n'
    return result
