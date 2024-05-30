import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QInputDialog, QWidget
from src.display import menu

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = menu.MyBeginning()
    myWin.show()
    sys.exit(app.exec_())
