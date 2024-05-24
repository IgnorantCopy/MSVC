from PyQt5 import QtCore, QtGui, QtWidgets
from Calc import Ui_Form_calc
from CUI_rc1 import Ui_Form


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow

        self.CForm = QtWidgets.QWidget()
        self.Cui = Ui_Form()
        self.Cui.setupUi(self.CForm)
        # connect to Calc
        self.Cui.pushButton_calc.clicked.connect(self.switch_to_calc)
        # end

        self.calc_Form = QtWidgets.QWidget()
        self.calc_ui = Ui_Form_calc()
        self.calc_ui.setupUi(self.calc_Form)
        # connect to CUI
        self.calc_ui.pushButton_menu.clicked.connect(self.switch_to_cui)

        self.stacked_widget = QtWidgets.QStackedWidget()
        self.stacked_widget.addWidget(self.CForm)
        self.stacked_widget.addWidget(self.calc_Form)

        MainWindow.setCentralWidget(self.stacked_widget)

    def switch_to_calc(self):
        self.stacked_widget.setCurrentWidget(self.calc_Form)
        self.MainWindow.resize(600, 400)
        self.MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        self.MainWindow.setMaximumSize(QtCore.QSize(600, 400))

    def switch_to_cui(self):
        self.stacked_widget.setCurrentWidget(self.CForm)
        self.MainWindow.resize(930, 600)
        self.MainWindow.setMinimumSize(QtCore.QSize(930, 600))
        self.MainWindow.setMaximumSize(QtCore.QSize(930, 600))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling) # 使尺寸一致
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
