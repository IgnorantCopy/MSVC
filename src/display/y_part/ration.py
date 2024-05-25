import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QCoreApplication, Qt


class MyWindow(QWidget):
    def resizeEvent(self, event):
        # 获取当前窗口大小
        size = self.size()

        # 宽高比为2:1
        ratio = 2

        if size.width() / size.height() > ratio:
            new_width = size.height() * ratio
            self.resize(new_width, size.height())
        elif size.width() / size.height() < ratio - 0.1:
            new_height = int(size.width() / ratio)
            self.resize(size.width(), new_height)


if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 使尺寸一致

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
