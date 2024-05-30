from Ui_drum import Ui_Form
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QWidget


class Drum(QWidget,Ui_Form):
    def __init__(self,parent=None):
        super(Drum,self).__init__(parent)
        self.setupUi(self)
