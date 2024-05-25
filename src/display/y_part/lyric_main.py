import sys
from Ui_lyrics import Ui_Form
from PyQt5.QtWidgets import QWidget,QApplication

class Lyrics(QWidget,Ui_Form):
    def __init__(self,parent=None):
        super(Lyrics,self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = Lyrics()
    myWin.show()
    sys.exit(app.exec_())