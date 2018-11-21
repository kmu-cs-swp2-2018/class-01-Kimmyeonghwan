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
            # 방법1. 데이터 베이스를 읽을 때, 긴 길이의 단어를 차단.
            if (len(word)) <= 16:
                self.words.append(word)
                self.count += 1

        # 단어 갯수 알려주기
        print('%d words in DB' % self.count)


    # 테스트 케이스용
    def test(self):
        return 'default'

    # 랜덤 난수로 단어 고르기
    def randFromDB(self):
        r = random.randrange(self.count)
        return self.words[r]

