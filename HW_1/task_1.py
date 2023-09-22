# Задание 1.
# В классе Calculator создайте метод calculateDiscount, который принимает сумму покупки и процент скидки и возвращает сумму с учетом скидки.
# Ваша задача - проверить этот метод с использованием библиотеки AssertJ. Если метод calculateDiscount
# получает недопустимые аргументы, он должен выбрасывать исключение ArithmeticException.
# Не забудьте написать тесты для проверки этого поведения.


class Calculator:

    def discount_calculation(self, sum: float, discount: int) -> float:
        if not (isinstance(sum, int) or isinstance(sum, float)):
            raise ArithmeticError(f'Недопустимое значение {sum}')
        if not (isinstance(discount, int) and (discount in range(101))):
            raise ArithmeticError(f'Недопустимое значение {discount}')
        total_amount = sum * (100 - discount) / 100
        return total_amount


if __name__ == '__main__':
    calculator = Calculator()
    print(calculator.discount_calculation(1234.5, 12))
