import random
AHORCADO = ['''
      +---+
          |
          |
          |
          |
          |
    =========''',
      '''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

def read():
    with open("./ahorcado/words.txt", "r", encoding="utf-8") as file:
        all_wods = file.read()
        words = list(map(str, all_wods.split()))
    return(random.choice(words))

    