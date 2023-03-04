import os
import sys
import imgbank
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QGridLayout, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = "Image Viewer"
        self.setWindowTitle(self.title)

        label = QLabel(self)
        pixmap = QPixmap('2335520.jpeg')
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())


        self.label_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 100))
        self.label_5.setMaximumSize(QSize(100, 100))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setPixmap(QPixmap(u":/newPrefix/2335520.jpeg"))
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(False)
        self.label_5.setOpenExternalLinks(True)

    def select_directory(self):
        return None


class ImageGrid(QGridLayout):
    def __init__(self):
        super().__init__()


def main():

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()