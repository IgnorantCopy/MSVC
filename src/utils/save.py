from pydub import AudioSegment as am
import os

__save_path = "../data/users/"


def save_music(username, music, filename):
    if not os.path.exists(__save_path + username):
        os.mkdir(__save_path + username)
    music.export(__save_path + username + "/" + filename + ".WAV", format="wav")
