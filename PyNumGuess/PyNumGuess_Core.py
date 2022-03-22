import random
from turtle import update

class PyNumGuess_Core():
    def __init__(self, upper_bound):
        self.upper_bound = upper_bound
        self._score = 100
        self._answer = self.generate_random_answer()
        self.__last_guess = 0

    def generate_random_answer(self):
        """
        Generate the random answer from the upper_bound provided to init.
        """
        return random.randint(1, self.upper_bound)

    def update_score(self, update_by):
        self._score += update_by

    def evaluate_guess(self, guess):
        """
        Evaluate the provided guess against the stored answer and return
        1 if the answer is higher than the guess,
        0 if the guess is correct,
        -1 if the answer is lower than the guess.
        """
        self.__last_guess = guess
        if guess == self._answer:
            return 0
        elif self._answer > guess:
            self.update_score(-5)
            return 1
        elif self._answer < guess:
            self.update_score(-5)
            return -1
        else:
            assert()

    def get_clue(self):
        """
        Provide a clue to the player in the form of a multiple or a fraction
        e.g the player guesses 10 and the answer is 210
        -> return 21 to show that the answer is >= 21x the guess
        or the player guesses 550 and the answer is 5
        -> return -110 to show the answer is <= 1/110
        """
        if self.__last_guess > self._answer:
            clue = int(self.__last_guess / self._answer) * -1
            return clue
        elif self.__last_guess < self._answer:
            clue = int(self._answer / self.__last_guess)
            return clue
        else:
            return 0


    def can_continue(self):
        """
        Returns true if the score is above 0 and false if not
        """
        if self._score <= 0:
            return False
        else:
            return True

