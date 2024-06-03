from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget
from PyQt5.QtGui import QFont


class Lyric_Help(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("帮助")
        text = '''输入您的要求即可获得歌词。'''
        self.label = QLabel(text, self)
        self.setStyleSheet("font-size:30px")
        help_layout = QVBoxLayout()
        help_layout.addWidget(self.label)
        self.setGeometry(500, 500, 400, 300)
        self.setLayout(help_layout)


class Drum_Help(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("帮助")
        text = '''点击“生成”，稍作等待，即可获得你想要的谱子。

在生成结果中，谱子从上到下依次代表：军鼓、鼓边、中高音嗵鼓、中低音嗵鼓、
        
落地嗵鼓、低音大鼓、闭音踩镲、开音踩镲、叮叮镲边、叮叮镲尖。

点击色块可以调整特定位置的特定部位的敲击与否，选中色块之后，按 ’A‘ 键添加，按 ’D' 键删除。
'''
        self.label = QLabel(text)
        self.setStyleSheet("font-size:30px")
        help_layout = QVBoxLayout()
        help_layout.addWidget(self.label)
        self.setGeometry(500, 500, 400, 300)
        self.setLayout(help_layout)


class Piano_Help(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("帮助")
        text = '''点击“生成”，稍作等待，即可获得你想要的谱子。

在生成结果中，谱子显示了每个音的急促程度，从急到缓依此为：ss、s、l、ll。
        
可以选中色块后右击来修改该音高音符的演奏与否
'''
        self.label = QLabel(text)
        self.setStyleSheet("font-size:30px")
        help_layout = QVBoxLayout()
        help_layout.addWidget(self.label)
        self.setGeometry(500, 500, 400, 300)
        self.setLayout(help_layout)


class Guitar_Help(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("帮助")
        text = '''点击“生成”，稍作等待，即可获得你想要的谱子。

在生成结果中，谱子显示了每个小节的和弦类型。如果你要修改和弦，可以点击色块右击进行修改。
'''
        self.label = QLabel(text)
        self.setStyleSheet("font-size:30px")
        help_layout = QVBoxLayout()
        help_layout.addWidget(self.label)
        self.setGeometry(500, 500, 400, 300)
        self.setLayout(help_layout)
