import unittest
from task_1 import even_odd_number


class TestEvenOddNumber(unittest.TestCase):

    def test_even(self):
        self.assertTrue(even_odd_number(16), 'Тест на четность провален')

    def test_odd(self):
        self.assertFalse(even_odd_number(27), 'Тест на нечетность провален')