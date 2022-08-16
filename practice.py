tries = 0
print (HPICS[tries])?
secret_word= "baboon"
letters = 0
play_again = True

while play_again:
    while tries < 6:
        print("Enter a letter")
        x = input()
        if x not in secret_word:
            tries += 1
            print("you missed")
            print(HPICS[tries])
        else:
            letters += 1
            print ("you guessed right")
            if letters == (len(secret_word)-1):
                print ("you win")
                print ("play again? y/n")
                tries = 6
        if tries == 6:
            print ("you lose")
            print ("play again? y/n")
        again = input()
        if not again.lower().startswith('y'):
            play_again = False
        else:
            tries = 0
            letters = 0
            play_again = True



            