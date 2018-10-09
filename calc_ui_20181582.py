from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout


class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]
        for i in range(10):
            self.digitButton[i] = Button(str(i), self.buttonclicked)
        """
        self.digitButton[1] = Button('1', self.buttonclicked)
        self.digitButton[2] = Button('2', self.buttonclicked)
        self.digitButton[3] = Button('3', self.buttonclicked)
        self.digitButton[4] = Button('4', self.buttonclicked)
        self.digitButton[5] = Button('5', self.buttonclicked)
        self.digitButton[6] = Button('6', self.buttonclicked)
        self.digitButton[7] = Button('7', self.buttonclicked)
        self.digitButton[8] = Button('8', self.buttonclicked)
        self.digitButton[9] = Button('9', self.buttonclicked)
        """
        # . and = Buttons
        self.decButton = Button('.', self.buttonclicked)
        self.eqButton = Button('=', self.buttonclicked)

        # Operator Buttons
        self.mulButton = Button('*', self.buttonclicked)
        self.divButton = Button('/', self.buttonclicked)
        self.addButton = Button('+', self.buttonclicked)
        self.subButton = Button('-', self.buttonclicked)

        # Parentheses Buttons
        self.lparButton = Button('(', self.buttonclicked)
        self.rparButton = Button(')', self.buttonclicked)

        # Clear Button
        self.clearButton = Button('C', self.buttonclicked)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()
        a = 3
        b = 0
        numLayout.addWidget(self.digitButton[0], 3, 0)
        for i in range(1, 10):
            numLayout.addWidget(self.digitButton[i], (9 - i) / 3, (i - 1) % 3)
        """
        numLayout.addWidget(self.digitButton[1], 2, 0)
        numLayout.addWidget(self.digitButton[2], 2, 1)
        numLayout.addWidget(self.digitButton[3], 2, 2)
        numLayout.addWidget(self.digitButton[4], 1, 0)
        numLayout.addWidget(self.digitButton[5], 1, 1)
        numLayout.addWidget(self.digitButton[6], 1, 2)
        numLayout.addWidget(self.digitButton[7], 0, 0)
        numLayout.addWidget(self.digitButton[8], 0, 1)
        numLayout.addWidget(self.digitButton[9], 0, 2)
        """
        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        opLayout = QGridLayout()

        opLayout.addWidget(self.mulButton, 0, 0)
        opLayout.addWidget(self.divButton, 0, 1)
        opLayout.addWidget(self.addButton, 1, 0)
        opLayout.addWidget(self.subButton, 1, 1)

        opLayout.addWidget(self.lparButton, 2, 0)
        opLayout.addWidget(self.rparButton, 2, 1)

        opLayout.addWidget(self.clearButton, 3, 0)

        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

    def buttonclicked(self):
        button = self.sender()
        key = button.text()
        if key == '=':
            result = str(eval(self.display.text()))
            self.display.setText(result)
        elif key == 'C':
            self.display.setText("")
        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
