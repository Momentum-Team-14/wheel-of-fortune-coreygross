import random


# this is to re-run game.
def play_again():
    play_game = input("Do you want to play again (y/n)?")
    if play_game == ("y"):
        guess_letters()
    else:
        print("peace out")


def guess_letters():
    word = (random.choice(open("words.txt", "r").read().split()))  # the word generated at randon
    letters_in_correct_word = ["_" for letter in word]  # create a blank board based on the number of letters in the word (DONE)
    print(f'the length of the word is {len(word)}')
    wrong_choices = []  # used for putting letters in dict.
    tries = 8  # number of lives
    while tries > 0:
        guess = input("guess a letter ")
        if len(guess) > 1:
            print('input only one letter') 
        elif guess in wrong_choices:
            print("you guessed that already, guess again")
        elif guess not in word:
            wrong_choices.append(guess)
            tries -= 1
            print(f' Wrong, you have {tries} more tries')  # if the guess is wrong, tell players its wrong and move wrong answer into wrong_list. 
            print(f'Wrong choices: {wrong_choices}')  #print wrong choices so they know what they guessed
            if tries == 0:
                print("You're a Loser. The correct word is", word)
                play_again()
        else:
            wrong_choices.append(guess)
            for i in range(len(letters_in_correct_word)):  # if the letter is in the word, show the letter in "word" and remaining _ (blank spaces)
                if guess == word[i]:
                    letters_in_correct_word[i] = guess
            print(letters_in_correct_word)
            if word == "".join(letters_in_correct_word):  ##.join is used to have a string == a list.
                print("winner, winner, chicken-dinner")
                play_again()


guess_letters()