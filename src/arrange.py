from pydub import AudioSegment as am
from utils import common
import piano
import guitar
import drum
import lyrics

class Song:
    def __init__(self, track, key, tempo, bar, len):
        self.track = track * (len * ((600 // int(tempo)) + 1))
        self.key = key
        self.tempo = tempo
        self.bar = bar
        self.len = len

def compose(req, question, key, tempo, bar, len):
    return common.llm_to_text(question, req, len)


def arrange(req, question, key, tempo, bar, len):
    null = am.silent(duration=100)
    song = Song(track=null, key=key, tempo=tempo, bar=bar, len=len)
    if req == "piano":
        piano.text_to_piano(song.key, song.tempo, song.bar, song.len)
        track_piano = am.from_wav("../data/cache/audio/track_piano.WAV")
        song.track = song.track.overlay(track_piano)
    elif req == "guitar":
        guitar.text_to_guitar(song.key, song.tempo, song.bar, song.len)
        track_guitar = am.from_wav("../data/cache/audio/track_guitar.wav")
        song.track.overlay(track_guitar)
    elif req == "drum":
        drum.text_to_drum(song.key, song.tempo, song.bar, song.len)
        track_drums = am.from_wav("../data/cache/audio/track_drum.wav")
        song.track.overlay(track_drums)
    elif req == "lyrics":
        pass

    song.track.export("../data/cache/audio/arranged.WAV", format="WAV")


if __name__ == "__main__":
    key = 0
    tempo = 60
    bar = 4
    len = 16
    req_list = ["piano", "guitar", "drum", "lyrics"]
    question = "请写一首儿歌。"
    arrange(question, req_list, key, tempo, bar, len)
