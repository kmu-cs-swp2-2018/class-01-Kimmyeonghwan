from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton

from Hangman.hangman import Hangman
from Hangman.guess import Guess
from Hangman.word import Word


class HangmanGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize word database
        self.word = Word('words.txt')

        # Hangman display window
        self.hangmanWindow = QTextEdit()
        self.hangmanWindow.setReadOnly(True)
        self.hangmanWindow.setAlignment(Qt.AlignLeft)
        font = self.hangmanWindow.font()
        font.setFamily('Courier New')
        self.hangmanWindow.setFont(font)

        # Layout
        hangmanLayout = QGridLayout()
        hangmanLayout.addWidget(self.hangmanWindow, 0, 0)

        # Status Layout creation
        statusLayout = QGridLayout()

        # Display widget for current status
        self.currentWord = QLineEdit()
        self.currentWord.setReadOnly(True)
        self.currentWord.setAlignment(Qt.AlignCenter)
        font = self.currentWord.font()
        font.setPointSize(font.pointSize() + 8)
        self.currentWord.setFont(font)
        statusLayout.addWidget(self.currentWord, 0, 0, 1, 2)

        # Display widget for already used characters
        self.guessedChars = QLineEdit()
        self.guessedChars.setReadOnly(True)
        self.guessedChars.setAlignment(Qt.AlignLeft)
        self.guessedChars.setMaxLength(52)
        statusLayout.addWidget(self.guessedChars, 1, 0, 1, 2)

        # Display widget for message output
        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignLeft)
        self.message.setMaxLength(52)
        statusLayout.addWidget(self.message, 2, 0, 1, 2)

        # Input widget for user selected characters
        self.charInput = QLineEdit()
        self.charInput.setMaxLength(1)
        # 엔터키 눌러도 됨.
        self.charInput.returnPressed.connect(self.guessClicked)
        statusLayout.addWidget(self.charInput, 3, 0)

        # Button for submitting a character
        self.guessButton = QToolButton()
        self.guessButton.setText('Guess!')
        self.guessButton.clicked.connect(self.guessClicked)
        statusLayout.addWidget(self.guessButton, 3, 1)

        # Button for a new game
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        self.newGameButton.clicked.connect(self.startGame)
        statusLayout.addWidget(self.newGameButton, 4, 0)

        # Layout placement
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(hangmanLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 0, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle('Hangman Game')

        # Start a new game on application launch!
        self.startGame()


    def startGame(self):
        self.hangman = Hangman()
        self.guess = Guess(self.word.randFromDB())
        self.gameOver = False
        # 방법2. 단어의 길이가 길어서 다 보이지 않을 때, QLineEdit 길이 늘리기.
        if (len(self.guess.secretWord) >= 16):
            self.currentWord.setFixedWidth(15 * (len(self.guess.secretWord)))

        self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
        self.currentWord.setText(self.guess.displayCurrent())
        self.guessedChars.setText(self.guess.displayGuessed())
        self.message.clear()
        print(self.guess.secretWord)


    def guessClicked(self):
        guessedChar = self.charInput.text()
        self.charInput.clear()
        self.message.clear()


        if self.gameOver == True:
            self.message.setText("Game Over! Good Game!")


        while True:

            if self.guess.finished() == True:
                self.message.setText("plz Click the New Game!")
                break

            # 공백과 띄어쓰기를 입력했는지 판단하고, 맞는 경우 메시지 출력, 리턴
            if self.guess.blankSpacebarChar(guessedChar) == False:
                self.message.setText("You shouldn't Blank and Spacebar!")
                break

            # 입력의 길이가 1 인지를 판단하고, 아닌 경우 메시지 출력, 리턴
            if self.guess.oneChar(guessedChar) == False:
                self.message.setText("One character at a time!")
                break

            # 이미 사용한 글자인지를 판단하고, 아닌 경우 메시지 출력, 리턴
            if self.guess.alreadyChar(guessedChar) == False:
                self.message.setText('You already guessed \"' + guessedChar + '\"')
                break

            # 영어 소문자만 입력했는지 판단하고, 아닌 경우 메시지 출력, 리턴
            if self.guess.smallLetterChar(guessedChar) == False:
                self.message.setText("Only english! and Only small letter!!")
                break

            success = self.guess.guess(guessedChar)
            if success == False:
                # 남아 있는 목숨을 1 만큼 감소
                self.hangman.decreaseLife()
                self.message.setText("Wrong answer! life - 1!")
            else:
                self.message.setText('There is \"' + guessedChar + '\" in the sentence.')
            break


        # hangmanWindow 에 현재 hangman 상태 그림을 출력
        self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
        # currentWord 에 현재까지 부분적으로 맞추어진 단어 상태를 출력
        self.currentWord.setText(self.guess.displayCurrent())
        # guessedChars 에 지금까지 이용한 글자들의 집합을 출력
        self.guessedChars.setText(self.guess.displayGuessed())


        if self.guess.finished():

            # 메시지 ("Success!") 출력하고, self.gameOver 는 True 로
            self.message.setText("Success!")
            print("============================")
            print("Success")
            print("Tries : {}".format(self.guess.numTries))
            print("SecretWord is {}".format(self.guess.secretWord))
            print("============================")
            self.gameOver = True
            pass

        elif self.hangman.getRemainingLives() == 0:
            # 메시지 ("Fail!" + 비밀 단어) 출력하고, self.gameOver 는 True 로
            self.message.setText("Fail! SecreWord is {}".format(self.guess.secretWord))
            print("============================")
            print('Fail')
            print('SecretWord is [{}]'.format(self.guess.secretWord))
            print('guess {}'.format(self.guess.guessedChars))
            print('Tries : {}'.format(self.guess.numTries))
            print("============================")
            self.gameOver = True
            pass


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = HangmanGame()
    game.show()
    sys.exit(app.exec_())

