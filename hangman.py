class Hangman:

    text = [

'''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |   / \\
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |   /
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |    o
  |   /|
  |    |
  |
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |    o
  |    |
  |    |
  |
 _|_
|   |______
|          |
|__________|\
''',

'''\
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
''',

'''\
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
''',

    ]


    def getLife(self):
        return len(self.text) - 1


    def get(self, life):
        return self.text[life]

# 뷰?
