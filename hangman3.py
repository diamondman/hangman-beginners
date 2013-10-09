f=open('words_list.txt')
words=f.readlines()
f.close

from random import choice
secret=choice(words)

questions3=0
while questions3<3:
  play=input('Wanna play hangman? y/n: ')
  questions3 +=1
  if play!='y':
    print('Haha, I must have misheard you.  I SAID:')
  if play=='y':
    break
  if questions3==3:
    print("WRONG.  We're playing now.")
    break

guesslist=[]
failcount=0
donecount=0
blank='*'*(len(secret)-1)
play_on=1
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while play_on==1:
  print(blank)
  guess=input("Guess a letter: ")

  if len(guess)!=1:
    print('Guess one letter dumbass.  And:')

  if guess not in alpha:
    print('Lower case letters, if you please.')


  if guess in alpha:

    if guess in guesslist and secret:
      print('You already guessed '+guess+'.')

    if guess in secret:
      for i in range(len(secret)):
        if guess==secret[i]:
          blank=blank[:i]+secret[i]+blank[i+1:]
          guesslist+=guess
          donecount+=1  

    if guess not in secret:
      if guess in guesslist:
        print('you already guessed '+guess+'.')
      else:   
        print('Nope! '+str(6-failcount)+' strikes left.')
        failcount+=1
        guesslist+=guess
  
  if donecount==(len(secret)-1):
    print('YOU WIN!!!')
    play_on=0 
 
  if failcount>6:
    print('GAME OVER....the secret word was: '+secret+'.')
    play_on=0
