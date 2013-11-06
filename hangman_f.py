def build_world():
  #from docs import word lists, random, functions

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

def game_play():
  secret=choice(words)
  guesslist=[]
  failcount=0
  donecount=0
  blank='*'*(len(secret)-1)
  #call next functions

sort_checks
number
alpha
guess list

in_word

not_in_word


play_history
play_again


