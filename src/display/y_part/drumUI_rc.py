# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drumUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from qt_material import apply_stylesheet
from src.display.y_part.MyClass import MusicWidget, AIAnswer, AICreator, MyGraphicsView, DrumGraphicsPixmapItem
from src.utils import common
from src import drum


class Drum_Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 800)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_6.addWidget(self.line_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.hbox_tools = QtWidgets.QHBoxLayout()
        self.hbox_tools.setObjectName("hbox_tools")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hbox_tools.addItem(spacerItem)
        self.pushButton_menu = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_menu.setFont(font)
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.hbox_tools.addWidget(self.pushButton_menu)
        self.pushButton_help = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_help.setFont(font)
        self.pushButton_help.setObjectName("pushButton_help")
        self.hbox_tools.addWidget(self.pushButton_help)
        self.pushButton_close = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setObjectName("pushButton_close")
        self.hbox_tools.addWidget(self.pushButton_close)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hbox_tools.addItem(spacerItem1)
        self.hbox_tools.setStretch(1, 2)
        self.hbox_tools.setStretch(2, 2)
        self.hbox_tools.setStretch(3, 2)
        self.verticalLayout_2.addLayout(self.hbox_tools)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.hbox_choose = QtWidgets.QHBoxLayout()
        self.hbox_choose.setSpacing(5)
        self.hbox_choose.setObjectName("hbox_choose")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hbox_choose.addItem(spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_speed = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_speed.setFont(font)
        self.label_speed.setObjectName("label_speed")
        self.horizontalLayout.addWidget(self.label_speed)
        self.spinBox_speed = QtWidgets.QSpinBox(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.spinBox_speed.setFont(font)
        self.spinBox_speed.setObjectName("spinBox_speed")
        self.horizontalLayout.addWidget(self.spinBox_speed)
        self.hbox_choose.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hbox_choose.addItem(spacerItem5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_style = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_style.setFont(font)
        self.label_style.setObjectName("label_style")
        self.horizontalLayout_2.addWidget(self.label_style)
        self.comboBox_style = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_style.setFont(font)
        self.comboBox_style.setObjectName("comboBox_style")
        self.horizontalLayout_2.addWidget(self.comboBox_style)
        self.hbox_choose.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hbox_choose.addItem(spacerItem6)
        self.label_section = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_section.setFont(font)
        self.label_section.setObjectName("label_section")
        self.hbox_choose.addWidget(self.label_section)
        self.spinBox_section = QtWidgets.QSpinBox(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.spinBox_section.setFont(font)
        self.spinBox_section.setObjectName("spinBox_section")
        self.hbox_choose.addWidget(self.spinBox_section)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hbox_choose.addItem(spacerItem7)
        self.hbox_choose.setStretch(1, 5)
        self.hbox_choose.setStretch(2, 2)
        self.hbox_choose.setStretch(3, 5)
        self.hbox_choose.setStretch(4, 2)
        self.hbox_choose.setStretch(5, 2)
        self.hbox_choose.setStretch(6, 3)
        self.verticalLayout_2.addLayout(self.hbox_choose)
        spacerItem8 = QtWidgets.QSpacerItem(815, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.pushButton_create = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_create.setFont(font)
        self.pushButton_create.setStyleSheet("")
        self.pushButton_create.setObjectName("pushButton_create")
        self.verticalLayout_2.addWidget(self.pushButton_create)
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_result = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)
        self.pushButton_play = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_play.setFont(font)
        self.pushButton_play.setObjectName("pushButton_play")
        self.verticalLayout.addWidget(self.pushButton_play)
        self.pushButton_enter = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_enter.setFont(font)
        self.pushButton_enter.setObjectName("pushButton_enter")
        self.verticalLayout.addWidget(self.pushButton_enter)
        self.pushButton_stop = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.verticalLayout.addWidget(self.pushButton_stop)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 3)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.graphicsview_result = MyGraphicsView(Form)
        self.graphicsview_result.setObjectName("graphicsview_result")
        self.horizontalLayout_5.addWidget(self.graphicsview_result)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.setStretch(0, 20)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 10)
        self.verticalLayout_2.setStretch(3, 20)
        self.verticalLayout_2.setStretch(4, 5)
        self.verticalLayout_2.setStretch(5, 20)
        self.verticalLayout_2.setStretch(6, 1)
        self.verticalLayout_2.setStretch(7, 60)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_6.addWidget(self.line_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_ATtitle = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_ATtitle.setFont(font)
        self.label_ATtitle.setObjectName("label_ATtitle")
        self.verticalLayout_3.addWidget(self.label_ATtitle)
        self.textBrowser_AIanswer = QtWidgets.QTextBrowser(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_AIanswer.setFont(font)
        self.textBrowser_AIanswer.setObjectName("textBrowser_AIanswer")
        self.verticalLayout_3.addWidget(self.textBrowser_AIanswer)
        self.textEdit_user = QtWidgets.QTextEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit_user.setFont(font)
        self.textEdit_user.setObjectName("textEdit_user")
        self.verticalLayout_3.addWidget(self.textEdit_user)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_userdel = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_userdel.setFont(font)
        self.pushButton_userdel.setObjectName("pushButton_userdel")
        self.horizontalLayout_3.addWidget(self.pushButton_userdel)
        self.pushButton_usersend = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_usersend.setFont(font)
        self.pushButton_usersend.setObjectName("pushButton_usersend")
        self.horizontalLayout_3.addWidget(self.pushButton_usersend)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.setStretch(1, 5)
        self.verticalLayout_3.setStretch(2, 2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.horizontalLayout_6.setStretch(1, 5)
        self.horizontalLayout_6.setStretch(3, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.extra_set(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_menu.setText(_translate("Form", "菜单"))
        self.pushButton_help.setText(_translate("Form", "帮助"))
        self.pushButton_close.setText(_translate("Form", "结束"))
        self.label.setText(_translate("Form", "请设置以下的音乐元素后点击“开始”来生成音乐"))
        self.label_speed.setText(_translate("Form", "速度："))
        self.label_style.setText(_translate("Form", "风格："))
        self.label_section.setText(_translate("Form", "节拍数："))
        self.pushButton_create.setText(_translate("Form", "开始"))
        self.label_result.setText(_translate("Form", "结果："))
        self.pushButton_play.setText(_translate("Form", "播放"))
        self.pushButton_enter.setText(_translate("Form", "确认"))
        self.pushButton_stop.setText(_translate("Form", "暂停"))
        self.label_ATtitle.setText(_translate("Form", "AI问答："))
        self.pushButton_userdel.setText(_translate("Form", "删除"))
        self.pushButton_usersend.setText(_translate("Form", "发送"))

    def extra_set(self, Form):
        # 设置风格
        self.style_set()
        # some variables
        ai_text = "AI：你好，有什么问题?\n\n"
        self.textBrowser_AIanswer.setPlainText(ai_text)
        self.ai_answer = AIAnswer("")
        self.ai_answer.sinEnd.connect(self.AI_answer)
        self.ai_creater = AICreator("流行", "drum", 50, 90)
        self.image_path = "display/image/"
        # set textedit default text
        self.textEdit_user.setPlaceholderText("请输入你的问题：")
        # set spinbox
        self.spinBox_speed.setMinimum(50)
        self.spinBox_speed.setMaximum(240)
        self.spinBox_section.setMinimum(20)
        self.spinBox_section.setMaximum(80)
        # set comboBox's items
        self.comboBox_style.addItem("流行")
        self.comboBox_style.addItem("摇滚")
        self.comboBox_style.addItem("爵士")
        self.comboBox_style.addItem("金属")
        self.comboBox_style.addItem("前卫")
        # set GraphicsView
        self.graphics_set()
        # 连接到方法
        self.pushButton_create.clicked.connect(self.create_sender)
        self.pushButton_usersend.clicked.connect(self.AI_user_send)
        self.pushButton_userdel.clicked.connect(self.textEdit_user.clear)
        self.pushButton_close.clicked.connect(QtWidgets.QApplication.quit)
        self.pushButton_play.clicked.connect(self.play_event)
        self.pushButton_enter.clicked.connect(self.enter_event)
        self.pushButton_stop.clicked.connect(self.player.stop)

        Form.Key_event.connect(self.createKeyEvent)
        # end

    def style_set(self):
        # 设置字体
        font_size = 30
        for item in [self.pushButton_menu, self.pushButton_help, self.pushButton_close, self.pushButton_usersend,
                     self.pushButton_userdel, self.pushButton_play, self.pushButton_enter, self.pushButton_stop]:
            item.setStyleSheet(f"font-size: {font_size}px")
        for item in [self.label_style, self.label_speed, self.label_section, self.label_ATtitle, self.label,
                     self.label_result]:
            item.setStyleSheet(f"font-size: {font_size}px")
        for item in [self.spinBox_speed, self.spinBox_section, self.comboBox_style]:
            item.setStyleSheet(f"color: #1de9b6; font-size: {font_size}px")
        font_size = 22
        for item in [self.textEdit_user, self.textBrowser_AIanswer]:
            item.setStyleSheet(f"font-size: {font_size}px")
        font_size = 45
        self.pushButton_create.setStyleSheet(f"font-size: {font_size}px")
        # 设置大小
        self.pushButton_create.setMinimumHeight(70)

    def graphics_set(self):
        self.scene = QtWidgets.QGraphicsScene(0, 0, 100000, 100000)
        self.graphicsview_result.setMinimumSize(732, 344)
        self.graphicsview_result.setScene(self.scene)
        self.graphicsview_result.setSceneRect(0, 0, 1460, 680)
        # 设置一些参数
        self.section_size = (140, 25)
        self.instrument_icon_size = (35, 35)
        self.instrument_vspace = 20
        self.spaceBetween = 50
        self.instrument_y = 50
        self.block_space = 1
        self.section_space = 5
        self.instrument_num = 12
        self.right_space = 50
        self.down_space = 50
        self.block_true_name = "green_1.png"
        self.block_false_name = "green_0.png"
        self.cur_scale = 1.0
        self.min_scale = 0.6
        self.max_scale = 2.5
        self.change_scale = 1.2
        self.drum_speed = 90
        self.player = QtMultimedia.QMediaPlayer()

        self.instrument_names = ['snare', 'snare_side', 'tom1', 'tom2', 'tom3', 'ground', 'hihi_close', 'hihi_open',
                                 'ding', 'dang', 'cymbal1', 'cymbal2']

        self.choose = 0
        # 设置背景
        self.graphicsview_result.setBackgroundBrush(QtCore.Qt.GlobalColor.black)
        # 字典
        self.music = []
        self.section_lens = []
        self.modify_dict = {}

    def create_sender(self):
        self.pushButton_create.setEnabled(False)
        self.scene.clear()
        self.section_lens = []
        self.drum_speed = self.spinBox_speed.value()

        self.ai_creater.genre = f"请写一个{self.comboBox_style.currentText()}风格的鼓谱。"
        self.ai_creater.instrument = "drum"
        self.ai_creater.section = self.spinBox_section.value()
        self.ai_creater.speed = self.spinBox_speed.value()

        musiclists = [[{0: "11010", 1: "01010", 5: "11000"}, {0: "110", 2: "010", 3: "111"},
                       {-1: "0010", 0: "1001", 1: "100"}, {-1: "00"}, {-1: "00000000"}],
                      [{0: "11010", 1: "01010", 5: "11000"}, {0: "110", 2: "010", 3: "111"}]]

        # self.AI_create_result(musiclists[self.choose])
        # self.choose = (self.choose + 1) % 2

        self.ai_creater.sinEnd.connect(self.AI_create_result)
        self.ai_creater.start()

    def set_block(self, ti, tj, tlen, tj_str):
        """
        设置每个小节的各个乐器的旋律的显示
        :param ti: 表示第几个小节
        :param tj: 表示第几行
        :param tlen: 该小节的总长度，如："1001"对应4
        :param tj_str: 表示旋律的字符串如："1001"
        :return: 无
        """
        if tlen == 0:
            tlen = 4
        if tj_str == "":
            for k in range(tlen):
                tj_str += "0"
        each_len = int(self.section_size[0] / tlen)
        for m in range(tlen):
            if tj_str[m] == "0":
                timg_reader = QtGui.QImageReader(f"{self.image_path}{self.block_false_name}")
            else:
                timg_reader = QtGui.QImageReader(f"{self.image_path}{self.block_true_name}")
            timg_reader.setScaledSize(QtCore.QSize(each_len - self.block_space, self.section_size[1]))
            timg_reader = timg_reader.read()
            titem = DrumGraphicsPixmapItem(QtGui.QPixmap(timg_reader))
            self.scene.addItem(titem)
            titem.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
            titem.action1.triggered.connect(self.rightMenuAdd)
            titem.action2.triggered.connect(self.rightMenuDel)
            titem.instrument = tj
            titem.section = ti
            titem.beat = m
            titem.setPos(self.instrument_icon_size[0] + self.spaceBetween + each_len * m + (
                    self.section_size[0] + self.section_space) * ti,
                         self.instrument_y + int((self.instrument_icon_size[1] - self.section_size[1]) / 2) +
                         (self.instrument_icon_size[1] + self.instrument_vspace) * tj)

    def AI_create_result(self, music):
        self.music = music
        self.graphicsview_result.setSceneRect(0, 0, self.instrument_icon_size[0] + self.spaceBetween +
                                              (self.section_size[0] + self.section_space) * len(music) + self.right_space,
                                              self.instrument_y + (self.instrument_icon_size[1] + self.instrument_vspace) * 12 + self.down_space)

        self.graphicsview_result.centerOn(360, 200)

        i = 0
        for name in self.instrument_names:
            img_reader = QtGui.QImageReader(f"{self.image_path}{name}.png")
            img_reader.setScaledSize(QtCore.QSize(self.instrument_icon_size[0], self.instrument_icon_size[1]))
            img_reader = img_reader.read()
            instrument_item = DrumGraphicsPixmapItem(QtGui.QPixmap(img_reader))
            self.scene.addItem(instrument_item)
            instrument_item.setPos(0, self.instrument_y + i * (self.instrument_icon_size[1] + self.instrument_vspace))
            i += 1

        i = 0
        for section in music:
            max_len = 0
            if -1 in section:
                j_len = len(section[-1])
                section.clear()
                section[-1] = "0" * j_len
                self.section_lens += [j_len]
                for j in range(self.instrument_num):
                    self.set_block(i, j, j_len, "")
            else:
                left_instructions = []
                for j in range(self.instrument_num):
                    if j in section:
                        j_str = section[j]
                        j_len = len(j_str)
                        if j_len > max_len:
                            max_len = j_len
                        self.set_block(i, j, j_len, j_str)

                    else:
                        left_instructions += [j]

                self.section_lens += [max_len]
                for j in left_instructions:
                    self.set_block(i, j, max_len, "")

            i += 1

        self.pushButton_create.setEnabled(True)

    def create_rightmenu(self):
        print("yes")
        self.graphicsview_menu = QtWidgets.QMenu(Form)
        self.action1 = QtWidgets.QAction(u"增加")
        self.graphicsview_menu.addAction(self.action1)

        self.action1.triggered.connect(self.rightMenuAdd)

        if self.scene.selectedItems():
            self.graphicsview_menu.popup(QtGui.QCursor.pos())

    def createKeyEvent(self, key_name):
        if key_name == "A" or key_name == "D":
            file = ''
            if key_name == "A":
                judge = 1
                file = f"{self.image_path}{self.block_true_name}"
            elif key_name == "D":
                judge = 0
                file = f"{self.image_path}{self.block_false_name}"
            if self.scene.selectedItems():
                for item in self.scene.selectedItems():
                    item_rect = item.boundingRect()
                    item_pos = item.pos()
                    img_reader = QtGui.QImageReader(file)
                    img_reader.setScaledSize(QtCore.QSize(int(item_rect.width()) - 1, self.section_size[1]))
                    img_reader = img_reader.read()
                    new_item = DrumGraphicsPixmapItem(QtGui.QPixmap(img_reader))
                    new_item.instrument = item.instrument
                    new_item.section = item.section
                    new_item.beat = item.beat
                    self.scene.removeItem(item)
                    self.scene.addItem(new_item)
                    new_item.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
                    new_item.setSelected(True)
                    new_item.action1.triggered.connect(self.rightMenuAdd)
                    new_item.action2.triggered.connect(self.rightMenuDel)
                    new_item.setPos(item_pos)
                    self.modify_dict[new_item.section] = self.modify_event(new_item.instrument, new_item.section, new_item.beat, judge)
        elif key_name == "W" or key_name == "S":
            if key_name == "W" and self.cur_scale * self.change_scale < self.max_scale:
                self.cur_scale *= self.change_scale
                self.graphicsview_result.scale(self.change_scale, self.change_scale)
            elif key_name == "S" and self.cur_scale / self.change_scale > self.min_scale:
                self.cur_scale /= self.change_scale
                self.graphicsview_result.scale(1 / self.change_scale, 1 / self.change_scale)

    def modify_event(self, instrument, section, beat, judge):
        if judge == 1:
            j_str = "1"
        else:
            j_str = "0"
        result = ""
        if -1 in self.music[section] and judge == 1:
            self.music[section].clear()
            self.music[section][instrument] = "0" * self.section_lens[section]
            temp = list(self.music[section][instrument])
            temp[beat] = "1"
            self.music[section][instrument] = "".join(temp)
        elif instrument in self.music[section]:
            temp = list(self.music[section][instrument])
            temp[beat] = j_str
            self.music[section][instrument] = "".join(temp)
        elif not(instrument in self.music[section]) and judge == 1:
            self.music[section][instrument] = "0" * self.section_lens[section]
            temp = list(self.music[section][instrument])
            temp[beat] = "1"
            self.music[section][instrument] = "".join(temp)
        for k, v in self.music[section].items():
            result += f"{drum.get_index(k)}_{v} "
        print(result)
        return result

    def enter_event(self):
        self.player.stop()
        audio = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(""))
        self.player.setMedia(audio)
        text = drum.modify_text("../data/cache/text/drum_text.txt", self.modify_dict)

        drum.text_to_drum(self.drum_speed)
        self.modify_dict = {}

    def play_event(self):
        audio = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile("../data/cache/audio/track_drum.WAV"))
        self.player.setMedia(audio)
        self.player.play()

    def rightMenuAdd(self):
        self.createKeyEvent("A")

    def rightMenuDel(self):
        self.createKeyEvent("D")

    def AI_user_send(self):
        user_text = self.textEdit_user.toPlainText()
        if user_text != "":
            self.pushButton_usersend.setEnabled(False)
            self.textBrowser_AIanswer.append("你：" + user_text + "\n\n")
            self.textEdit_user.clear()
            self.ai_answer.user_text = user_text
            self.ai_answer.start()

    def AI_answer(self, ai_text):
        final_text = "AI：" + ai_text
        final_text += "\n\n"
        self.textBrowser_AIanswer.append(final_text)
        self.pushButton_usersend.setEnabled(True)


class DrumUI:
    def __init__(self):
        self.ui = Drum_Ui_Form()
        self.widget = MusicWidget()
        self.ui.setupUi(self.widget)


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 使尺寸一致
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    QtGui.QGuiApplication.setHighDpiScaleFactorRoundingPolicy(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_teal.xml")  # 设置样式表
    Form = MusicWidget()
    ui = Drum_Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
