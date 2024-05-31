from PyQt5.QtWidgets import QApplication, QTabWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtGui
from src.display.y_part.drumUI_rc import Drum_Ui_Form, MusicWidget
from qt_material import apply_stylesheet
from src.display.y_part.lyric_main import Lyrics
from src.display.y_part.Ui_lyrics import Ui_Form
from src.display.y_part.pianoUI_rc import Piano_Ui_Form
from src.display.y_part.guitarUI_rc import Guitar_Ui_Form
import sys


class Window(QTabWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 100, 1200, 850)
        self.setMinimumSize(1200, 850)
        self.setWindowTitle("Python GUI TabExample")
        self.setWindowIcon(QIcon(QPixmap('images/ice.jpg')))

        self.setTabPosition(QTabWidget.TabPosition.North)

        self.drumWidget = MusicWidget()
        self.drumUi = Drum_Ui_Form()
        self.drumUi.setupUi(self.drumWidget)
        self.addTab(self.drumWidget, "Drum")

        self.pianoWidget = MusicWidget()
        self.pianoUi = Piano_Ui_Form()
        self.pianoUi.setupUi(self.pianoWidget)
        self.addTab(self.pianoWidget, "Piano")

        self.guitarWidget = MusicWidget()
        self.guitarUi = Guitar_Ui_Form()
        self.guitarUi.setupUi(self.guitarWidget)
        self.addTab(self.guitarWidget, "Guitar")

        self.lyricsWidget = Lyrics()
        self.lyricsUi = Ui_Form()
        self.lyricsUi.setupUi(self.lyricsWidget)
        self.addTab(self.lyricsWidget, "Lyrics")


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 使尺寸一致
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    QtGui.QGuiApplication.setHighDpiScaleFactorRoundingPolicy(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    window = Window()
    # apply_stylesheet(app, theme="light_teal.xml", invert_secondary=True)  # 设置样式表
    apply_stylesheet(app, theme="dark_teal.xml")  # 设置样式表
    window.show()
    sys.exit(app.exec())
