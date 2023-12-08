import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_prompt(self):
        self.assertEqual("(hbnb) ", self.console.prompt)

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('\n')
            self.assertEqual(fake_out.getvalue(), '')

    def tearDown(self):
        pass

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd('quit'))
            expected_output = 'Thank you for using AirBnB clone.\n'
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd('EOF'))
            self.assertEqual(fake_out.getvalue(), '\n')


if __name__ == '__main__':
    unittest.main()
