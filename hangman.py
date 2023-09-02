# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    print("-------------------------------")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """

    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    if "_ " not in get_guessed_word(secret_word, letters_guessed):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''

    guessed_word_list = []

    for i in range(len(secret_word)):
        guessed_word_list.append("_ ")

    for index, i in enumerate(secret_word):
        for letter in letters_guessed:
            if letter == i:
                guessed_word_list[index] = letter

    guessed_word = "".join(guessed_word_list)
    return guessed_word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    available_letters_list = []

    for letter in all_letters:
        if letter not in letters_guessed:
            available_letters_list.append(letter)

    available_letters = "".join(available_letters_list)
    return available_letters


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("----------------------------")

    letters_guessed = []

    guesses = 6
    warnings = 3

    print('You have', warnings, 'warnings. You will get a warning if you enter a letter that\nyou have already entered or entering an invalid character.')
    print("----------------------------------------------------------------------")

    while (is_word_guessed(secret_word, letters_guessed) == False) or (warnings > 0) or (guesses > 0):
        print(f'\nYou have {guesses} guesses left.')
        print("Available letters:", get_available_letters(letters_guessed))

        letter = str(input("Please enter a letter: ")).lower()

        if letter in letters_guessed:
            warnings = warnings - 1
            print('This letter has been entered before!. You have', warnings, 'warnings left.')
            print("\n----------------------------")
            print(get_guessed_word(secret_word, letters_guessed))

        elif letter not in letters_guessed:

            letters_guessed.append(letter)

            if letter in secret_word:
                print("Good guess! :", get_guessed_word(secret_word, letters_guessed))
                print("\n----------------------------")

            elif (letter not in secret_word) and (97 <= ord(letter) <= 122):
                guesses = guesses - 1
                print("This letter is not in the secret word!")
                print("\n----------------------------")
                print(get_guessed_word(secret_word, letters_guessed))

            elif ord(letter) < 97 or ord(letter) > 122:
                warnings = warnings - 1
                print('That is not a valid letter!. You have', warnings, 'warning(s) left.')
                print("\n----------------------------")
                print(get_guessed_word(secret_word, letters_guessed))

        if is_word_guessed(secret_word, letters_guessed) == True:
            print(f"You have correctly guessed the word: {secret_word}!")
            print("Thank you for playing, goodbye!!")
            break
        elif warnings <= 0:
            print("\n----------------------------")
            print("You have used up all your warnings!")
            print("Therefore, the game has ended, you lost!")
            print("The secret word was:", secret_word)
            print("Thank you for playing, goodbye!!")
            break
        elif guesses <= 0:
            print("\n----------------------------")
            print("You have used up all your guesses!")
            print("Therefore, the game has ended, you lost!")
            print("The secret word was:", secret_word)
            print("Thank you for playing, goodbye!!")
            break

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    secret_word = 'secret'
    hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)



