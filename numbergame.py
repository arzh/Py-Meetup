#!/usr/bin/python
import random
import sys

firstrun = True 

no_list = ['no', 'n', 'exit']
yes_list = ['yes', 'y', 'of course']

def is_no(string):
  return string.lower() in no_list

def is_yes(string):
  return string.lower() in yes_list


while True:
  if firstrun:
    msg = 'Would you like to play a game?\t'
    firstrun = False
  else:
    msg = 'Would you like to play again?\t'
   
  play_input = raw_input(msg)

  if is_yes(play_input):
    master_number = random.randint(1, 10)
    while True:
      guessed_str = raw_input("What is your guess?\t")

      if is_no(guessed_str):
	sys.exit()

      try:
        guessed_int = int(guessed_str)
      except:
	continue

      if guessed_int == master_number:
        print "SHIT you go it right\n"
        break
      else:
        lose_msg = "HAHA! WRONG! "
        if guessed_int < master_number:
          lose_msg += "My number is higher\n"
        else:
          lose_msg += "My number is lower\n"

        print lose_msg
  elif is_no(play_input):
    sys.exit()
  else:
    print '\n........\nWhat?\n'
      

