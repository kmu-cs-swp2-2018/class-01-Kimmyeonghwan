class Guess:

    def __init__(self, word):
        self.numTries = 0
        self.secretWord = word
        self.life = 0
        # 사용자 편의를 위해 - 를 _ 로 변경
        self.currentStatus = "_"*len(self.secretWord)
        # 집합 vs 리스트, 리스트에 append 해주는 방식을 이용함. 코드 간결화
        self.guessedChars = []



    def guess(self, character):
        self.guessedChars.append(character)
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

    def displayCurrent(self):
        return self.currentStatus


    def displayGuessed(self):
        return sorted(self.guessedChars)