from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())

    finished = False
    hangman = Hangman()
    maxTries = hangman.getLife()

    while guess.life < maxTries:

        # 목숨(단두대)
        display = hangman.get(maxTries - guess.life)
        print(display)
        guess.display()

        guessedChar = input('Select a letter: ')

        # 영어 1개만 입력
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue

        # 이미 입력한 단어 다시 입력 방지 (guessedChar은 입력했던 단어들)
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue

        # 입력한 알파벳들로 단어를 맞췄는지 확인
        finished = guess.guess(guessedChar)
        if finished == True:
            break

    # 성공!
    if finished == True:
        print('Success')
    else:
        print(hangman.get(0))
        print('word [{}]'.format(guess.secretWord))
        print('guess {}'.format(guess.guessedChars))
        print('Tries : {}'.format(guess.numTries))
        print('Fail')


if __name__ == '__main__':
    gameMain()


# 컨트롤러