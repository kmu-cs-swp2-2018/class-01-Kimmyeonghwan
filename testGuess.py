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

    def testDisplayGuessed(self):

        self.g1.guess('a')
        self.assertIn('a', self.g1.displayGuessed())


if __name__ == '__main__':
    unittest.main()