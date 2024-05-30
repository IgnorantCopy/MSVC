from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5 import QtCore, QtGui
from drumUI_rc import Drum_Ui_Form, MusicWidget
from Calc import Calc_Ui_Form
from qt_material import apply_stylesheet
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

        self.CalcWidget = QWidget()
        self.CalcUi = Calc_Ui_Form()
        self.CalcUi.setupUi(self.CalcWidget)
        self.addTab(self.CalcWidget, "Calc")


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
