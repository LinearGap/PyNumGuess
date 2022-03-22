from PyNumGuess_Core import PyNumGuess_Core as Core
import argparse

class PyNumGuess():
    def __init__(self):
        self.__upper_bound = 0
        self.__parse_args()
        self.__running = True
    
    def __parse_args(self):
        """
        Parse the command line arguments and update the necessary variables within.
        """
        parser = argparse.ArgumentParser("A Higher/Lower number guessing game!")
        # Upper bound sets the difficulty by defining how high the random number can be.
        parser.add_argument("-d", action='store', default=100, type=int, help="The upper bound of the random number generated!")
        args = parser.parse_args()
        # Set the upper bound of the game for the difficulty from the d flag at CLI, or the default of 100
        self.__upper_bound = args.d

    def run(self):
        """
        The main loop of the application itself.
        """
        while(self.__running):
            self.__core_setup()
            correct = self.__first_guess()
            if correct:
                self.__correct_answer()
                self.__reset()
                continue
            while(self.__core.can_continue()):
                correct = self.__step()
                if correct:
                    self.__correct_answer()
                    self.__reset()
                    break
            
            if not self.__core.can_continue():
                self.__game_over()
                self.__reset()
        

        print('Thanks for playing :)')
        return 0

    def __core_setup(self):
        """
        Setup the PyNumGuess_Core
        """
        self.__core = Core(self.__upper_bound)
        self.__core.generate_random_answer()

        print(f"Game has begun with a random number between 1 and {self.__upper_bound}!")

    def __first_guess(self):
        """
        Make the first guess and return true if its correct and false if not
        """
        valid = False
        while(not valid):
            guess = input('Take your first guess:')
            if guess.isdigit():
                valid = True

        result = self.__core.evaluate_guess(int(guess))
        return self.__check_answer(result)

    def __step(self):
        """
        Step through the game taking input from the user and calling the core
        """
        valid = False
        while(not valid):
            user_input = input('Take another guess(or type c for a clue):')
            if user_input == 'c':
                self.__get_clue()
                return False
                valid = True
            elif user_input.isdigit():
                result = self.__core.evaluate_guess(int(user_input))
                return self.__check_answer(result)
                valid = True

    def __check_answer(self, result):
        """
        Use the core, check if the guess is correct, higher, or lower than the
        correct answer
        """
        if result == 0:
            return True
        elif result == 1:
            print('You need to guess higher than that!')
            return False
        elif result == -1:
            print('Go lower next time around!')
            return False

    def __get_clue(self):
        """
        Get a clue and give to the user!
        """
        clue_val = self.__core.get_clue()
        if clue_val > 0:
            print(f'The correct answer is {clue_val}x your last guess')
        elif clue_val < 0:
            print(f'The correct answer is 1/{clue_val*-1} your last guess')



    def __correct_answer(self):
        """
        The last guess was correct. Congratulate the player and offer the chance to play again
        """
        print("Awesome! Thats the right answer! Well Done!")
        print(f"You scored {self.__core._score}")

    def __game_over(self):
        """
        The game is over, the players score hit zero so they had to stop.
        """
        print('GAME OVER! You ran out of points!')

    def __reset(self):
        """
        Reset the game, allow the player to change the difficulty or stop all together.
        """
        valid = False
        while(not valid):
            user_input = input('Do you want to play again Y/N?')
            if user_input == 'Y' or user_input == 'N' or user_input == 'y' or user_input == 'n':
                valid = True
        if user_input == 'N' or user_input == 'n':
            self.__running = False


def main():
    """
    Run the PyNumGuess class loop runner
    """
    guesser = PyNumGuess()
    guesser.run()
    return 0

if __name__ == '__main__':
    main()