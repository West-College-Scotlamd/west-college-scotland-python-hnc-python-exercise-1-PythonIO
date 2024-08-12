import unittest
from unittest.mock import patch
import io
import sys

class TestGreeting(unittest.TestCase):

    @patch('builtins.input', return_value='Sarah')
    def test_greeting_sarah(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            # Simulate running the student's script
            import assignment
            # Check the output
            self.assertEqual(fake_stdout.getvalue().strip(), "Hello Sarah")

    @patch('builtins.input', return_value='John')
    def test_greeting_john(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            # Reload the module to reset any state
            import importlib
            import assignment
            importlib.reload(assignment)
            # Check the output
            self.assertEqual(fake_stdout.getvalue().strip(), "Hello John")

if __name__ == '__main__':
    unittest.main()
