import sys
from PyQt5.QtWidgets import QApplication
from src.display import menu
from src.utils import config

user = config.get_record()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = menu.MyBeginning(app)
    myWin.show()
    sys.exit(app.exec_())
