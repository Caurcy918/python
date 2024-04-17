import random
from hangame_art import stages, logo
from hangame_words import word_list

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)


lives = 6

print(logo)
"""
guess = input("Guess a letter: ").lower()
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
"""
display_word = []
for _ in chosen_word:
        display_word += "_"
"""
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display_word[position] = letter
"""

while "_" in display_word:
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        print(f"You've already guessed {guess}.")
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display_word[position] = letter
        else:
            print("Wrong")

    if guess not in chosen_word:
        
        print(f"You guessed {guess}, that's not in the word. You lose a life!")
        lives -= 1
        if lives == 0:
            print("You lost!")
        
            
    print(f"{' '.join(display_word)}")
    print(stages[lives])