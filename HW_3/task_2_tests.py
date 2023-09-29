import unittest
from task_2 import number_in_interval


class TestNumberInInterval(unittest.TestCase):

    def test_in_interval(self):
        self.assertTrue(number_in_interval(26), 'Тест на принадлежность интервалу провален')

    def test_out_of_interval(self):
        self.assertFalse(number_in_interval(115), 'Тест на нахождение за пределами интервала провален')

    def test_not_int(self):
        self.assertRaisesRegex(TypeError, 'Аргумент должен быть целым числом', number_in_interval, n=116.7)