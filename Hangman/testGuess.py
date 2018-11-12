import unittest

from Hangman.guess import Guess

class TestGuess(unittest.TestCase):
    # 초기 설정!
    def setUp(self):
        self.g1 = Guess('default')
        self.g2 = Guess('original')

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

        # g2로 실험
        self.assertEqual(self.g2.displayCurrent(), '________')
        self.g2.guess('a')
        self.assertEqual(self.g2.displayCurrent(), '______a_')
        self.g2.guess('i')
        self.assertEqual(self.g2.displayCurrent(), '__i_i_a_')
        self.g2.guess('o')
        self.assertEqual(self.g2.displayCurrent(), 'o_i_i_a_')


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

    def testFinished(self):
        self.g1.guess('d')
        self.assertFalse(self.g1.finished())
        self.g1.guess('e')
        self.assertFalse(self.g1.finished())
        self.g1.guess('f')
        self.assertFalse(self.g1.finished())
        self.g1.guess('a')
        self.assertFalse(self.g1.finished())
        self.g1.guess('u')
        self.assertFalse(self.g1.finished())
        self.g1.guess('l')
        self.assertFalse(self.g1.finished())
        self.g1.guess('t')
        self.assertTrue(self.g1.finished())

    def testGuess(self):
        self.assertTrue(self.g1.guess('d'))
        self.assertFalse(self.g1.guess('z'))
        self.assertTrue(self.g1.guess('e'))
        self.assertFalse(self.g1.guess('q'))
        self.assertTrue(self.g1.guess('f'))
        self.assertFalse(self.g1.guess('v'))

    def testOneChar(self):
        self.assertTrue(self.g1.oneChar('a'))
        self.assertFalse(self.g1.oneChar('dsadawdqeqdsadawd'))
        self.assertTrue(self.g2.oneChar('z'))
        self.assertFalse(self.g2.oneChar(''))

    def testSmallLetterChar(self):
        self.assertTrue(self.g1.smallLetterChar('a'))
        self.assertFalse(self.g1.smallLetterChar('종강종강종강종강종강종강종강'))
        self.assertFalse(self.g1.smallLetterChar('A'))
        self.assertTrue(self.g2.smallLetterChar('z'))
        self.assertFalse(self.g2.smallLetterChar(''))


    def testalreadyChar(self):
        self.assertTrue(self.g1.alreadyChar('u'))
        self.g1.guess('u')
        self.assertFalse(self.g1.alreadyChar('u'))
        self.assertTrue(self.g1.alreadyChar('v'))
        self.g1.guess('v')
        self.assertFalse(self.g1.alreadyChar('v'))
        self.assertTrue(self.g2.alreadyChar('q'))
        self.g2.guess('q')
        self.assertFalse(self.g2.alreadyChar('q'))
        self.assertTrue(self.g2.alreadyChar('p'))
        self.g2.guess('p')
        self.assertFalse(self.g2.alreadyChar('p'))




if __name__ == '__main__':
    unittest.main()