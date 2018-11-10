import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_______')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '___a___')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '___a__t')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '___au_t')
        # 한글 입력 방지 확인
        self.g1.guess('ㅁ')
        self.assertEqual(self.g1.displayCurrent(), '___au_t')

    def testDisplayGuessed(self):

        self.g1.guess('a')
        self.assertListEqual(['a'], self.g1.displayGuessed())
        self.g1.guess('t')
        self.assertListEqual(['a', 't'], self.g1.displayGuessed())
        self.g1.guess('u')
        self.assertListEqual(['a', 't', 'u'], self.g1.displayGuessed())
        # sorted 정상 작동 확인
        self.g1.guess('d')
        self.assertListEqual(['a', 'd', 't', 'u'], self.g1.displayGuessed())



if __name__ == '__main__':
    unittest.main()