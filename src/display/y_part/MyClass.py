from PyQt5 import QtCore, QtGui, QtWidgets
from src.utils import common
from src import drum
from src import arrange
from src import piano
from src import guitar


class MusicWidget(QtWidgets.QWidget):
    Key_event = QtCore.pyqtSignal(str)

    def keyPressEvent(self, event):
        key_name = ''
        if event.key() == QtCore.Qt.Key_A:
            key_name = "A"
        elif event.key() == QtCore.Qt.Key_D:
            key_name = "D"
        elif event.key() == QtCore.Qt.Key_W:
            key_name = "W"
        elif event.key() == QtCore.Qt.Key_S:
            key_name = "S"
        self.Key_event.emit(key_name)


class AIAnswer(QtCore.QThread, QtCore.QObject):  # 自定义信号，执行run()函数时，从线程发射此信号
    sinEnd = QtCore.pyqtSignal(str)

    def __init__(self, user_text, parent=None):
        QtCore.QThread.__init__(self, parent)
        QtCore.QObject.__init__(self, parent)
        self.user_text = user_text

    def run(self):
        ai_text = common.call_with_messages(common.prompt_default, self.user_text)
        self.sinEnd.emit(ai_text)


class AICreator(QtCore.QThread, QtCore.QObject):
    sinEnd = QtCore.pyqtSignal(list)

    def __init__(self, genre, instrument, section, speed, parent=None):
        QtCore.QThread.__init__(self, parent)
        QtCore.QObject.__init__(self, parent)
        self.genre = genre
        self.instrument = instrument
        self.section = section
        self.speed = speed

    def run(self):
        path = common.llm_to_text(self.genre, self.instrument, self.section)
        text = common.read_text(path)
        drum.text_to_drum(text, self.speed)
        musicLists = drum.text_to_array(text)
        self.sinEnd.emit(musicLists)


class PianoAICreator(QtCore.QThread, QtCore.QObject):
    sinEnd = QtCore.pyqtSignal(list)

    def __init__(self, genre, instrument, len, speed, key, parent=None):
        QtCore.QThread.__init__(self, parent)
        QtCore.QObject.__init__(self, parent)
        self.genre = genre
        self.instrument = instrument
        self.len = len
        self.speed = speed
        self.key = key
        self.text_path = ""

    def run(self):
        song = arrange.Song(None, self.key, self.speed, 4, self.len)
        arrange.compose("piano", self.genre, self.len)
        arrange.arrange(song, "piano")
        tmpc = self.get_tmps()
        print(tmpc)
        self.sinEnd.emit(tmpc)

    def get_tmps(self):
        tmpc = []
        file = open(f"{self.text_path}piano_text.txt", "r")
        text = file.read()
        for line in text.split("\n"):
            if line != "":
                tmpc += [piano.text_to_coordinate(line)]
        file.close()
        return tmpc


class GuitarAICreator(QtCore.QThread, QtCore.QObject):
    sinEnd = QtCore.pyqtSignal(list)

    def __init__(self, genre, instrument, len, speed, key, parent=None):
        QtCore.QThread.__init__(self, parent)
        QtCore.QObject.__init__(self, parent)
        self.genre = genre
        self.instrument = instrument
        self.len = len
        self.speed = speed
        self.key = key
        self.text_path = ""

    def run(self):
        song = arrange.Song(None, self.key, self.speed, 1, self.len)
        arrange.compose("guitar", self.genre, self.len)
        arrange.arrange(song, "guitar")
        tmpc = self.get_tmps()
        print(tmpc)
        self.sinEnd.emit(tmpc)

    def get_tmps(self):
        tmpc = []
        file = open(f"{self.text_path}guitar_text.txt", "r")
        text = file.read()
        for line in text.split("\n"):
            if line != "":
                tmpc += [piano.text_to_coordinate(line)]
        file.close()
        return tmpc


class DrumGraphicsPixmapItem(QtWidgets.QGraphicsPixmapItem):
    def __init__(self, pixmap):
        super().__init__(pixmap)

        self.instrument = ""
        self.section = 0
        self.beat = 0

        self.menu = QtWidgets.QMenu()
        self.action1 = QtWidgets.QAction("增加")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.action1.setFont(font)
        self.menu.addAction(self.action1)
        self.action2 = QtWidgets.QAction("删除")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.action2.setFont(font)
        self.menu.addAction(self.action2)

    def contextMenuEvent(self, event):
        self.setSelected(True)

        self.menu.popup(QtGui.QCursor.pos())


class MyGraphicsView(QtWidgets.QGraphicsView):
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.RightButton:
            pass
        else:
            super().mousePressEvent(event)


class PianoGraphicsPixmapItem(QtWidgets.QGraphicsPixmapItem):
    def __init__(self, pixmap):
        super().__init__(pixmap)

        self.section = 0
        self.line = 0
        self.style = ""

        self.menu = QtWidgets.QMenu()
        self.action1 = QtWidgets.QAction("增加")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.action1.setFont(font)
        self.menu.addAction(self.action1)
        self.action2 = QtWidgets.QAction("删除")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.action2.setFont(font)
        self.menu.addAction(self.action2)

    def contextMenuEvent(self, event):
        self.setSelected(True)

        self.menu.popup(QtGui.QCursor.pos())


class PianoGraphicsItemGroup(QtWidgets.QGraphicsItemGroup):
    def __init__(self):
        super().__init__()

        self.section = 0
        self.line = 0
        self.beat = 0
        self.style = ""

        self.menu = QtWidgets.QMenu()

        self.action2 = QtWidgets.QAction("删除")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.action2.setFont(font)
        self.menu.addAction(self.action2)

        self.action_ll = QtWidgets.QAction("ll")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.action_ll.setFont(font)
        self.menu.addAction(self.action_ll)

        self.action_l = QtWidgets.QAction("l")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.action_l.setFont(font)
        self.menu.addAction(self.action_l)

        self.action_s = QtWidgets.QAction("s")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.action_s.setFont(font)
        self.menu.addAction(self.action_s)

        self.action_ss = QtWidgets.QAction("ss")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.action_ss.setFont(font)
        self.menu.addAction(self.action_ss)

    def contextMenuEvent(self, event):
        self.setSelected(True)

        self.menu.popup(QtGui.QCursor.pos())


class GuitarGraphicsItemGroup(QtWidgets.QGraphicsItemGroup):
    def __init__(self):
        super().__init__()

        self.section = 0
        self.line = 0
        self.beat = 0
        self.style = ""

        self.menu = QtWidgets.QMenu()

        self.action1 = QtWidgets.QAction("增加")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.action1.setFont(font)
        self.menu.addAction(self.action1)

        self.action2 = QtWidgets.QAction("删除")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.action2.setFont(font)
        self.menu.addAction(self.action2)

    def contextMenuEvent(self, event):
        self.setSelected(True)

        self.menu.popup(QtGui.QCursor.pos())


class AttributeUi(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(213, 144)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.extra_set(Dialog)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "确认"))

    def extra_set(self, Dialog):
        self.style_set()
        self.Dialog = Dialog

        self.pushButton.clicked.connect(self.enterEvent)

    def style_set(self):
        font_size = 30
        for item in [self.lineEdit, self.pushButton]:
            item.setStyleSheet(f"color: #1de9b6; font-size: {font_size}px")

    def enterEvent(self):
        self.Dialog.close()
