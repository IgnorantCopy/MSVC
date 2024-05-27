def extra_set(self, Form):
    # 设置风格
    self.style_set()
    # some variables
    ai_text = "AI：你好，有什么问题?\n\n"
    self.textBrowser_AIanswer.setPlainText(ai_text)
    self.ai_answer = AIAnswer("")
    self.image_path = "../image/"
    # set textedit default text
    self.textEdit_user.setPlaceholderText("请输入你的问题：")
    # set spinbox
    self.spinBox_speed.setMinimum(5)
    self.spinBox_speed.setMaximum(50)
    self.spinBox_section.setMinimum(10)
    self.spinBox_section.setMaximum(50)
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

    Form.Key_event.connect(self.createKeyEvent)
    # end


def style_set(self):
    # 设置字体
    font_size = 30
    for item in [self.pushButton_menu, self.pushButton_help, self.pushButton_close, self.pushButton_usersend,
                 self.pushButton_userdel]:
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
    self.block_true_name = "block_true.png"
    self.block_false_name = "block_false.png"
    self.cur_scale = 1.0
    self.min_scale = 0.6
    self.max_scale = 2.5
    self.change_scale = 1.2

    self.instrument_names = ['A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'A']

    self.choose = 0
    # 设置背景
    self.graphicsview_result.setBackgroundBrush(QtCore.Qt.GlobalColor.black)


def create_sender(self):
    self.pushButton_create.setEnabled(False)
    self.scene.clear()
    musiclists = [[{0: "11010", 1: "01010", 5: "11000"}, {0: "110", 2: "010", 3: "111"},
                   {-1: "0010", 0: "1001", 1: "100"}, {-1: "00"}, {-1: "00000000"}],
                  [{0: "11010", 1: "01010", 5: "11000"}, {0: "110", 2: "010", 3: "111"}]]

    self.AI_create_result(musiclists[self.choose])
    self.choose = (self.choose + 1) % 3


def AI_create_result(self, music):
    def set_block(ti, tj, tlen, tj_str):
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
            if tj_str[m] == '0':
                timg_reader = QtGui.QImageReader(f"{self.image_path}{self.block_false_name}")
            else:
                timg_reader = QtGui.QImageReader(f"{self.image_path}{self.block_true_name}")
            timg_reader.setScaledSize(QtCore.QSize(each_len - self.block_space, self.section_size[1]))
            timg_reader = timg_reader.read()
            titem = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap(timg_reader))
            self.scene.addItem(titem)
            titem.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
            titem.setPos(self.instrument_icon_size[0] + self.spaceBetween + each_len * m + (
                        self.section_size[0] + self.section_space) * ti,
                         self.instrument_y + int((self.instrument_icon_size[1] - self.section_size[1]) / 2) +
                         (self.instrument_icon_size[1] + self.instrument_vspace) * tj)

    # 设置graphicsview的大小和初始位置
    self.graphicsview_result.setSceneRect(0, 0, self.instrument_icon_size[0] + self.spaceBetween +
                                          (self.section_size[0] + self.section_space) * len(music) + self.right_space,
                                          self.instrument_y + (self.instrument_icon_size[
                                                                   1] + self.instrument_vspace) * 12 + self.down_space)
    self.graphicsview_result.centerOn(360, 200)

    i = 0
    for name in self.instrument_names:
        img_reader = QtGui.QImageReader(f"{self.image_path}{name}")
        img_reader.setScaledSize(QtCore.QSize(self.instrument_icon_size[0], self.instrument_icon_size[1]))
        img_reader = img_reader.read()
        instrument_item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap(img_reader))
        self.scene.addItem(instrument_item)
        instrument_item.setPos(0, self.instrument_y + i * (self.instrument_icon_size[1] + self.instrument_vspace))
        i += 1

    i = 0
    for section in music:
        max_len = 0
        if -1 in section:
            j_len = len(section[-1])
            for j in range(self.instrument_num):
                set_block(i, j, j_len, "")
        else:
            left_instructions = []
            for j in range(self.instrument_num):
                if j in section:
                    j_str = section[j]
                    j_len = len(j_str)
                    if j_len > max_len:
                        max_len = j_len
                    set_block(i, j, j_len, j_str)

                else:
                    left_instructions += [j]

            for j in left_instructions:
                set_block(i, j, max_len, "")

        i += 1

    self.pushButton_create.setEnabled(True)


def createKeyEvent(self, key_name):
    if key_name == "A" or key_name == "D":
        file = ''
        if key_name == "A":
            file = f"{self.image_path}{self.block_true_name}"
        elif key_name == "D":
            file = f"{self.image_path}{self.block_false_name}"
        if self.scene.selectedItems():
            for item in self.scene.selectedItems():
                item_rect = item.boundingRect()
                item_pos = item.pos()
                img_reader = QtGui.QImageReader(file)
                img_reader.setScaledSize(QtCore.QSize(int(item_rect.width()) - 1, self.section_size[1]))
                img_reader = img_reader.read()
                new_item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap(img_reader))
                self.scene.removeItem(item)
                self.scene.addItem(new_item)
                new_item.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
                new_item.setPos(item_pos)
    elif key_name == "W" or key_name == "S":
        if key_name == "W" and self.cur_scale * self.change_scale < self.max_scale:
            self.cur_scale *= self.change_scale
            self.graphicsview_result.scale(self.change_scale, self.change_scale)
        elif key_name == "S" and self.cur_scale / self.change_scale > self.min_scale:
            self.cur_scale /= self.change_scale
            self.graphicsview_result.scale(1 / self.change_scale, 1 / self.change_scale)


def AI_user_send(self):
    user_text = self.textEdit_user.toPlainText()
    if user_text != "":
        self.pushButton_usersend.setEnabled(False)
        self.textBrowser_AIanswer.append("你：" + user_text + "\n\n")
        self.textEdit_user.clear()
        self.ai_answer.user_text = user_text
        self.ai_answer.sinEnd.connect(self.AI_answer)
        self.ai_answer.start()


def AI_answer(self, ai_text):
    final_text = "AI：" + ai_text
    final_text += "\n\n"
    self.textBrowser_AIanswer.append(final_text)
    self.pushButton_usersend.setEnabled(True)


class DrumWidget(QtWidgets.QWidget):
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

    def __init__(self, require, parent=None):
        QtCore.QThread.__init__(self, parent)
        QtCore.QObject.__init__(self, parent)
        self.require = require

    def run(self):
        pass


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 使尺寸一致
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    QtGui.QGuiApplication.setHighDpiScaleFactorRoundingPolicy(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_teal.xml")  # 设置样式表
    # app.setStyleSheet("") # 重设样式表
    Form = DrumWidget()
    ui = Drum_Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
