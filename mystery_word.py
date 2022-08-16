import random
from re import T

# right_list = []
# wrong_list = []
# 2 empty lists for "right list" and "wrong list" (DONE)

correct_word = (random.choice(open("words.txt", "r").read().split()))
# print(letters_in_correct_word)

# participant guesses a letter.

# continue guessing until word is complete(win) or 8 tries is complete (lose)


def play_again():
    play_game = input("Do you want to play again (y/n)?")
    if play_game == ("y"):
        guess_letters(correct_word)
    else:
        print("peace out")



def guess_letters(word):
    letters_in_correct_word = ["_" for letter in word]# create a blank board based on the number of letters in the word (DONE)
    wrong_choices = []
    tries = 8
    while tries > 0:
        guess = input("guess a letter ")
        if guess not in word:
            wrong_choices.append(guess)
            tries -= 1
            print(f' Wrong, you have {tries} more tries')# if the guess is wrong, tell players its wrong and move wrong answer into wrong_list. 
            print(f'Wrong choices: {wrong_choices}')
            if tries == 0:
                print("You're a Loser.")
                play_again()
        else:
            for i in range(len(letters_in_correct_word)):# if the letter is in the word, show the letter in "word" and remaining _ (blank spaces)
                if guess == word[i]:
                    letters_in_correct_word[i] = guess
            print(letters_in_correct_word)
            # if word == .join(letters_in_correct_word)


guess_letters(correct_word)

