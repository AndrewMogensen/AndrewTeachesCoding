import unittest

from src.lesson1 import *
from test.utilities import *


class Lesson1Test(unittest.TestCase):

    def test_set_five(self):
        self.assertEqual(5, set_x_to_five())

    def test_get_name(self):
        self.assertNotEquals(0, len(get_name()), msg="You did not set a name.")

    def test_say_hello(self):
        hello_str = say_hello()
        print(hello_str)
        self.assertEqual("Hello " + get_name() + "!", hello_str)

    def test_format_last_comma_first_simple(self):
        formatted = format_last_comma_first("first", "last")
        self.assertEqual("last, first", formatted)

    def test_format_last_comma_first_complex(self):
        first = get_random_string(6)
        last = get_random_string(8)
        formatted = format_last_comma_first(first, last)
        self.assertEqual(last + ", " + first, formatted)

    def test_is_even(self):
        for i in range(-100, 100):
            self.assertEqual(i % 2 == 0, is_even(i))
