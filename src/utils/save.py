from pydub import AudioSegment as am
import os

__save_path = "../data/users/"


def save_music(username, music, filename, instrument):
    path = __save_path + username
    if not os.path.exists(path):
        os.mkdir(path)
    if instrument != '':
        path += "/" + instrument
        if not os.path.exists(path):
            os.mkdir(path)
    music.export(path + "/" + filename + ".WAV", format="wav")


def save_lyrics(username, lyrics, filename):
    path = __save_path + username
    if not os.path.exists(path):
        os.mkdir(path)
    path += "/lyrics"
    if not os.path.exists(path):
        os.mkdir(path)
    with open(path + "/" + filename + ".txt", "w", encoding="utf-8") as f:
        f.write(lyrics)