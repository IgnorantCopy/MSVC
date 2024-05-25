    def fucs_set(self, Form):
        # 设置大小
        self.style_set()

        # some variables
        self.user_text = ""
        self.AI_text = "AI：你好，有什么问题?\n\n"
        self.textBrowser_AIanswer.setPlainText(self.AI_text)
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
        font_size = 18
        for item in [self.pushButton_menu, self.pushButton_help, self.pushButton_close, self.pushButton_usersend,
                     self.pushButton_userdel]:
            item.setStyleSheet(f"font-size: {font_size}px")
        for item in [self.label_style, self.label_speed, self.label_section, self.label_ATtitle, self.label,
                     self.label_result, self.label_result_container]:
            item.setStyleSheet(f"font-size: {font_size}px")
        for item in [self.spinBox_speed, self.spinBox_section, self.comboBox_style]:
            item.setStyleSheet(f"font-size: {font_size}px")
        for item in [self.textEdit_user, self.textBrowser_AIanswer]:
            item.setStyleSheet(f"font-size: {font_size}px")
        font_size = 35
        self.pushButton_create.setStyleSheet(f"font-size: {font_size}px")
        # 设置颜色
        self.spinBox_speed.setStyleSheet("color:#1de9b6")
        self.comboBox_style.setStyleSheet("color:#1de9b6")
        self.spinBox_section.setStyleSheet("color:#1de9b6")


    def create_sender(self):
        self.speed = self.spinBox_speed.value()
        self.style = self.comboBox_style.currentText()
        self.section = self.spinBox_section.value()

        self.label_result_container.setText(f"要求：速度为{self.speed},风格为{self.style},小节为{self.section}")


def AI_user_send(self):
    self.user_text = self.textEdit_user.toPlainText()
    if self.user_text != "":
        self.textBrowser_AIanswer.append("你：" + self.user_text + "\n\n")
        self.textEdit_user.clear()
        self.AI_answer()


def AI_answer(self):
    self.AI_text = "AI："
    if self.user_text == "你好":
        self.AI_text += "我很好，谢谢。"
    else:
        self.AI_text += "我不懂。"
    self.AI_text += "\n\n"
    self.textBrowser_AIanswer.append(self.AI_text)


if __name__ == "__main__":
    import sys

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 使尺寸一致
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    QtGui.QGuiApplication.setHighDpiScaleFactorRoundingPolicy(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QtWidgets.QApplication(sys.argv)
    dpi = app.primaryScreen().logicalDotsPerInch()
    Form = QtWidgets.QWidget()
    ui = Drum_Ui_Form()
    ui.setupUi(Form)
    apply_stylesheet(app, theme="dark_teal.xml")  # 设置样式表
    Form.show()
    sys.exit(app.exec_())
