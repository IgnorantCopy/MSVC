from PyQt5 import QtCore, QtGui, QtWidgets
from src.utils import common
from src import drum


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