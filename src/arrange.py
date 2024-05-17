from pydub import AudioSegment as am


class Song:
    track = am.empty()
    key = 0
    tempo = 60
    bar = 4

    def __init__(self, track, key, tempo, bar, len):
        self.track = track
        self.key = key
        self.tempo = tempo
        self.bar = bar
        self.len = len


song = Song(am.empty(), 0, 90, 4, 16)
