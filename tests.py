import unittest
from unittest.mock import patch
from io import StringIO
from WordleSolver import mainloop

class TestWordleSolver(unittest.TestCase):
    @patch("sys.stdin", StringIO("карт\nбона\nnnny\nхрип\nygnn\n"))
    @patch("sys.stdout", new_callable=StringIO)
    def test_mainloop(self, mock_stdout):
        mainloop()
        expected_phrases = [
            "Enter one of next words:",
            "Found 5 available words",
            "Different masks: 3",
            "Please, type one of next words:",
            "Found 3 available words",
            "Different masks: 3",
            "Please, type one of next words:",
            "Found available words",
            "Your word is",
        ]
        actual_output = mock_stdout.getvalue().split('\n')
        for phrase in expected_phrases:
            self.assertIn(phrase, actual_output)

if __name__ == '__main__':
    unittest.main()
