from pydub import AudioSegment as am
from utils import common


class Song:

    def __init__(self, track, key, tempo, bar, len):
        self.track = track * (len * ((600 // int(tempo)) + 1))
        self.key = key
        self.tempo = tempo
        self.bar = bar
        self.len = len


file = open("../data/cache/text/song.txt", "r")
null = am.silent(duration=100)
key = 0
tempo = 60
bar = 4
len = 16
song = Song(track=null, key=key, tempo=tempo, bar=bar, len=len)

for line in file:
    if line.startswith("key:"):
        key = int(line.split(":")[1])
    elif line.startswith("tempo:"):
        tempo = int(line.split(":")[1])
    elif line.startswith("bar:"):
        bar = int(line.split(":")[1])
    elif line.startswith("len:"):
        len = int(line.split(":")[1])
    elif line.startswith("req:"):
        for req in line.split():
            if req == "piano":
                import piano
                track_piano = am.from_wav("../data/cache/audio/track_piano.WAV")
                song.track = song.track.overlay(track_piano)
            elif req == "guitar":
                import guitar
                track_guitar = am.from_wav("../data/cache/audio/track_guitar.wav")
                song.track.overlay(track_guitar)
            elif req == "drum":
                import drum
                track_drums = am.from_wav("../data/cache/audio/track_drum.wav")
                song.track.overlay(track_drums)
            elif req == "lyric":
                import lyric

song.track.export("../data/cache/audio/arranged.WAV", format="WAV")
file.close()
