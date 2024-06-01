from pydub import AudioSegment as am
from src.utils import common
from src import piano
from src import guitar
from src import drum


class Song:
    def __init__(self, key, tempo, bar, len):
        self.key = key
        self.tempo = tempo
        self.bar = bar
        self.len = len
        self.track = am.silent(duration = 60000 / tempo * len + 3000)


def check_guitar():
    file = "../data/cache/text/guitar_text.txt"
    f = open(file, "r", encoding="utf-8")
    for line in f:
        l = []
        tmp = l
        index = line.find(" ")
        tmp.append(line[:index])
        tmp.append((line[index+1:])[:-1])
        if not tmp[1].isdigit():
            print(tmp[1])
            return False
        index = tmp[1].find(" ")
        if index != -1:
            return False
    return True


def compose(req, question, len):
    file = common.llm_to_text(question, req, len)
    if req == "guitar":
        while not check_guitar():
            print("Error")
            file = common.llm_to_text(question, req, len)
    if req == "piano":
        piano.change()
    return file


def arrange(song, req):
    if req == "piano" and piano.text_to_piano(song.key, song.tempo, song.bar, song.len) == 1:
        track_piano = am.from_wav("../data/cache/audio/track_piano.WAV")
        song.track = song.track.overlay(track_piano)
    elif req == "guitar" and guitar.text_to_guitar(song.key, song.tempo, song.bar, song.len) == 1:
        track_guitar = am.from_wav("../data/cache/audio/track_guitar.wav")
        song.track = song.track.overlay(track_guitar)
    elif req == "drum" and drum.text_to_drum(song.tempo) == 1:
        track_drums = am.from_wav("../data/cache/audio/track_drum.wav")
        track_drums -= 8
        song.track = song.track.overlay(track_drums)
    else:
        return 0
    song.track.export("../data/cache/audio/arranged.WAV", format="WAV")
    return 1


if __name__ == "__main__":
    key = 3
    tempo = 110
    bar = 4
    len = 49
    req_list = ["piano"]
    genre = "流行"
    song = Song(key, tempo, bar, len)
    # 每次用arrange函数都要重新生成一个Song对象————这是错误的！！！
    for req in req_list:
        compose(req, genre, len)
        arrange(song, req)
