import unittest
from file_processor import get_largest_word_reversed
from io import StringIO
from unittest.mock import patch

# create a decorator which wraps a TestCase method and pass it a mocked stdout object to catch print output
mock_stdout = unittest.mock.patch('sys.stdout', new_callable=StringIO)


class LargestWordReversedTest(unittest.TestCase):

    @mock_stdout
    def test_no_words(self, print_output):
        get_largest_word_reversed("test_files/no_words.txt")
        self.assertEqual(print_output.getvalue().strip(), "File has no words")

    @mock_stdout
    def test_multiple_words_on_single_line(self, print_output):
        get_largest_word_reversed("test_files/multiple_words_on_single_line.txt")
        self.assertEqual(print_output.getvalue().strip(), "There is more than one word per line")

    @mock_stdout
    def test_one_word(self, print_output):
        get_largest_word_reversed("test_files/one_word.txt")
        self.assertEqual(print_output.getvalue().strip(), "anyword\ndrowyna")

    @mock_stdout
    def test_multiple_largest_words_matching(self, print_output):
        get_largest_word_reversed("test_files/multiple_largest_words_matching.txt")
        # Assuming the function will print the first largest word matching
        self.assertEqual(print_output.getvalue().strip(), "largestword1\n1drowtsegral")

    @mock_stdout
    def test_words_with_special_characters(self, print_output):
        self.assertEqual(print_output.getvalue().strip(), "")

    @mock_stdout
    def test_words_with_trailing_spaces(self, print_output):
        get_largest_word_reversed("test_files/one_largest_word_matching.txt")
        self.assertEqual(print_output.getvalue().strip(), "abcde\nedcba")

    @mock_stdout
    def test_one_largest_word_matching(self, print_output):
        get_largest_word_reversed("test_files/one_largest_word_matching.txt")
        self.assertEqual(print_output.getvalue().strip(), "abcde\nedcba")

    @mock_stdout
    def test_one_largest_word_matching_complex(self, print_output):
        get_largest_word_reversed("test_files/one_largest_word_matching_complex.txt")
        self.assertEqual(print_output.getvalue().strip(), "thelargestwordintheuniverse\nesrevinuehtnidrowtsegraleht")


if __name__ == '__main__':
    unittest.main()
