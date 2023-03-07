import random
from art import logo
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
#a Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

print(logo)
print(
    "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100."
)
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
num = random.randint(0, 100)
print(num)
game_over = True


def main(attemps, num):
    while attemps > 0:
      print(f"You have {attemps} attempts remaining to guess the number.")
      guess_number = int(input("Make a guess: "))
      if guess_number == num:
          print(f"You got it! The answer was {num}.")
          return False
      elif guess_number < num:
          print("Too low")
      elif guess_number > num:
          print("Too high")
      print("Guess again.")
      attemps -= 1
    print(f"You've run out of guesses. The number was {num}.")
    return False

if level == "easy":
    attemps = 10
    while game_over:
        game_over = main(attemps,num)
else:
    attemps = 5 
    while game_over:
        game_over = main(attemps,num)
