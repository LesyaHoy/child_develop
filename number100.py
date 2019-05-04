import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QVBoxLayout, \
    QGridLayout, QLabel, QTextEdit, QMessageBox

__name__ = '__main__'


class Number100Dlg(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Number100'
        self.width = 320
        self.height = 100
        self.init_ui()


    def init_ui(self):

        #QtGui.QApplication.translate

        self.okButton = QPushButton('Ok')
        self.horizontalGroupBox = QWidget()

        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)

        self.numbersGridLayout = QGridLayout()
        self.fillIn100NumberGrid()

        dialogLayout = QVBoxLayout()
        dialogLayout.addWidget(self.horizontalGroupBox)
        self.okButton.clicked.connect(self.checkResult)

        dialogLayout.addWidget(self.okButton)

        self.setLayout(dialogLayout)

        self.show()


    def checkResult(self):
        userInputText = int(self.absentNumberTextField.toPlainText())
        msg = QMessageBox()

        if userInputText == self.currentAbsentNumber100:
            msg.setInformativeText("Correct! Lets play again!")
        else:
            msg.setInformativeText("Nice try! Please try again.")

        msg.exec_()
        self.reload100NumberGrid()


    def reload100NumberGrid(self):
        for i in reversed(range(self.numbersGridLayout.count())):
            self.numbersGridLayout.itemAt(i).widget().deleteLater()
        self.fillIn100NumberGrid()
        self.update()


    def fillIn100NumberGrid(self):
        self.currentAbsentNumber100 = randint(1, 100)

        for i in range(0, 10):
            for j in range(1, 11):
                title = i * 10 + j
                if self.currentAbsentNumber100 == title:
                    self.absentNumberTextField = QTextEdit()
                    self.numbersGridLayout.addWidget(self.absentNumberTextField, i, j)
                else:
                    self.numbersGridLayout.addWidget(QLabel(str(title)), i, j)

        self.horizontalGroupBox.setLayout(self.numbersGridLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Number100Dlg()
    sys.exit(app.exec_())
