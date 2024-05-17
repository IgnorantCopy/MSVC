from utils import common
from utils import save
from pydub import AudioSegment as am


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
        return 1
    return -1


def text_to_drum(text, speed):
    lines = text.split('\n')
    rate = 120 / speed
    duration = 500 * rate
    song = am.silent(duration=duration * len(lines))
    for i in range(len(lines)):
        line = lines[i]
        if len(line) == 0:
            continue
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
                    song = song.overlay(common.drum_list[index], position=(i + k / len(times)) * duration)
    return song


if __name__ == '__main__':
    text = '''
    A_1011
    B_1111
    C_1011
    D_1111
    H_1
    '''
    song = text_to_drum(text, 160)
    save.save_music("Ignorant", song, "song")