from pydub import AudioSegment as am
import os

__save_path = "../data/users/"


def save_music(username, music, filename, instrument):
    path = __save_path + username
    if not os.path.exists(path):
        os.mkdir(path)
    path += "/" + instrument
    if not os.path.exists(path):
        os.mkdir(path)
    music.export(path + "/" + filename + ".WAV", format="wav")
