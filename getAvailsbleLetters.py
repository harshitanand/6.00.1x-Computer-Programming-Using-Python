def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    availableletters = ""
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            availableletters += i

    return availableletters
