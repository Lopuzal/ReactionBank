import os
import sys
import imgbank
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QGridLayout, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap




def main():

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()