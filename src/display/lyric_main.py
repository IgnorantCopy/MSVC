from Ui_lyrics import Ui_Form
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QWidget
from src.utils import common


class Lyrics(QWidget,Ui_Form):
    def __init__(self,parent=None):
        super(Lyrics,self).__init__(parent)
        self.setupUi(self)
