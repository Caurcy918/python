rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

game_images = [rock, paper, scissors]

user_choice = int(input("What do you want to play with? Type 0 for Rock, 0 for paper, or 2 for scissors?\n"))
print(game_images[(user_choice)])
computer_choice = random.randint(0, 2)
print(f"the computer chose:{computer_choice}")
print(game_images[computer_choice])

if user_choice == computer_choice:
    print("It's a draw.")

elif (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1) or (user_choice == 1 and computer_choice == 0) or (user_choice == 0 and computer_choice == 1):
    print("You win.")
else:
    print("You lose.")