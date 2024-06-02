import sys
from src.display.Ui_beginning import Ui_MainWindow
from src.display.y_part.QTabWidget import Window
from src.display import help
from src.utils import config
from src.utils import common
import src.display.beginning_fonts_rc
from PyQt5 import QtCore, QtGui
from qt_material import apply_stylesheet
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QInputDialog, QWidget
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtGui import QFont, QFontDatabase


class MyBeginning(QMainWindow, Ui_MainWindow):
    def __init__(self, app, parent=None):
        super(MyBeginning, self).__init__(parent)
        self.app = app
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
        self.init_user()

        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(self.add_user)

        self.add_user.clicked.connect(self.add_user_config)
        self.enter.clicked.connect(self.Enter)
        self.delete_user.clicked.connect(self.remove_user_config)
        self.change_name.clicked.connect(self.modify_user_config)
        self.window.drumUi.pushButton_menu.clicked.connect(self.return_menu)
        self.window.drumUi.pushButton_close.clicked.connect(self.close_menu)
        self.window.drumUi.pushButton_help.clicked.connect(self.open_drum_help)
        (self.window.lyricsUi.pushButton_2.clicked.connect(self.lyrics_start))
        self.window.lyricsUi.pushButton_menu.clicked.connect(self.return_menu)
        self.window.lyricsUi.pushButton_help.clicked.connect(self.open_lyric_help)
        self.window.lyricsUi.pushButton_close.clicked.connect(self.close_menu)
        self.window.pianoUi.pushButton_menu.clicked.connect(self.return_menu)
        self.window.pianoUi.pushButton_close.clicked.connect(self.close_menu)
        self.window.pianoUi.pushButton_help.clicked.connect(self.open_piano_help)
        self.window.guitarUi.pushButton_menu.clicked.connect(self.return_menu)
        self.window.guitarUi.pushButton_close.clicked.connect(self.close_menu)
        self.window.guitarUi.pushButton_help.clicked.connect(self.open_guitar_help)

    def statusShowTime(self):
        self.Timer = QTimer()
        self.Timer.start(1000)
        self.Timer.timeout.connect(self.updateTime)

    def updateTime(self):
        time = QDateTime.currentDateTime()
        timeplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.clock.setText(timeplay)

    def Enter(self):
        apply_stylesheet(self.app, theme="dark_teal.xml")
        self.close()
        self.window.show()

    def return_menu(self):
        self.window.close()
        self.app.setStyleSheet("")
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

    def lyrics_start(self):
        content = self.window.lyricsUi.textEdit.toPlainText()
        lyrics = common.call_with_messages(common.prompt_lyrics, content)
        self.window.lyricsUi.textBrowser.setText(lyrics)

    def init_user(self):
        user_list = config.load_user()
        for user in user_list:
            self.combo.addItem(user)

    def add_user_config(self):
        text, ok = QInputDialog.getText(self, '添加用户', '请输入用户名:')
        if ok and text:
            self.combo.clear()
            config.add_user(text)
            self.init_user()

    def remove_user_config(self):
        text = self.combo.currentText()
        config.remove_user(text)
        self.combo.clear()
        self.init_user()

    def modify_user_config(self):
        old_text = self.combo.currentText()
        new_text, ok = QInputDialog.getText(self, '更改名字', '请输入用户名:')
        if ok and new_text:
            self.combo.clear()
            config.modify_user(old_text, new_text)
            self.init_user()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyBeginning(app)
    myWin.show()
    sys.exit(app.exec_())
