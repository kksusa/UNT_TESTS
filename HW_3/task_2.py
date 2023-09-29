# Задание 2. Разработайте и протестируйте метод numberInInterval, который проверяет, попадает ли переданное число
# в интервал (25;100)

def number_in_interval(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError('Аргумент должен быть целым числом')
    return n in range(26, 100)