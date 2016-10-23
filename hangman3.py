from random import choice

f=open('words_list.txt')
words=f.readlines()
f.close

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

def show_hangman(failcount):
  if failcount==0:
    print(('\n')*6)
  elif failcount==1:
    print('  x x  '+('\n'*5))
  elif failcount==2:
    print('  x x  ')
    print('   n  '+('\n'*4))
  elif failcount==3:
    print('  x x  ')
    print('   n  ')
    print(' \\_|_/ '+('\n'*3))
  elif failcount==4:
    print('  x x  ')
    print('   n  ')
    print(' \\_|_/ ')
    print('   |  '+('\n'*2))
  elif failcount==5:
    print('  x x  ')
    print('   n  ')
    print(' \\_|_/ ')
    print('   |  ')
    print('  / \\ '+'\n')
  elif failcount==6:
    print('  x x  ')
    print('   n  ')
    print(' \\_|_/ ')
    print('   |  ')
    print('  / \\ ')
    print(' d   b ')

def is_guess_valid(guess, secret, guesslist):
  if len(guess)!=1:
    print('One guess at a time.')
    return False

  if not guess.isalpha():
    print('This needs to be a letter dipwad.')
    return False

  if guess in guesslist and secret:
    print('You already guessed %s.'%guess)
    return False

  return True

def hangman():
  while True:
    secret = choice(words).strip()
    guesslist = []
    failcount = 0
    donecount = 0
    blank ='*'*len(secret)
    while True:
      guesslist.sort()
      show_hangman(failcount)
      print(blank)
      print('You have guessed: %s'%guesslist)
      print('You have %s strikes left.'%(5-failcount))
      guess=input("Guess a letter: ").lower()

      if not is_guess_valid(guess, secret, guesslist):
        continue

      guesslist += guess

      if guess in secret:
        for i in range(len(secret)):
          if guess == secret[i]:
            blank = blank[:i] + secret[i] + blank[i+1:]
            donecount+=1
      else:
        print('Nope! %s strikes left,' % (5-failcount))
        failcount += 1

      if failcount==6:
        show_hangman(failcount)
        print('GAME OVER....the secret word was: '+secret+'.')
        break
      elif donecount == len(secret):
        print('YOU WIN!!!')
        break

    if input("Play again? y/n: ") != 'y':
      break


#THE BEGINNING OF IT ALL
hangman_intro()
hangman()
