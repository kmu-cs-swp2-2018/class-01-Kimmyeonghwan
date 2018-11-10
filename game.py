from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())
    english = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
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

        # 글자 1개만 입력
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue

        # 영어 소문자만 입력 받기
        if guessedChar not in english:
            print("Only english! and Only small letter!!")
            continue

        # 이미 입력한 단어 다시 입력 방지 (guessedChar은 입력했던 단어들)
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
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


# 컨트롤러