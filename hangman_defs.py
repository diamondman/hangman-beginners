def intro_screen():
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


def build_game():
  f=open('words_list.txt')
  words=f.readlines()
  f.close
  from random import choice
  secret=choice(words)
  guesslist=[]
  failcount=0
  donecount=0
  blank='*'*(len(secret)-1)
  game_play(True)


def game_play(keep_on):  
  guesslist.sort()
  print(('\n')*5)
  print(blank)
  print('You have guessed: %s'%guesslist)
  print('You have %s strikes left.'%(6-failcount))
  if keep_on==True:
    guess=input("Guess a letter: ").lower()
    sort_checks()
    is_in_word()
    ask_play_again()


def sort_checks():
  if guess in guesslist:
    print('You already guessed '+guess+'.')
  if len(guess)!=1:
    print('One guess at a time.')
  if not guess.isalpha():
    print('This needs to be a letter dipwad.')
  if guess in secret:
    is_in_word(True)
  else:
    is_in_word(False)


def is_in_word(in_secret):
  if in_secret==True:
    if guess in secret:
      guesslist+=guess
      for i in range(len(secret)):
        if guess==secret[i]:
          blank=blank[:i]+secret[i]+blank[i+1:]
          donecount+=1  
        if donecount==(len(secret)-1):
          print('YOU WIN!!!')
          save_play_history(True)
          get_play_history()
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
  save_play_history(False)
  get_play_history()


def get_play_history():
  f=open('percents', 'r')
  data=f.readlines()
  win=int(data[0][:-1])
  loss=int(data[1][:-1])
  f.close()
  total=win+loss
  if total==0:
    avg='0%'
  else:
    avg=str(round(((win/total)*100), 1))+'%'
  return(win, loss, total, avg)
  print('Wins:'+win+', Losses:'+loss+', Total Games:'+total+', Percent Won:'+avg)


def save_play_history(did_win):
  history=get_play_history()
  win=history[0]
  loss=history[1]
  if did_win==True:
    win+=1
  else:
    loss+=1
  f=open('percents', 'w')
  f.write(str(win)+'\n')
  f.write(str(loss)+'\n')
  f.close()


def ask_play_again():
  play_again=input("Play again? y/n: ")
  keep_on=False
  if play_again!='y':
    print("Well then we're done here.  Fuck off.")
  else:
    print("Sucker!")
    build_game()
