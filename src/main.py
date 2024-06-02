import sys
from PyQt5.QtWidgets import QApplication
from src.display import menu

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = menu.MyBeginning(app)
    myWin.show()
    sys.exit(app.exec_())
