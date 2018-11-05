import random

class Word:

    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        # 한 줄씩 읽기
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            # 공백 없애기
            word = line.rstrip()
            self.words.append(word)
            self.count += 1

        # 단어 갯수 알려주기
        print('%d words in DB' % self.count)


    # 이건 뭐지?
    def test(self):
        return 'default'

    # 랜덤 난수로 단어 고르기
    def randFromDB(self):
        r = random.randrange(self.count)
        return self.words[r]

# 모델