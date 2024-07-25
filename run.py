# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

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

    def display_word(self):
        displayed_word = ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])
        print(displayed_word)

    def play(self):
        while not (self.check_win() or self.check_loss()):
            self.display_word()
            self.display_guessed_letters()
            self.display_remaining_guesses()
            guess = self.get_guess()
            if not self.already_guessed(guess):
                self.update_game_state(guess)
            else:
                print(f"{self.username}, you've already guessed '{guess}'")
        if self.check_win():
            print(f"Congratulations, {self.username}! You've won!")
        else:
            print(f"Sorry, {self.username}. You've lost. The word was '{self.word}'")
        self.restart_game()