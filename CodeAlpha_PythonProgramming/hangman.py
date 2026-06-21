import random
word_list = ["python", "java", "laptop", "apple", "computer", "software"]
chosen_word = random.choice(word_list)
guesses = []
max_attempts = 6
attempts = 0

hangman_stages = [
    """
    ------
    |    |
         |
         |
         |
         |
    """,
    """
    ------
    |    |
    o    |
         |
         |
         |
    """,
    """
    ------
    |    |
    o    |
    |    |
         |
         |
    """,
    """
    ------
    |    |
    o    |
   /|    |
         |
         |
    """,
    """
    ------
    |    |
    o    |
   /|\   |
         |
         |
    """,
    """
    ------
    |    |
    o    |
   /|\   |
   /     |
         |
    """,
     """
    ------
    |    |
    o    |
   /|\   |
   / \   |
         |
    """
]
while True:
    print(hangman_stages[attempts])
    display_word = ""
    for letter in chosen_word:
        if letter in guesses:
            display_word += letter
        else:
            display_word += "_"
    print(f"word: {display_word}")
    if "_" not in display_word:
        print(f"congratulations! you guessed the word: {chosen_word}")

    guess = input("Guess a letter: ").lower()    

    if len(guess) != 1 or not guess.isalpha():
        print("Enter a single letter.")
        continue
    if guess in guesses:
        print("You already guess a letter.")
        continue
    guesses.append(guess)
    
    if guess in chosen_word:
        print("correct!")
    else:
        print("You guessed wrong letter!")
        attempts += 1
    if attempts >= max_attempts:
        print(f"sorry, you are out. the word was:{chosen_word}")
        break 
