import unittest
from PyNumGuess_Core import PyNumGuess_Core

class TestPyNumGuessCoreMethods(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_generate_answer(self):
        """
        Test that the answer is randomly generate and is between 1 and
        the upper bound. Test 100 iterations
        """
        upper_bound = 1000
        core = PyNumGuess_Core(upper_bound)
        for i in range(100):
            with self.subTest(i):
                answer = core.generate_random_answer()
                self.assertLess(answer, upper_bound+1, "The answer is higher than the upper bound!")
                self.assertGreater(answer, 1, "The answer generated is less than 1!")

    def test_evaluate_guess(self):
        """
        Tests that the evaulate guess function returns the correct values
        depending on the guess.
        1 if the answer is higher than the guess,
        0 if the guess is correct,
        -1 if the answer is lower than the guess.
        """
        upper_bound = 1000
        core = PyNumGuess_Core(upper_bound)
        correct_answer = core._answer
    
        for i in range(1, correct_answer):
            """
            Answer is more than guess so shold return -1
            """
            with self.subTest(i):
                evaluated = core.evaluate_guess(i)
                self.assertEqual(evaluated, 1, f"Failed to return 1! Returned {evaluated}")
        for i in range(correct_answer + 1, upper_bound):
            """
            Answer is less than guess so shold return 1
            """
            with self.subTest(i):
                evaluated = core.evaluate_guess(i)
                self.assertEqual(evaluated, -1, f"Failed to return -1! Returned {evaluated}")
        """
        Answer is correct should return 0
        """
        evaluated = core.evaluate_guess(correct_answer)
        self.assertEqual(evaluated, 0, f"Failed to return 0! Returned {evaluated}")


    def test_get_clue(self):
        """
        Test the clue mechanism
        provide a clue to the player in the form of a multiple or a fraction
        e.g the player guesses 10 and the answer is 210
        -> return 21 to show that the answer is >= 21x the guess
        or the player guesses 550 and the answer is 5
        -> return -110 to show the answer is <= 1/110
        """ 
        upper_bound = 1000
        core = PyNumGuess_Core(upper_bound)
        correct_answer = 100
        core._answer = correct_answer

        """
        First test for when the answer is a multiple of the last guess
        """
        for i in range(1, correct_answer - 10):
            with self.subTest(i):
                core.evaluate_guess(i)
                multiple = int(correct_answer / i)
                self.assertEqual(core.get_clue(), multiple, f"Did not return the correct multiple, returned {core.get_clue}")

        """
        Next test for when the answer is a fraction of the last guess
        """
        for i in range(600, correct_answer + 200, -1):
            with self.subTest(i):
                core.evaluate_guess(i)
                multiple = int(i / correct_answer) * -1
                self.assertEqual(core.get_clue(), multiple, f"Did not return the correct multiple, returned {core.get_clue()}")



    def test_update_score(self):
        """
        Test that the score updating mechanic works. core._score should change by 
        the value supplied to update_score
        """
        upper_bound = 1000
        core = PyNumGuess_Core(upper_bound)
        for i in range(1, 100):
            with self.subTest(i):
                core.update_score(-1)
                self.assertEqual(core._score, 100 - i, f"Score did not update correctly, score was {core._score}")

    def test_can_continue(self):
        """
        Test that the can continue method stops the game when the score is <= 0
        """
        upper_bound = 1000
        core = PyNumGuess_Core(upper_bound)
        core.update_score(-99)
        self.assertTrue(core.can_continue(), f"Can_continue stopped the game early with score at {core._score}")
        core.update_score(-1)
        self.assertFalse(core.can_continue(), f"Can_continue stopped the game late with score at {core._score}")

if __name__ == '__main__':
    unittest.main()