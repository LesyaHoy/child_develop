import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLabel, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from random import randint


class App(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Number100'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.create100NumberGrid()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.okButton = QPushButton('Ok')
        self.okButton.clicked.connect(self.checkAndRefresh)

        windowLayout.addWidget(self.okButton)

        self.setLayout(windowLayout)

        self.show()

    def checkAndRefresh(self):
        self.horizontalGroupBox.re

    def create100NumberGrid(self):
        self.horizontalGroupBox = QWidget()
        layout = QGridLayout()

        randomNumber100 = randint(1, 101)

        for i in range(0, 10):
            for j in range(1, 11):
                title = i*10 + j
                if randomNumber100 == title:
                    layout.addWidget(QTextEdit(),i,j)
                else:
                    layout.addWidget(QLabel(str(title)),i,j)



        self.horizontalGroupBox.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
