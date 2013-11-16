from random import choice

class HangmanGame(object):
  def __init__(self, word=None, hangmanbody=None):
    if hangmanbody is None:
      hangmanbody = [
        '  x x  ',
        '   n  ',
        ' \\_|_/ ',
        '   |  ',
        '  / \\ ',
        ' d   b '
        ]
    self.hangmanbody = hangmanbody

    if word is None:
      word = self.get_random_word()
    self.secret = word
    print("SECRET: '%s'" % self.secret)
    self.guesslist = []
    self.failcount = 0
    self.donecount = 0
    self.blank = '*'*len(self.secret)

  @classmethod
  def get_random_word(cls):
    f=open('words_list.txt')
    words=f.readlines()
    f.close
    word = choice(words)
    if word[-1] == "\n":
      word = word[:-1]
    return word

  def play_game(self):
    while True:
      self.guesslist.sort()
      self.show_hangman()
      print(self.blank)
      print('You have guessed: %s' % self.guesslist)
      print('You have %s strikes left.' % (6-self.failcount))

      guess=input("Guess a letter: ").lower()
      
      if not self.is_guess_valid(guess):
        continue
  
      self.guesslist += guess

      if guess in self.secret:
        for i in range(len(self.secret)):
          if guess == self.secret[i]:
            self.blank = self.blank[:i] + self.secret[i] + self.blank[i+1:]
            self.donecount+=1
      else:
        print('Nope! %s strikes left,' % (5-self.failcount))
        self.failcount += 1

      print('\n')

      if self.failcount == 6:
        self.show_hangman()
        print("GAME OVER....the secret word was '%s'." % self.secret)
        break
      elif self.donecount == len(self.secret):
        print("YOU WIN!!!  The word was '%s'." % self.secret)
        break

  def is_guess_valid(self, guess):
    if len(guess)!=1:
      print('One guess at a time.')
      return False
    
    if not guess.isalpha():
      print('This needs to be a letter dipwad.')
      return False
  
    if guess in self.guesslist and self.secret:
      print('You already guessed %s.'%guess)
      return False
    
    return True

  def show_hangman(self):
    if self.failcount > 0:
      print("\n".join(self.hangmanbody[0:self.failcount]))
    if self.failcount<6:
      print('\n'*(5-self.failcount))


def hangman_intro():
  questions3=0
  while questions3<3:
    play=input('Wanna play hangman? y/n: ')
    questions3 +=1
    if play=='y':
      break
    else:
      print('Haha, I must have misheard you.  I SAID:')
    if questions3==3:
      print("WRONG.  We're playing now.")
      break





#THE BEGINNING OF IT ALL
hangman_intro()
while True:
  hangmaninstance = HangmanGame()
  hangmaninstance.play_game()
  print("YOU ARE PLAYING AGAIN! DO IT BETTER THIS TIME!")
