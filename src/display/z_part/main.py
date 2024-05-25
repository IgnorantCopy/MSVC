from Ui_beginning import Ui_MainWindow
import sys
import beginning_fonts_rc
from PyQt5.QtWidgets import QApplication, QMainWindow,QComboBox,QVBoxLayout,QInputDialog
from PyQt5.QtCore import QTimer,QDateTime
from PyQt5.QtGui import QFont,QFontDatabase

class MyBeginning(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyBeginning, self).__init__(parent)
        self.setupUi(self)
        self.statusShowTime()

        fontDb = QFontDatabase()
        fontID = fontDb.addApplicationFont(":beginning_fonts/fonts/HYPixel9pxU-2.ttf")
        fontFamilies = fontDb.applicationFontFamilies(fontID)

        self.combo = QComboBox(self)
        font = QFont('HYPixel 9px',13)
        self.combo.setFont(font)
        self.combo.addItem('用户1')
        self.add_user.clicked.connect(self.addItem)
        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(self.add_user)
        self.setLayout(layout)

    def addItem(self):
        
        text, ok = QInputDialog.getText(self, '添加用户', '请输入新的用户名：')
        if ok:
            self.combo.addItem(text)
    
    def statusShowTime(self):   
        self.Timer=QTimer()   
        self.Timer.start(1000)  
        self.Timer.timeout.connect(self.updateTime)  

    def updateTime(self):
        time=QDateTime.currentDateTime()    
        timeplay=time.toString('yyyy-MM-dd hh:mm:ss dddd')   
        self.clock.setText(timeplay)  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyBeginning()
    myWin.show()
    sys.exit(app.exec_())