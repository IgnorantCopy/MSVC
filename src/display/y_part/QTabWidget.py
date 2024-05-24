from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5 import QtCore
from drum3UI_rc import Drum_Ui_Form
import sys


class Window(QTabWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 900, 600)
        self.setWindowTitle("Python GUI TabExample")
        self.setWindowIcon(QIcon(QPixmap('images/ice.jpg')))

        self.setTabPosition(QTabWidget.TabPosition.North)

        self.DrumWidget = QWidget()
        self.DrumUi = Drum_Ui_Form()
        self.DrumUi.setupUi(self.DrumWidget)

        self.addTab(self.DrumWidget, "Drum")


QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 使尺寸一致
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
