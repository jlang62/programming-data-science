
# There is a list of words present, out of which our interpreter will choose 1 random word.
# The user first has to input his/her name
# Then, will be asked to guess any alphabet.
# If the random word (selected by the computer) contains that alphabet,
# it will be shown as the output(with correct placement).
# Else the program will ask you to guess another alphabet.
# The user will be given 12 turns (which can be changed accordingly)
# to guess the complete word

import random

print("Welcome to Word Guessing Game")
name = input("Enter your name: ")
print("Good Luck {}!".format(name))

words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print("Guess the characters")

guesses = ''

turns = 12

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("\nYou Win")
        print("The word is: ", word)
        break

    guess = input("\nGuess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")