class Guess:

    def __init__(self, word):
        self.numTries = 0
        self.guessedChars = []
        self.secretWord = word
        self.life = 0
        # 사용자 편의를 위해 - 를 _ 로 변경
        self.currentStatus = "_"*len(self.secretWord)


    def display(self):
        print("Current :", self.currentStatus)
        print("Tries : ", self.numTries)
        print("Guessd Chars : ", self.guessedChars)


    def guess(self, character):
        # 단어가 추측했던 단어(guessedChars)에 없다면 추가
        if character not in self.guessedChars:
            self.guessedChars.append(character)

        # 단어가 정답의 단어와 다르면 목숨 -1
        if character not in self.secretWord:
            self.life += 1

        # 단어가 정답의 단어와 같으면
        else:
            for i in range(len(self.secretWord)):
                if self.secretWord[i] == character:
                    self.currentStatus = self.currentStatus[:i] + character + self.currentStatus[i+1:]

            # 단어를 다 맞추면 True 리턴
            if self.secretWord == self.currentStatus:
                return True
        self.numTries = len(self.guessedChars)
# 모델