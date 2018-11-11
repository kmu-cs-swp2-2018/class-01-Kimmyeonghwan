import unittest

from Hangman.word import Word

class TestWord(unittest.TestCase):

    def setUp(self):
        self.g1 = Word('words.txt')

    def tearDown(self):
        pass
    # word 파일이 실행되는지 확인
    def testTest(self):
        self.assertEqual(self.g1.test(), 'default')
        self.assertNotEqual(self.g1.test(), 'Kookmin Uni. KMU')

    # 내가 원하는 파일을 열었는지 확인
    def testOpen(self):
        self.assertEqual(self.g1.count, 19184)
        self.assertNotEqual(self.g1.count, 19000)

    # 랜덤 범위가 정상적으로 작동하는지 확인
    def testRandom(self):
        '''
        self.test = False
        ok = 0
        while (ok <= self.g1.testRandFromDB()):
            if 0 < self.g1.testRandFromDB() <= self.g1.count:
                self.test = True
            else:
                self.test = False
            ok += 1
        self.assertTrue(self.test)
        '''
        # 0 < 랜덤 범위 <= 19184
        self.assertGreaterEqual(self.g1.count, self.g1.testRandFromDB()) # 19184 => 랜덤 범위
        self.assertGreater(self.g1.testRandFromDB(), 0) # 랜덤 범위 > 0


if __name__ == '__main__':
    unittest.main()