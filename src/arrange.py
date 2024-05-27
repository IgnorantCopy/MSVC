from pydub import AudioSegment as am
from utils import common
import piano
import guitar
import drum
import lyrics

null = am.silent(duration=1000)


class Song:
    def __init__(self, track, key, tempo, bar, len):
        self.key = key
        self.tempo = tempo
        self.bar = bar
        self.len = len
        self.track = track * int(len * (60 / tempo) + 3)


def compose(song, req, question, key, tempo, bar, len):
    return common.llm_to_text(question, req, len)


def arrange(song, req, question, key, tempo, bar, len):
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
        song.track = song.track.overlay(track_drums)
    elif req == "lyrics":
        pass

    song.track.export("../data/cache/audio/arranged.WAV", format="WAV")


if __name__ == "__main__":
    key = 3
    tempo = 80
    bar = 4
    len = 48
    req_list = ["piano", "drum", "guitar"]
    genre = "流行"
    song = Song(null, key, tempo, bar, len)
    # 每次用arrange函数都要重新生成一个Song对象————这是错误的！！！
    for req in req_list:
        # compose(song, req, genre, key, tempo, bar, len)
        arrange(song, req, genre, key, tempo, bar, len)
