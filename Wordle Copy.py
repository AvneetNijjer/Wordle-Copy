"""
This program is a Wordle type game called WordP13, where the user attempts to guess a target word 
chosen randomly from a list of valid words in a txt file. Then the player will recieve feedback after each guess, 
indicating correct and partially correct letters until they get it correct.

How to play the game:
- The target word is randomly chosen from a predefined list of words in 'targets.txt'.
- The player enters guesses, which must be valid words from 'legal.txt' 
- THen Feedback is provided for each guess:
  - '*' indicates the letter is in the correct position.
  - '?' indicates the letter is in the word but in a different position.
  - '_' indicates the letter is not in the word at all.
- Incorrectly guessed letters are displayed to help the player avoid repeating them.

Functions used in the game:
- load_words: Loads and validates words from a file.
- choose_word: Selects a random index for the target word.
- update_letters: Tracks which letters are incorrect based on guesses.
- score_guess: Evaluates the guess and provides feedback on each letter.
- play_wordP13: Main function to play the game, handling user input and game flow.
"""


import random

def load_words(filename):
    
    """Loads words from a given file and validates their format.
    Returns a list of valid words if the file is formatted correctly and 
    returns a boolean False if any word fails validation.
    """
    
    file = open(filename)
    words = []
    length = len(file.readline().strip()) # Get the length of the first word 
    
    #Read each line in the file and validate each word
    for line in file:
        row = line.strip()
        words.append(row)
        
        if not row.isalpha(): # Check if word contains only letters 
            return False
        elif len(row) != length: #Check if it matches the expected length
            return False
    if words == []:
        return False # Return False if no words were loaded
    
    return words #Return list of valid words


def choose_word(wordlist):
    
    """Randomly selects an index from the word list.
    Argument is word_list (list): List of words to select from.
    Returns an int which is the random index of the chosen word, 
    or False if the list is empty.
    """
    
    if not wordlist:
        return False
    index = random.randint(0, (len(wordlist) - 1)) #Get a random index
    return index  #Return the index

def update_letters(letters, target, guess):
    
    """Updates the letters list to mark letters not in the target word.

    It has 3 argument's
        letters - Boolean list tracking which letters are incorrect.
        target_word - The target word to be guessed.
        guessed_word - The player's current guess.

    Returns a list with updated letters list with incorrect letters marked as False.
    """
    
    target = target.lower()
    guess = guess.lower() #Ensure case-insensitivity
    
    for letter in guess:
        index = ord(letter) - ord('a') # Convert letter to an index (0-25)
        
        # If letter is not in target, mark it as incorrect
        if letter not in target:
            letters[index] = False
            
    return letters # Return updated list of letters


#Evaluates the guess, providing feedback for each letter
def score_guess(guess, target, words):
    
    """Checks the player's guess, and gives feedback on each letter.

    Arguments:
        guess - The word guessed by the player.
        target - The target word to match.
        words - List of valid words for guesses.

    Returns:
        Feedback string for each letter in the guess.
        False if the guess is invalid.
    """
    
    target = target.lower()
    guess = guess.lower() #Ensure case-insensitivity
    
    #Check if guess is valid (in words list and correct length)
    if guess not in words or len(guess) != len(target):
        return False
    
    #If guess matches target exactly, indicate correct guess
    if guess == target:
        return "*****"
    
    final = "" #Store feedback for each letter
    guessed = [False] * len(target) #Track any matched letters
    
    #Loop through each letter in the guess
    for i in range(len(guess)):
        if guess[i] == target[i]:
            final += "*"
            guessed[i] = True
            
        elif guess[i] in target:
            matched = False
            
            #Check for misplaced letters
            for j in range(len(target)):
                if target[j] == guess[i] and not guessed[j]:
                    final += "?"
                    guessed[j] = True
                    matched = True
                   
            if not matched:
                final += "_"
        else:
            final += "_"
    
    return final # Return feedback string for current guess

def print_signature():
    
    """Prints student information and course details."""
    
    print("Avneet Singh Nijjer")
    print("400567604 - Engineering 1")
    print("ENGINEER 1P13A: Integrated Cornerstone Design Projects in Engineering")
    print("Professor: Sam Scott")
    print("Term: Fall 2024")

def play_wordP13():
    
    """Main function to start and manage the game logic/flow."""
    
    print_signature() #Print the signature 
    print("\nWelcome to WordP13")
    words = load_words("legal.txt") #Load legal words for guessing
    target_index = choose_word(load_words("targets.txt")) #choose target word using index
    target = load_words("targets.txt")[target_index] # Convert the index back into a word/retrive it
    
    letters = [True] * 26  # Initialize all letters as potentially usable
    guess = ""
    
    #Loop until the player guesses the target word
    while guess != target:
        guess = input("Enter your guess (any legal 5-letter word): ").strip().lower()
        
     
        result = score_guess(guess, target, words)
        if result == False:
            print("Invalid guess. Try a 5-letter legal word.")
        else:
          
            print("Result:", result)
            
            letters = update_letters(letters, target, guess)
            
            print("Incorrect letters:", end=" ")
        
            #Update incorrect letters and display them
            for singleletter in range(26):
                if letters[singleletter] == False:
                    print(chr(singleletter + ord('a')), end=" ")
            print()  
            
            #When they win, show statement and end game
            if result == "*****":
                print("Congratulations! You've guessed the word correctly.")
                guess = target  
    
#Calling the main function to start the game
play_wordP13()