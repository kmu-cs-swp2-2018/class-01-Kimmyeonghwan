import unittest

from Hangman.hangman import Hangman

class TestHangman(unittest.TestCase):

    # 초기 설정
    def setUp(self):
        self.g1 =Hangman()

    def tearDown(self):
        pass
    # Test Case (Case가 하나뿐인 Test suite)
    def testCurrentShape(self):
        # 정상 작동?
        self.assertEqual(self.g1.currentShape(), '''\
   ____
  |    |
  |
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''',)

        self.g1.decreaseLife()
        self.assertEqual(self.g1.currentShape(), '''\
   ____
  |    |
  |    o
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''', )
        self.g1.decreaseLife()
        # 정상 작동 X!
        self.assertNotEqual(self.g1.currentShape(), '''\
   ____
  |    |
  |    o
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''', )



if __name__ == '__main__':
    unittest.main()