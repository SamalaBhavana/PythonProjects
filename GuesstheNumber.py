#Number Guessing Game Objectives:
from GNart import logo
import random

num = random.randint(1,100)
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def play_game():
  print(logo)
  print(" Welcome to the Number Guessing Game! ")
  print(" I'm thinking a number between 1 and 100.")
  type = input("Choose the difficulty. Type 'easy' or 'hard' : ")
  chances = chance(type)
  guess_num(chances)
    

def chance(type):
  if type == 'easy':
    chances = 10
  elif type == 'hard':
    chances = 5
  return chances

def guess_num(chances):
  game = True
  global num
  i=0
  c = chances
  while game:
    print(f"You have {c} attempts remaining to guess the number.")
    number = int(input("Make a guess: "))
    i+=1
    c-=1
    if number < num:
      print("Too low.\nGuess again.")
    elif number > num:
      print("Too high.\nGuess again.")
    elif number == num:
      print(f"You got it. The answer was {num}.")
      game = False
    if i == chances:
      print(f"You run out of guesses. You lost!\n The correct guess is {num}.")
      game = False
      

play_game()
