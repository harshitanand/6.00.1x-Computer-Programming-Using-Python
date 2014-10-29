def hangman(secretWord):
    print 'Welcome to the game, Hangman!', '\nI am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    lettersGuessed = []
    win = False
    miss = 8
    while True:
        print '-------------'
        if miss == 0:
            print 'Sorry, you ran out of guesses. The word was ' + secretWord + '.'
            break;
        win = isWordGuessed(secretWord, lettersGuessed)
        if win == True:
            print 'Congratulations, you won!'
            break;
        print 'You have ' + str(miss) + ' guesses left.', '\nAvailable letters: ' + getAvailableLetters(lettersGuessed)
        guess = raw_input('Please guess a letter: ').lower()
        if guess in lettersGuessed:
            print 'Oops! You\'ve already guessed that letter: ', getGuessedWord(secretWord, lettersGuessed)
        else:
            lettersGuessed.append(guess)
            lettersGuessed.sort()
            if guess not in secretWord:
                print 'Oops! That letter is not in my word: ',
                miss -= 1
            else:
                print 'Good guess: ',
            print getGuessedWord(secretWord, lettersGuessed)
