# Hangman Game 🎮  

## Overview  
The **Hangman Game** is a simple text-based word-guessing game implemented in Python. The player has to guess a randomly selected word by guessing one letter at a time. The game ends when the player either correctly guesses the word or runs out of attempts.  

## Features  
✅ Randomly selects a word from a predefined list  
✅ Allows users to guess one letter at a time  
✅ Limits the number of incorrect guesses (6 attempts)  
✅ Displays progress as the user guesses letters  
✅ Provides feedback on correct and incorrect guesses  
✅ Shows the correct word if the user loses  

## How to Play  
1. Run the Python script.  
2. The game will display underscores representing the letters of a secret word.  
3. Guess one letter at a time.  
4. If the guessed letter is correct, it will be revealed in the word.  
5. If the guessed letter is incorrect, you lose one attempt.  
6. The game ends when you either guess the word correctly or run out of attempts.  

## Requirements  
- Python 3.x  
- No additional libraries needed  

## How to Run  
1. Open a terminal or command prompt.  
2. Navigate to the folder containing **hangman.py**.  
3. Run the script using:  
   ```sh
   python hangman.py

Example Gameplay

Welcome to Hangman!  
_ _ _ _ _  

Guess a letter: p  
Good guess!  
p _ _ _ _  

Guess a letter: z  
Wrong guess! 5 attempts left.  
p _ _ _ _  

Guess a letter: y  
Good guess!  
p y _ _ _

Author

Developed by Jayapriya

License

This project is open-source and available under the MIT License.
