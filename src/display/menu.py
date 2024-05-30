import sys
from Ui_beginning import Ui_MainWindow
from y_part.QTabWidget import Window
from src.display import help
from src.utils import config
import beginning_fonts_rc
from PyQt5 import QtCore, QtGui
from qt_material import apply_stylesheet
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QInputDialog
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtGui import QFont, QFontDatabase


class MyBeginning(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyBeginning, self).__init__(parent)
        self.setupUi(self)
        self.statusShowTime()
        self.window = Window()
        self.lyric_help_window = help.Lyric_Help()
        self.drum_help_window = help.Drum_Help()
        self.piano_help_window = help.Piano_Help()
        self.guitar_help_window = help.Guitar_Help()

        fontDb = QFontDatabase()
        fontID = fontDb.addApplicationFont(":beginning_fonts/fonts/HYPixel9pxU-2.ttf")
        fontFamilies = fontDb.applicationFontFamilies(fontID)

        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
        QtGui.QGuiApplication.setHighDpiScaleFactorRoundingPolicy(
            QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

        self.combo = QComboBox(self)
        font = QFont('HYPixel 9px', 13)
        self.combo.setFont(font)
        self.combo.addItem('用户1')

        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(self.add_user)

        self.add_user.clicked.connect(config.add_user)
        self.enter.clicked.connect(self.Enter)
        self.delete_user.clicked.connect(config.remove_user)
        self.change_name.clicked.connect(config.modify_user)
        self.window.lyricsWidget.pushButton_menu.clicked.connect(self.return_menu)
        self.window.drumUi.pushButton_menu.clicked.connect(self.return_menu)
        self.window.lyricsWidget.pushButton_close.clicked.connect(self.close_menu)
        self.window.drumUi.pushButton_close.clicked.connect(self.close_menu)
        self.window.lyricsWidget.pushButton_help.clicked.connect(self.open_lyric_help)
        self.window.drumUi.pushButton_help.clicked.connect(self.open_drum_help)

    def statusShowTime(self):
        self.Timer = QTimer()
        self.Timer.start(1000)
        self.Timer.timeout.connect(self.updateTime)

    def updateTime(self):
        time = QDateTime.currentDateTime()
        timeplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.clock.setText(timeplay)

    def Enter(self):
        apply_stylesheet(app, theme="dark_teal.xml")
        self.close()
        self.window.show()

    def return_menu(self):
        self.window.close()
        app.setStyleSheet("")
        self.show()

    def close_menu(self):
        self.window.close()

    def open_lyric_help(self):
        self.lyric_help_window.show()

    def open_drum_help(self):
        self.drum_help_window.show()

    def open_piano_help(self):
        self.piano_help_window.show()

    def open_guitar_help(self):
        self.guitar_help_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyBeginning()
    myWin.show()
    sys.exit(app.exec_())
