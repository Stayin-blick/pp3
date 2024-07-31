# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

class Hangman:
    def __init__(self, word: str, name: str, difficulty: str):
        """Start the Hangman game with the given word, player name, and difficulty level."""
        self.name = name
        self.word = word.lower()
        self.guessed_letters = []
        self.wrong_guesses = []
        self.difficulty = difficulty
        self.max_wrong_guesses = self.set_max_wrong_guesses()
        self.remaining_guesses = self.max_wrong_guesses

    def set_max_wrong_guesses(self):
        """Set the maximum number of wrong guesses based on the difficulty level."""
        if self.difficulty == 'medium':
            return 13
        elif self.difficulty == 'hard':
            return 14
        else:
            return 11

    def play(self):
        """Main game loop to handle the gameplay until the player wins or loses."""
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
        """Display the current state of the word being guessed with underscores for unguessed letters."""
        displayed_word = ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])
        print(displayed_word)

    def display_guessed_letters(self):
        """Display the list of letters that have been guessed so far."""
        all_guesses = self.guessed_letters + self.wrong_guesses
        print(f"Guessed Letters: {', '.join(all_guesses)}")

    def display_remaining_guesses(self):
        """Display the number of guesses remaining."""
        print(f"Remaining Guesses: {self.remaining_guesses}")

    def get_guess(self):
        """Prompt the player to guess a letter and validate the input."""
        guess = input(f"{self.name}, please guess a letter: ").lower()
        while not guess.isalpha() or len(guess) != 1:
            guess = input("Invalid input. Please guess a single letter: ").lower()
        return guess

    def update_game_state(self, guess: str):
        """Update the game state based on the player's guess."""
        if guess in self.word:
            self.guessed_letters.append(guess)
        else:
            self.wrong_guesses.append(guess)
            self.remaining_guesses -= 1
            #hangamn diagram to be added

    def check_win(self):
        """Check if the player has won the game by guessing all the letters."""
        return all(letter in self.guessed_letters for letter in self.word)

    def check_loss(self):
        """Check if the player has lost the game by running out of guesses."""
        return self.remaining_guesses <= 0

    def already_guessed(self, guess: str):
        """Check if the letter has already been guessed."""
        return guess in self.guessed_letters or guess in self.wrong_guesses

    def restart_game(self):
        """Prompt the player to restart the game or end it."""
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice == 'yes':
            main()
        else:
            print("Thank you for playing Hangman!")

def load_words(difficulty: str):
    """Load the list of words based on the chosen difficulty level."""
    word_lists = {
        'easy': [ 'bruise', 'forty', 'develop', 'muscle', 'vehicle', 'vegetable'],
        'medium': ['accommodate', 'category', 'competition', 'mischievous', 'lightning', 'opportunity'],
        'hard': ['sentiment' , 'sentiment', 'rehabilitation', 'extraterrestrial', 'prosecution', 'charismatic']
    }
    return word_lists.get(difficulty, [])


def choose_word(words):
    """Select a random word from the list of words."""
    return random.choice(words)

def main():
    """Main function to start the game and get player inputs."""
    print("Welcome to Hangman!")

    # Get the player's name and validate it
    while True:
        name = input("Please enter your name: ").lower()
        if name.isalpha() and len(name) < 11:
            break
        else:
            print("Invalid name. Name should contain only letters and be less than 11 characters.")

    # Get the difficulty level and validate it
    while True:
        difficulty = input("Choose a difficulty (easy, medium, hard): ").lower()
        if difficulty in ['easy', 'medium', 'hard']:
            break
        else:
            print("Invalid difficulty. Choose again (easy, medium, hard).")

    # Load words based on difficulty and start the game
    words = load_words(difficulty)
    word = choose_word(words)
    game = Hangman(word, name, difficulty)
    game.play()

main()