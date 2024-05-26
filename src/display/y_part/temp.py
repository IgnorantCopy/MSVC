    def fucs_set(self, Form):
        # 设置大小
        self.style_set()

        # some variables
        ai_text = "AI：你好，有什么问题?\n\n"
        self.textBrowser_AIanswer.setPlainText(ai_text)
        self.ai_worker = AIWorker("")
        # set textedit default text
        self.textEdit_user.setPlaceholderText("请输入你的问题：")
        # set comboBox's items
        self.comboBox_style.addItem("流行")
        self.comboBox_style.addItem("摇滚")
        self.comboBox_style.addItem("爵士")
        self.comboBox_style.addItem("金属")
        self.comboBox_style.addItem("前卫")
        # end
        # 连接到方法
        self.pushButton_create.clicked.connect(self.create_sender)

        self.pushButton_usersend.clicked.connect(self.AI_user_send)

        self.pushButton_userdel.clicked.connect(self.textEdit_user.clear)
        # end


    def style_set(self):
        # 设置字体
        font_size = 30
        for item in [self.pushButton_menu, self.pushButton_help, self.pushButton_close, self.pushButton_usersend,
                     self.pushButton_userdel]:
            item.setStyleSheet(f"font-size: {font_size}px")
        for item in [self.label_style, self.label_speed, self.label_section, self.label_ATtitle, self.label,
                     self.label_result, self.label_result_container]:
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


    def create_sender(self):
        self.speed = self.spinBox_speed.value()
        self.style = self.comboBox_style.currentText()
        self.section = self.spinBox_section.value()

        self.label_result_container.setText(f"要求：速度为{self.speed},风格为{self.style},小节为{self.section}")


    def AI_user_send(self):
        user_text = self.textEdit_user.toPlainText()
        if user_text != "":
            self.pushButton_usersend.setEnabled(False)
            self.textBrowser_AIanswer.append("你：" + user_text + "\n\n")
            self.textEdit_user.clear()
            self.ai_worker.user_text = user_text
            self.ai_worker.sinEnd.connect(self.AI_answer)
            self.ai_worker.start()


    def AI_answer(self, ai_text):
        final_text = "AI：" + ai_text
        final_text += "\n\n"
        self.textBrowser_AIanswer.append(final_text)
        self.pushButton_usersend.setEnabled(True)


class AIWorker(QtCore.QThread, QtCore.QObject):  # 自定义信号，执行run()函数时，从线程发射此信号
    sinEnd = QtCore.pyqtSignal(str)

    def __init__(self, user_text, parent=None):
        QtCore.QThread.__init__(self, parent)
        QtCore.QObject.__init__(self, parent)
        self.user_text = user_text

    def run(self):
        ai_text = common.call_with_messages(common.prompt_default, self.user_text)
        self.sinEnd.emit(ai_text)


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 使尺寸一致
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    QtGui.QGuiApplication.setHighDpiScaleFactorRoundingPolicy(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_teal.xml")  # 设置样式表
    Form = QtWidgets.QWidget()
    ui = Drum_Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
