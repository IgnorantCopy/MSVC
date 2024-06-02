# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pianoUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from qt_material import apply_stylesheet
from src.display.y_part.MyClass import MusicWidget, AIAnswer, MyGraphicsView, PianoGraphicsItemGroup, PianoAICreator
from src import piano, arrange


class Piano_Ui_Form(object):
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
        self.label_mode = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_mode.setFont(font)
        self.label_mode.setObjectName("label_mode")
        self.hbox_choose.addWidget(self.label_mode)
        self.spinBox_mode = QtWidgets.QSpinBox(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.spinBox_mode.setFont(font)
        self.spinBox_mode.setObjectName("spinBox_mode")
        self.hbox_choose.addWidget(self.spinBox_mode)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hbox_choose.addItem(spacerItem8)
        self.hbox_choose.setStretch(1, 5)
        self.hbox_choose.setStretch(2, 2)
        self.hbox_choose.setStretch(3, 2)
        self.hbox_choose.setStretch(4, 2)
        self.hbox_choose.setStretch(5, 2)
        self.hbox_choose.setStretch(6, 3)
        self.hbox_choose.setStretch(8, 2)
        self.hbox_choose.setStretch(9, 5)
        self.verticalLayout_2.addLayout(self.hbox_choose)
        spacerItem9 = QtWidgets.QSpacerItem(815, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem9)
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
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
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
        self.label_section.setText(_translate("Form", "长度："))
        self.label_mode.setText(_translate("Form", "调式："))
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
        self.ai_creater = PianoAICreator("流行", "piano", 50, 90, 0)
        self.text_path = "../data/cache/text/"
        self.audio_path = "../data/cache/audio/"
        self.ai_creater.text_path = self.text_path
        self.image_path = "display/image/"
        # set textedit default text
        self.textEdit_user.setPlaceholderText("请输入你的问题：")
        # set spinbox
        self.spinBox_speed.setMinimum(70)
        self.spinBox_speed.setMaximum(120)
        self.spinBox_section.setMinimum(17)
        self.spinBox_section.setMaximum(61)
        self.spinBox_mode.setMinimum(-7)
        self.spinBox_mode.setMaximum(7)
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

        Form.Key_event.connect(self.viewKeyEvent)
    # end

    def style_set(self):
        # 设置字体
        font_size = 30
        for item in [self.pushButton_menu, self.pushButton_help, self.pushButton_close, self.pushButton_usersend,
                     self.pushButton_userdel, self.pushButton_play, self.pushButton_enter, self.pushButton_stop]:
            item.setStyleSheet(f"font-size: {font_size}px")
        for item in [self.label_style, self.label_speed, self.label_section, self.label_ATtitle, self.label,
                     self.label_result, self.label_mode]:
            item.setStyleSheet(f"font-size: {font_size}px")
        for item in [self.spinBox_speed, self.spinBox_section, self.comboBox_style, self.spinBox_mode]:
            item.setStyleSheet(f"color: #1de9b6; font-size: {font_size}px")
        font_size = 22
        for item in [self.textEdit_user, self.textBrowser_AIanswer]:
            item.setStyleSheet(f"font-size: {font_size}px")
        font_size = 45
        self.pushButton_create.setStyleSheet(f"font-size: {font_size}px")
        # 设置大小
        self.pushButton_create.setMinimumHeight(70)
    # end

    def graphics_set(self):
        self.scene = QtWidgets.QGraphicsScene(0, 0, 100000, 100000)
        self.graphicsview_result.setMinimumSize(732, 344)
        self.graphicsview_result.setScene(self.scene)
        self.graphicsview_result.setSceneRect(0, 0, 1460, 680)
        # 设置一些参数
        self.section_size = (140, 25)
        self.instrument_icon_size = (35, 35)
        self.instrument_vspace = 1
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

        self.mode_names = ["1_0", "2_0", "3_0", "4_0", "5_0", "6_0", "7_0",
                           "1_1", "2_1", "3_1", "4_1", "5_1", "6_1", "7_1",
                           "1_2", "2_2", "3_2", "4_2", "5_2", "6_2", "7_2"]

        self.choose = 0
        # 设置背景
        self.graphicsview_result.setBackgroundBrush(QtCore.Qt.GlobalColor.black)
        # 字典
        self.music = []
        self.modify_dict = {}
    # end

    def create_sender(self):
        self.pushButton_create.setEnabled(False)
        self.scene.clear()

        self.ai_creater.len = self.spinBox_section.value()
        self.ai_creater.genre = self.comboBox_style.currentText()
        self.ai_creater.key = self.spinBox_mode.value()
        self.ai_creater.speed = self.spinBox_speed.value()

        # music_lists = []
        # music_lists += [[[10, 1, "ll"], [11, 2, "s"], [12, 3, "l"], [15, 4, "l"], [12, 5, "ss"], [11, 6, "s"], [12, 7, "l"], [15, 8, "l"]]]
        # music_lists += [[[10, 1, "ll"], [11, 2, "s"], [12, 3, "l"], [15, 4, "l"], [12, 5, "ss"], [14, 6, "s"], [11, 7, "s"], [12, 8, "l"]]]

        # self.AI_create_result(music_lists[self.choose])
        # self.choose = (self.choose + 1) % 2

        self.ai_creater.sinEnd.connect(self.AI_create_result)
        self.ai_creater.start()
    # end

    def AI_create_result(self, tmpc):
        music = self.create_array(tmpc)
        self.music = music
        self.graphicsview_result.setSceneRect(0, 0, self.instrument_icon_size[0] + self.spaceBetween +
                                              (self.section_size[0] + self.section_space) * len(music) + self.right_space,
                                              self.instrument_y + (self.instrument_icon_size[1] + self.instrument_vspace) * 21 + self.down_space)

        self.graphicsview_result.centerOn(360, 200)

        i = 0
        for name in self.mode_names:
            img_reader = QtGui.QImageReader(f"{self.image_path}{name}.png")
            img_reader.setScaledSize(QtCore.QSize(self.instrument_icon_size[0], self.instrument_icon_size[1]))
            img_reader = img_reader.read()
            instrument_item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap(img_reader))
            self.scene.addItem(instrument_item)
            instrument_item.setPos(0, self.instrument_y + i * (self.instrument_icon_size[1] + self.instrument_vspace))
            i += 1

        i = 0
        for section in music:
            j = 0
            for line in section:
                k = 0
                for beat in line:
                    self.set_block(i, j, k, beat)
                    k += 1
                j += 1
            i += 1

        self.pushButton_create.setEnabled(True)
    # end

    def create_array(self, music):
        max_len = 0
        for each in music:
            if each[1] - 1 > max_len:
                max_len = each[1] - 1
        if max_len % 4 == 0:
            max_len = max_len // 4
        else:
            max_len = max_len // 4 + 1
        result = []
        for i in range(max_len):
            lines = []
            for j in range(21):
                line = []
                for k in range(4):
                    line += [[0, ""]]
                lines += [line]
            result += [lines]
        for each in music:
            x = (each[1] - 1) // 4
            y = each[0]
            z = (each[1] - 1) % 4
            result[x][y][z][0] = 1
            result[x][y][z][1] = each[2]
        return result
    # end

    def set_block(self, ti, tj, tk, each):
        """
        设置每个小节的各个乐器的旋律的显示
        :param ti: 表示第几个小节
        :param tj: 表示第几行
        :param tk: 表示第几拍
        :param each: a list: [0, "ll"]
        :return: 无
        """
        tlen = 4
        if each[1] == "":
            # each[1] = "none"
            pass

        each_len = int(self.section_size[0] / tlen)

        pos = QtCore.QPointF(self.instrument_icon_size[0] + self.spaceBetween + each_len * tk + (
                self.section_size[0] + self.section_space) * ti,
                     self.instrument_y + int((self.instrument_icon_size[1] - self.section_size[1]) / 2) +
                     (self.instrument_icon_size[1] + self.instrument_vspace) * tj)

        size = QtCore.QSize(each_len - self.block_space, self.section_size[1])

        self.create_group(each[0], tj, ti, tk, each[1], pos, size)
    # end

    def create_group(self, judge, line, section, beat, style, pos, size):
        if judge == 0:
            timg_reader = QtGui.QImageReader(f"{self.image_path}{self.block_false_name}")
        else:
            timg_reader = QtGui.QImageReader(f"{self.image_path}{self.block_true_name}")
        timg_reader.setScaledSize(size)
        timg_reader = timg_reader.read()

        pix_item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap(timg_reader))
        text_item = QtWidgets.QGraphicsTextItem(f"{style}")
        text_item.setFont(QtGui.QFont("Arial", 15))

        group = PianoGraphicsItemGroup()
        group.line = line
        group.section = section
        group.beat = beat
        group.style = style
        group.addToGroup(pix_item)
        group.addToGroup(text_item)

        self.scene.addItem(group)
        group.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)

        group.setPos(pos)

        # group.action1.triggered.connect(self.rightMenuAdd)
        group.action2.triggered.connect(self.rightMenuDel)
        group.action_ll.triggered.connect(self.addll)
        group.action_l.triggered.connect(self.addl)
        group.action_s.triggered.connect(self.adds)
        group.action_ss.triggered.connect(self.addss)

        return group
    # end

    def viewKeyEvent(self, key_name, style=""):
        if key_name == "add" or key_name == "D":
            if key_name == "add":
                judge = 1
            elif key_name == "D":
                judge = 0
            if self.scene.selectedItems():
                for item in self.scene.selectedItems():
                    item_rect = item.boundingRect()
                    item_pos = item.pos()
                    size = QtCore.QSize(int(item_rect.width()), self.section_size[1])

                    if judge == 1:
                        f_style = style
                    else:
                        f_style = ""

                    group = self.create_group(judge, item.line, item.section, item.beat, f_style, item_pos, size)

                    self.scene.removeItem(item)
                    group.setSelected(True)
                    self.music[group.section][group.line][group.beat][0] = judge
                    self.music[group.section][group.line][group.beat][1] = f_style
                    x = group.section * 4 + group.beat
                    modify_str = ""
                    i = 0
                    for a_item in self.music[group.section]:
                        if a_item[group.beat][0] == 1:
                            if modify_str != "":
                                modify_str = modify_str[:len(modify_str) - 1] + " "
                            tmp = [i, x + 1, a_item[group.beat][1]]
                            modify_str += piano.coordinate_to_text(tmp)
                        i += 1
                    self.modify_dict[x] = modify_str
                    print(self.modify_dict)
        elif key_name == "W" or key_name == "S":
            if key_name == "W" and self.cur_scale * self.change_scale < self.max_scale:
                self.cur_scale *= self.change_scale
                self.graphicsview_result.scale(self.change_scale, self.change_scale)
            elif key_name == "S" and self.cur_scale / self.change_scale > self.min_scale:
                self.cur_scale /= self.change_scale
                self.graphicsview_result.scale(1 / self.change_scale, 1 / self.change_scale)
    # end

    def modify_event(self, modify_dict):
        with open(f"{self.text_path}piano_text.txt", "r", encoding="utf-8") as f:
            old_text = f.read()
        new_text = old_text.split('\n')
        for k, v in modify_dict.items():
            if 0 <= k < len(new_text):
                new_text[k] = v
        with open(f"{self.text_path}piano_text.txt", "w", encoding="utf-8") as f:
            for line in new_text:
                if len(line) == 0:
                    f.write(line + "\n")
                elif line[-1] == "\n":
                    f.write(line)
                else:
                    f.write(line + "\n")
    # end

    def enter_event(self):
        self.player.stop()
        audio = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(""))
        self.player.setMedia(audio)
        self.modify_event(self.modify_dict)
        self.modify_dict = {}
        arrange.arrange(self.ai_creater.song, "piano")
    # end

    def play_event(self):
        audio = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(f"{self.audio_path}track_piano.WAV"))
        self.player.setMedia(audio)
        self.player.play()
    # end

    def rightMenuAdd(self, style=""):
        self.viewKeyEvent("add", style)
    # end

    def rightMenuDel(self):
        self.viewKeyEvent("D")
    # end

    def addll(self):
        self.rightMenuAdd("ll")

    def addl(self):
        self.rightMenuAdd("l")

    def adds(self):
        self.rightMenuAdd("s")

    def addss(self):
        self.rightMenuAdd("ss")

    def AI_user_send(self):
        user_text = self.textEdit_user.toPlainText()
        if user_text != "":
            self.pushButton_usersend.setEnabled(False)
            self.textBrowser_AIanswer.append("你：" + user_text + "\n\n")
            self.textEdit_user.clear()
            self.ai_answer.user_text = user_text
            self.ai_answer.start()
    # end

    def AI_answer(self, ai_text):
        final_text = "AI：" + ai_text
        final_text += "\n\n"
        self.textBrowser_AIanswer.append(final_text)
        self.pushButton_usersend.setEnabled(True)
    # end


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 使尺寸一致
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    QtGui.QGuiApplication.setHighDpiScaleFactorRoundingPolicy(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_teal.xml")  # 设置样式表
    Form = MusicWidget()
    ui = Piano_Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
