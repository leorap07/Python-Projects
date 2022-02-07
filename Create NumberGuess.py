#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

win = False
guesses = 0
comp_guess = random.randint(1,100)
level = input("Would you like to play on 'easy' or 'hard' mode?")
if level == "easy":
  guesses += 10
elif level == "hard":
  guesses += 5
print(f"you have {guesses} tries to get it right")

while guesses !=0:
  player_choice = int(input("Make your guess:"))
  if player_choice == comp_guess:
    print("Wow, you're good! hehe")
    guesses = 0
    win = True
  else:
    if player_choice > comp_guess:
      print(f"Aww, try again, {player_choice} is too High!")
    else:
      print(f"Aww, try again, {player_choice} is too Low!")
    guesses -= 1
    print(f"you have {guesses} guesses left")

if win == True:
  print("You won the Game, congratulations!")
else:
  print("You must guess better huhu")
