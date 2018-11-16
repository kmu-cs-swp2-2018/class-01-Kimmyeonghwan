class Guess:

    def __init__(self, word):
        self.numTries = 0
        self.secretWord = word
        # 사용자 편의를 위해 - 를 _ 로 변경
        self.currentStatus = "_"*len(self.secretWord)
        self.guessedChars = {''}
        self.english = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



    def guess(self, character):
        self.guessedChars |= {character}
        self.numTries = len(self.guessedChars)

        # 단어가 정답의 단어와 다르면 False 리턴
        if character not in self.secretWord:
            return False

        # 단어가 정답의 단어와 같으면
        else:
            for i in range(len(self.secretWord)):
                if self.secretWord[i] == character:
                    self.currentStatus = self.currentStatus[:i] + character + self.currentStatus[i+1:]
            return True

    # 단어를 다 맞추면 True 리턴
    def finished(self):
        if self.secretWord == self.currentStatus:
            return True
        else:
            return False


    def oneChar(self, char):
        # 글자 1개만 입력
        if len(char) != 1:
            print('One character at a time!')
            return False
        else:
            return True

    def smallLetterChar(self, char):
        # 영어 소문자만 입력
        if char not in self.english:
            print("Only english! and Only small letter!!")
            return False
        else:
            return True

    def alreadyChar(self, char):
        # 이미 입력한 단어 다시 입력 방지 (guessedChar은 입력했던 단어들)
        if char in self.guessedChars:
            print('You already guessed \"' + char + '\"')
            return False
        else:
            return True

    def blankSpacebarChar(self, char):
        if char == "" or char == " " :
            print("You shouldn't Blank and Spacebar!!!!!!!")
            return False
        else:
            return True


    def displayCurrent(self):
        return self.currentStatus


    def displayGuessed(self):
        guessed = ''
        for c in sorted(list(self.guessedChars)):
            guessed += (c + ' ')
        return guessed