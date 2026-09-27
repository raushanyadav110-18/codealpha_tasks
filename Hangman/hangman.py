import random


# List of predefined words
WORDS = [
    "python",
    "computer",
    "programming",
    "developer",
    "technology"
]


# Display the current progress of the word
def display_word(word, guessed_letters):
    result = ""

    for letter in word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "

    return result.strip()


# Run one complete Hangman game
def play_game():

    word = random.choice(WORDS)
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("\n" + "=" * 45)
    print("          WELCOME TO HANGMAN")
    print("=" * 45)

    print(f"Guess the word! You have {max_attempts} incorrect attempts.")

    while incorrect_guesses < max_attempts:

        print("\nWord:", display_word(word, guessed_letters))
        print("Incorrect guesses:", incorrect_guesses)
        print("Remaining attempts:", max_attempts - incorrect_guesses)

        # Take input from the player
        guess = input("Enter a letter: ").strip().lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue

        # Check repeated guesses
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)

        # Check whether the letter is in the word
        if guess in word:
            print("Correct guess! ✅")

        else:
            incorrect_guesses += 1
            print("Wrong guess! ❌")

        # Check whether the player has guessed the complete word
        if all(letter in guessed_letters for letter in word):
            print("\n" + "=" * 45)
            print("🎉 CONGRATULATIONS! YOU WON!")
            print("The word was:", word)
            print("=" * 45)
            return

    # Player used all attempts
    print("\n" + "=" * 45)
    print("😔 GAME OVER!")
    print("The correct word was:", word)
    print("=" * 45)


# Main program
def hangman():

    print("Welcome to the CodeAlpha Hangman Game!")

    while True:

        play_game()

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

        if play_again not in ["yes", "y"]:
            print("\nThanks for playing Hangman! 👋")
            break


# Start the game
if __name__ == "__main__":
    hangman()