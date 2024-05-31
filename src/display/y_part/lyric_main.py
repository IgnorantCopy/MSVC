from src.display.y_part.Ui_lyrics import Ui_Form
from PyQt5.QtWidgets import QWidget
from src.display.y_part import MyClass


class Lyrics(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Lyrics, self).__init__(parent)
        self.setupUi(self)

