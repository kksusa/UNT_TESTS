# Задание 1. Тесты первого задания

from task_1 import Calculator


def test_sum_is_string(calculator: Calculator):
    try:
        calculator.discount_calculation('string_sum', 0)
        raise Exception('Ожидалась ошибка "ArithmeticError", но получился другой результат')
    except Exception as e:
        print(f'Тест на строковую сумму пройден. Ошибка "{e}"')


def test_discount_is_float(calculator: Calculator):
    try:
        calculator.discount_calculation(123, 21.3)
        raise Exception('Ожидалась ошибка "ArithmeticError", но получился другой результат')
    except Exception as e:
        print(f'Тесты на целочисленную скидку пройдены. Ошибка "{e}"')


def test_all_discount(calculator: Calculator):
    for i in range(101):
        assert calculator.discount_calculation(100, i) == 100 * (100 - i) / 100,\
            f'Тесты на все возможные значения скидки не пройдены. Ошибка на проценте {i}'
    print('Тесты на все возможные значения скидки пройдены.')


if __name__ == '__main__':
    calculator = Calculator()
    test_sum_is_string(calculator)
    test_discount_is_float(calculator)
    test_all_discount(calculator)