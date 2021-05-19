import unittest
import scripttest

class TestGame(unittest.TestCase):
    def test_input(self):
        answer = scripttest.run_guess(5, 5)
        self.assertTrue(answer)
    
    def test_input_wrong_guess(self):
        answer = scripttest.run_guess(0, )
        self.assertFalse(answer)
    
    def guess_input_wrong_guess(self):
        answer = scripttest.run_guess(5, 11)
        self.assertFalse(answer)
    
    def guess_input_wrong_type(self):
        answer = scripttest.run_guess(5, '3')
        self.assertFalse(answer)
    
if __name__ == "__main__":
     unittest.main()

    