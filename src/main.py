import utils.save
import random
from pydub import AudioSegment as am


def main():
    Am = am.from_wav('../audio/guitar/Am_resolve.WAV')
    Dm = am.from_wav('../audio/guitar/Dm_resolve.WAV')
    Em = am.from_wav('../audio/guitar/Em_resolve.WAV')
    F = am.from_wav('../audio/guitar/F_resolve.WAV')
    G = am.from_wav('../audio/guitar/G_resolve.WAV')
    Gm = am.from_wav('../audio/guitar/Gm_resolve.WAV')
    duration = 3.5
    notes = [Am[:duration * 1000], Dm[:duration * 1000], Em[:duration * 1000], F[:duration * 1000], G[:duration * 1000],
             Gm[:duration * 1000]]
    song = G[:duration * 1000]
    for _ in range(7):
        index = random.randint(0, len(notes) - 1)
        song = song + notes[index]
    utils.save.save_music("Ignorant", song, "song")


if __name__ == '__main__':
    main()

