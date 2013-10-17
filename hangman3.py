f=open('words_list.txt')
words=f.readlines()
f.close
from random import choice

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

while True:
  secret=choice(words)
  guesslist=[]
  failcount=0
  donecount=0
  blank='*'*(len(secret)-1)

  while True:
    print(('\n')*5)
    print(blank)
    print('You have guessed: %s'%guesslist)
    print('You have %s strikes left.'%(6-failcount))
    guess=input("Guess a letter: ").lower()

    if len(guess)!=1:
      print('One guess at a time.  And:')
      
    if not guess.isalpha():
      print('This needs to be a letter dipwad.')
      continue

    if guess in guesslist and secret:
      print('You already guessed '+guess+'.')

    if guess in secret:
      for i in range(len(secret)):
        if guess==secret[i]:
          blank=blank[:i]+secret[i]+blank[i+1:]
          guesslist+=guess
          donecount+=1  
      if donecount==(len(secret)-1):
        print('YOU WIN!!!')
        break

    else:
      if guess in guesslist:
        print('you already guessed '+guess+'.')
      else:   
        print('Nope! '+str(5-failcount)+' strikes left.')
        failcount+=1
        guesslist+=guess
    if failcount==0:
      print(('\n')*6)
    if failcount==1:
      print('  x x  '+('\n'*5))
    if failcount==2:
      print('  x x  ')
      print('   n  '+('\n'*4))
    if failcount==3:
      print('  x x  ')
      print('   n  ')
      print(' \\_|_/ '+('\n'*3))
    if failcount==4:
      print('  x x  ')
      print('   n  ')
      print(' \\_|_/ ')
      print('   |  '+('\n'*2))
    if failcount==5:
      print('  x x  ')
      print('   n  ')
      print(' \\_|_/ ')
      print('   |  ')
      print('  / \\ '+'\n')
    if failcount==6:
      print('  x x  ')
      print('   n  ')
      print(' \\_|_/ ')
      print('   |  ')
      print('  / \\ ')
      print(' d   b ')
      print('GAME OVER....the secret word was: '+secret+'.')
      break

  play_again=input("Play again? y/n: ")
  if play_again!='y':
    break
