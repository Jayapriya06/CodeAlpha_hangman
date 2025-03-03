import random

def choose_word():
    words = ["python", "developer", "hangman", "coding", "programming"]
    return random.choice(words)

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6  # Limit incorrect guesses

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.")

        displayed_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
        print(" ".join(displayed_word))

        if "_" not in displayed_word:
            print("Congratulations! You won!")
            break
    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()
