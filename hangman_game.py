import random

# List of predefined words
words = ["python", "apple", "tiger", "house", "train"]

# Select random word
word = random.choice(words)

# Create blank spaces
guessed_word = ["_"] * len(word)

# Maximum wrong guesses
attempts = 6
guessed_letters = []

print("Welcome to Hangman Game")

while attempts > 0 and "_" in guessed_word:
    
    print("\nWord:", " ".join(guessed_word))
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    # check if already guessed
    if guess in guessed_letters:
        print("You already guessed this letter")
        continue

    guessed_letters.append(guess)

    # check letter in word
    if guess in word:
        print("Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong Guess!")
        attempts -= 1

# Result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
