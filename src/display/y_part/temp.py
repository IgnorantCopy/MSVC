    def fucs_set(self):
        # some variables
        self.user_text = "请输入："
        self.AI_text = "AI：你好，有什么问题?"
        self.textEdit_AIanswer.setPlainText(self.AI_text)
        # set comboBox's items
        self.comboBox_style.addItem("流行")
        self.comboBox_style.addItem("摇滚")
        self.comboBox_style.addItem("爵士")
        self.comboBox_style.addItem("金属")
        self.comboBox_style.addItem("前卫")
        # end
        # create way
        self.pushButton_create.clicked.connect(self.create_sender)

        self.pushButton_usersend.clicked.connect(self.AI_user_send)

        self.pushButton_userdel.clicked.connect(self.textEdit_user.clear)
        # end

    def create_sender(self):
        self.speed = self.spinBox_speed.value()
        self.style = self.comboBox_style.currentText()
        self.section = self.spinBox_section.value()

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_result_container.setFont(font)
        self.label_result_container.setText(f"要求：速度为{self.speed},风格为{self.style},小节为{self.section}")

    def AI_user_send(self):
        self.user_text = self.textEdit_user.toPlainText()
        self.textEdit_AIanswer.append("你：" + self.user_text + "\n\n")
        self.textEdit_user.clear()
        self.AI_answer()

    def AI_answer(self):
        self.AI_text = "AI："
        if self.user_text == "你好":
            self.AI_text += "我很好，谢谢。"
        else:
            self.AI_text += "我不懂"
        self.AI_text += "\n\n"
        self.textEdit_AIanswer.append(self.AI_text)


if __name__ == "__main__":
    import sys
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 使尺寸一致
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())