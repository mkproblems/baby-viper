# create a greeting
# create a word list
# randomly choose a word from the list
# ask they user to guess a letter
# take the input from the user and make it lowercase
# check if the letter is in the word

import random
import time

print("Welcome to the Whismical World of Hangman! (Morbid I know.. )")
time.sleep(2)

words = ["banjo", "candle", "dolphin", "Frog", "Guitar", "Humming", "Jazz", "Kitten", "Lizard", "Mango", "Napkin", "Octopus", "Pizza", "Quick", "Rabbit", "Sunset", "Tiger", "Umbrella", "Violin", "Wizard", "Xylophone", "Yogurt", "Zebra"]
words = [i.lower() for a,i in enumerate(words)]
secret_word = random.choice(words)
print(secret_word)
print("You get 5 attempts to HANG THIS MAN!")


num = 0
game_over = False

display_word = []
for letter in secret_word:
    display_word += "_"
print(display_word)


while not game_over:
    guess = input("Guess a letter! > ").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
            print("Nice!")
    if guess not in secret_word:
        num += 1
        guesses_left = 5 - num
        print(f"{guesses_left} guesses left!")
        if guesses_left <= 1:
            print("Uh oh!")
        if num >= 5:
            print("Game Over! The man lives.. ")
            game_over = True
    print(display_word)

    if guess == secret_word:
        # put each letter in the correct blank
        print("That's it! YOU WIN!")
        game_over = True

    if "_" not in display_word:
        print("YOU WIN! He is dead.")
        game_over = True

# I want to add a feature that lets you input the whole word and win, AND each letter displays in the right spot