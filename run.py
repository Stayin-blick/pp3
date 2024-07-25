# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

class Hangman:
    def __init__(self, word: str, name: str, difficulty: str):
        self.name = name
        self.word = word.lower()
        self.guessed_letters = []
        self.wrong_guesses = []
        self.difficulty = difficulty
        self.max_wrong_guesses = self.set_max_wrong_guesses()
        self.remaining_guesses = self.max_wrong_guesses

    def set_max_wrong_guesses(self):
        if self.difficulty == 'medium':
            return 13
        elif self.difficulty == 'hard':
            return 14
        else:
            return 11

    def play(self):
        while not (self.check_win() or self.check_loss()):
            self.display_word()
            self.display_guessed_letters()
            self.display_remaining_guesses()
            guess = self.get_guess()
            if not self.already_guessed(guess):
                self.update_game_state(guess)
            else:
                print(f"{self.name}, you've already guessed '{guess}'")
        if self.check_win():
            print(f"Congratulations, {self.name}! You've won!")
        else:
            print(f"Sorry, {self.name}. You've lost. The word was '{self.word}'")
        self.restart_game()

    def display_word(self):
        displayed_word = ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])
        print(displayed_word)

    def display_guessed_letters(self):
        print(f"Guessed Letters: {', '.join(self.guessed_letters)}")

    def display_remaining_guesses(self):
        print(f"Remaining Guesses: {self.remaining_guesses}")

    def get_guess(self):
        guess = input(f"{self.name}, please guess a letter: ").lower()
        while not guess.isalpha() or len(guess) != 1:
            guess = input("Invalid input. Please guess a single letter: ").lower()
        return guess

    def update_game_state(self, guess: str):
        if guess in self.word:
            self.guessed_letters.append(guess)
        else:
            self.wrong_guesses.append(guess)
            self.remaining_guesses -= 1

    def check_win(self):
        return all(letter in self.guessed_letters for letter in self.word)

    def check_loss(self):
        return self.remaining_guesses <= 0

    def already_guessed(self, guess: str):
        return guess in self.guessed_letters or guess in self.wrong_guesses

    def restart_game(self):
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice == 'yes':
            main()
        else:
            print("Thank you for playing Hangman!")
    
def choose_word(words):
    return random.choice(words)

def main():
    print("Welcome to Hangman!")

    while True:
        name = input("Please enter your name: ").lower()
        if name.isalpha() and len(name) < 11:
            break
        else:
            print("Invalid name. Name should contain only letters and be less than 11 characters.")

    while True:
        difficulty = input("Choose a difficulty (easy, medium, hard): ").lower()
        if difficulty in ['easy', 'medium', 'hard']:
            break
        else:
            print("Invalid difficulty. Choose again (easy, medium, hard).")

    words = load_words(difficulty)
    word = choose_word(words)
    game = Hangman(word, name, difficulty)
    game.play()

main()