from Hangman.hangman import Hangman
from Hangman.guess import Guess
from Hangman.word import Word


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())
    hangman = Hangman()

    while hangman.life > 0:

        # 목숨(단두대)
        display = hangman.currentShape()
        print(display)

        #guess에 있던 display를 가져옴.
        display = guess.displayCurrent()
        print("Current : {}".format(display))
        display = guess.numTries
        print("Tries : {}".format(display))
        display = guess.displayGuessed()
        print('Already Used : {}'.format(display))
        print(guess.secretWord)
        guessedChar = input('Select a letter: ')


        # 해당 부분을 guess로 이동.
        error = guess.oneChar(guessedChar)
        if error == False:
            continue

        error = guess.smallLetterChar(guessedChar)
        if error == False:
            continue

        error = guess.smallLetterChar(guessedChar)
        if error == False:
            continue

        error = guess.alreadyChar(guessedChar)
        if error == False:
            continue


        success = guess.guess(guessedChar)
        if success == False:
            hangman.decreaseLife()

        # 반복문 탈출
        if guess.finished():
            break

    # 성공의 경우, 실패의 경우를 구분하기 위해 한번 더 사용
    if guess.finished() == True:
        print("============================")
        print("Success")
        print("Tries : {}".format(guess.numTries))
        print("SecretWord is {}".format(guess.secretWord))
        print("============================")
    else:
        print(hangman.currentShape())
        print("============================")
        print('Fail')
        print('SecretWord is [{}]'.format(guess.secretWord))
        print('guess {}'.format(guess.guessedChars))
        print('Tries : {}'.format(guess.numTries))
        print("============================")


if __name__ == '__main__':
    gameMain()