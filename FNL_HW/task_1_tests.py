import pytest

from task_1 import NumeralLists


@pytest.fixture
def list_1():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def list_2():
    return [6, 7, 8, 9, 10]


def test_init(list_1, list_2):
    """Проверка инициализации класса"""
    nums_list = NumeralLists(list_1, list_2)
    assert nums_list.first_list == list_1
    assert nums_list.second_list == list_2


def test_get_average(list_1, list_2):
    """Проверка средних значений списков с размером больше 1"""
    nums_list = NumeralLists(list_1, list_2)
    assert nums_list.get_average() == (3, 8)


@pytest.mark.parametrize('first_list, second_list, result', [([1, 2, 3], [], (2, 0)), ([], [1, 2, 3], (0, 2)), ([], [], (0, 0))])
def test_get_empty_average(first_list, second_list, result):
    """Проверка средних значений, если один или оба списка пустые"""
    nums_list = NumeralLists(first_list, second_list)
    assert nums_list.get_average() == result


@pytest.mark.parametrize('first_list, second_list, result', [([1, 2, 3], [5], (2, 5)), ([5], [1, 2, 3], (5, 2)), ([5], [5], (5, 5))])
def test_get_one_element_lists_averages(first_list, second_list, result):
    """Проверка средних значений, если один или оба списка имеют только один элемент"""
    nums_list = NumeralLists(first_list, second_list)
    assert nums_list.get_average() == result


def test_first_average_more(list_1, list_2, capfd):
    """Проверка сообщения когда среднее значение первого списка больше второго"""
    nums_list = NumeralLists(list_2, list_1)
    nums_list.comparison()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Первый список имеет большее среднее значение'


def test_second_average_more(list_1, list_2, capfd):
    """Проверка сообщения когда среднее значение второго списка больше первого"""
    nums_list = NumeralLists(list_1, list_2)
    nums_list.comparison()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Второй список имеет большее среднее значение'


def test_equal_averages(list_1, capfd):
    """Проверка сообщения когда средние значения списков равны"""
    nums_list = NumeralLists(list_1, list_1)
    nums_list.comparison()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Средние значения равны'
