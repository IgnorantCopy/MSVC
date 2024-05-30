from pydub import AudioSegment as am
from src.utils import common
from src import piano
from src import guitar
from src import drum
from src import lyrics

class Song:
    def __init__(self, track, key, tempo, bar, len):
        self.key = key
        self.tempo = tempo
        self.bar = bar
        self.len = len
        self.track = am.silent(duration = 60000 / tempo * len + 3000)

def check_guitar():
    file = "../data/cache/text/guitar_text.txt"
    f = open(file, "r", encoding="utf-8")
    for line in f:
        tmp = []
        index = line.find(" ")
        tmp.append(line[:index])
        tmp.append((line[index+1:])[:-1])
        if(tmp[1].isdigit() == False):
            print(tmp[1])
            return False
        index = tmp[1].find(" ")
        if(index != -1):
            return False
    return True


def compose(req, question, len):
    file = common.llm_to_text(question, req, len)
    if(req == "guitar"):
        while(check_guitar() == False):
            print("Error")
            file = common.llm_to_text(question, req, len)
    return file


def arrange(song, req):
    if req == "piano":
        piano.text_to_piano(song.key, song.tempo, song.bar, song.len)
        track_piano = am.from_wav("../data/cache/audio/track_piano.WAV")
        song.track = song.track.overlay(track_piano)
    elif req == "guitar":
        guitar.text_to_guitar(song.key, song.tempo, song.bar, song.len)
        track_guitar = am.from_wav("../data/cache/audio/track_guitar.wav")
        song.track = song.track.overlay(track_guitar)
    elif req == "drum":
        f = common.read_text("../data/cache/text/drum_text.txt")
        drum.text_to_drum(f, song.tempo)
        track_drums = am.from_wav("../data/cache/audio/track_drum.wav")
        track_drums -= 8
        song.track = song.track.overlay(track_drums)
    elif req == "lyrics":
        pass

    song.track.export("../data/cache/audio/arranged.WAV", format="WAV")


if __name__ == "__main__":
    key = 3
    tempo = 110
    bar = 4
    len = 49
    req_list = ["piano", "guitar", "drum", "lyrics"]
    genre = "流行"
    song = Song(None, key, tempo, bar, len)
    # 每次用arrange函数都要重新生成一个Song对象————这是错误的！！！
    for req in req_list:
        compose(req, genre, len)
        arrange(song, req)
