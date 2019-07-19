import sys
import os
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QVBoxLayout, \
    QGridLayout, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QFontMetrics, QIntValidator, QFontDatabase, QFont
from PyQt5.QtCore import Qt

__name__ = '__main__'


class Number100Dlg(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Number100'
        self.init_ui()
        self.adjustSize()

    def init_ui(self):

        #QtGui.QApplication.translate

        font_db = QFontDatabase()
        font_path = os.path.realpath("fonts/KBREINDEERGAMES.ttf")
        font_id = font_db.addApplicationFont(font_path)

        #families = font_db.applicationFontFamilies(font_id)

        #for font_family in families:
        #    print(font_family)


        self.nice_font = QFont("KBREINDEERGAMES", 38)

        self.okButton = QPushButton('Ok')
        self.horizontalGroupBox = QWidget()

        self.setWindowTitle(self.title)

        self.numbersGridLayout = QGridLayout()
        self.fillIn100NumberGrid()

        dialogLayout = QVBoxLayout()
        dialogLayout.addWidget(self.horizontalGroupBox)
        self.okButton.clicked.connect(self.checkResult)

        dialogLayout.addWidget(self.okButton)

        self.setLayout(dialogLayout)

        self.show()


    def checkResult(self):
        userInputText = int(self.absentNumberTextField.text())
        msg = QMessageBox()

        if userInputText == self.currentAbsentNumber100:
            msg.setInformativeText("Correct! Lets play again!")
            msg.exec_()
            self.reload100NumberGrid()
        else:
            msg.setInformativeText("Nice try! Please try again.")
            msg.exec_()

    def reload100NumberGrid(self):
        for i in reversed(range(self.numbersGridLayout.count())):
            self.numbersGridLayout.itemAt(i).widget().deleteLater()
        self.fillIn100NumberGrid()
        self.update()


    def fillIn100NumberGrid(self):
        self.currentAbsentNumber100 = randint(1, 100)

        self.absentNumberTextField = QLineEdit()
        self.absentNumberTextField.setValidator(QIntValidator(1, 99));
        self.absentNumberTextField.setMaxLength(2)
        fontMetrics = QFontMetrics(self.nice_font);
        textDimension = 3 * fontMetrics.averageCharWidth();


        self.absentNumberTextField
        for i in range(0, 10):
            for j in range(1, 11):
                title = i * 10 + j
                if self.currentAbsentNumber100 == title:

                    self.absentNumberTextField.setFixedSize(textDimension,textDimension)
                    self.numbersGridLayout.addWidget(self.absentNumberTextField, i, j)
                    self.absentNumberTextField.setAlignment(Qt.AlignCenter)
                    self.absentNumberTextField.setFont(self.nice_font)
                else:
                    numberLabel = QLabel(str(title))
                    numberLabel.setStyleSheet("background-color: white; border: 1px inset grey;font-family:KBREINDEERGAMES;")
                    numberLabel.setFixedSize(textDimension,textDimension)
                    numberLabel.setAlignment(Qt.AlignCenter)
                    numberLabel.setFont(self.nice_font)
                    self.numbersGridLayout.addWidget(numberLabel, i, j)

        self.horizontalGroupBox.setLayout(self.numbersGridLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Number100Dlg()
    sys.exit(app.exec_())
