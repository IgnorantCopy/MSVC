import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QInputDialog, QWidget

if __name__ == '__main__':
    sys.path.append('D:\Desktop\projects\MSVC')
    print(sys.path)
    from src.display import menu
    app = QApplication(sys.argv)
    myWin = menu.MyBeginning(app)
    myWin.show()
    sys.exit(app.exec_())
