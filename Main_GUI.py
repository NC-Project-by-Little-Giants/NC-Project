import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox, QProgressBar, \
    QCheckBox, QStyleFactory, QComboBox, QLabel, QFontDialog, QColorDialog, QFileDialog, QTextEdit, QCalendarWidget


class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        # self.progress = QProgressBar(self)
        # self.btn = QPushButton('download', self)
        self.completed = 0
        self.sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
        self.setGeometry(50, 50, int(self.sizeObject.width() * 0.80), int(self.sizeObject.height() * 0.80))
        print(str(self.sizeObject.width() * 0.80) + ',,,,,' + str(self.sizeObject.height() * 0.80))
        self.setWindowTitle('NC Project')
        self.setWindowIcon(QIcon('D:/NCproject/Background_Images/PythonLogo.png'))
        self.show()


app = QApplication(sys.argv)
Gui = window()
sys.exit(app.exec_())