#### STARTER CODE - PLEASE DO NOT DELETE
from termcolor import colored, cprint
import random
from datetime import date

def get_word_lists():
  valid_answers_file = open('word_answers_list.txt')
  valid_guesses_file = open('valid_guesses_list.txt')
  # Pre-seeded with AAVE words
  aave_wordlist = ["munch", "bouta", "finna", "tweak", "glaze", "extra"]
  valid_answers_list = []
  valid_guesses_list = []

  for word in valid_answers_file:
    valid_answers_list.append(word.strip())
  for word in valid_guesses_file:
    valid_guesses_list.append(word.strip())

  valid_answers_list.extend(aave_wordlist)
  valid_guesses_list.extend(aave_wordlist)

  return [valid_answers_list, valid_guesses_list]

def get_target_word(wordlist):
  today = date.today()
  random.seed(today)
  return random.choice(wordlist).upper()
  

def check_word_valid(word, wordlist):
  return word.lower() in wordlist
  
def print_letter_color(letter, color):
  '''
    Prints the letter marked with the specified color.
    This will make your program look more like the wordle
    that we are familiar with.

    The only defaul options for coloring the text in
    your program are:
      - green
      - yellow
      - grey
    
    Please note:
      Subsequent calls of this function prints letters all on same line.
  '''
  if color == "yellow":
    print(colored(letter, "white", "on_yellow"), end = ' ')
  elif color == "grey":
    print(colored(letter, "white", "on_grey"), end = ' ')
  elif color == "green":
    print(colored(letter, "white", "on_green"), end = ' ')

def guesses(number_of_guesses):
  if number_of_guesses >= 6:
    print("\nOut of guesses. Please play again!\n")

  elif number_of_guesses < 6:
    print("\nYou have " + str(number_of_guesses) + " guesses left!\n")
  return number_of_guesses

   
def wordle():
 
  target_word = get_target_word(get_word_lists()[0])
  guess_number = 6
  five_letter_word = ""

  #list_of_target_words = ["munch", "bouta", "finna", tweak, "glaze", "extra"]

  while five_letter_word != target_word and guess_number >= 0:

    five_letter_word = input("Please enter a word.\n").upper()
    if check_word_valid(five_letter_word, get_word_lists()[1]) == False:
      print("Invalid Guess, try again")
    else:
      guess_number = guess_number - 1
        # First Guess - Parameter - Equal -> Target Word
      if five_letter_word == target_word:
        print("\nCongratulations! It took you " + str(6-guess_number) + " tries.\n")
        for i in range(len(five_letter_word)):
          print_letter_color(target_word[i], "green")
    
      else:
        for i in range(len(five_letter_word)):
          if five_letter_word[i] == target_word[i]:
            print_letter_color(five_letter_word[i], "green")
          
          elif five_letter_word[i] in target_word and i != target_word[i]:
            print_letter_color(five_letter_word[i], "yellow")
    
          elif five_letter_word[i] not in target_word:
            print_letter_color(five_letter_word[i], "grey") 
    
        
  
        guesses(guess_number)
      

wordle()
