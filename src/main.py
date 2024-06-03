import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui
sys.path.append('d:\Desktop\projects\MSVC')
from src.display import menu
from src.utils import config

user = config.get_record()

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 使尺寸一致
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    QtGui.QGuiApplication.setHighDpiScaleFactorRoundingPolicy(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    myWin = menu.MyBeginning(app)
    myWin.show()
    sys.exit(app.exec_())
