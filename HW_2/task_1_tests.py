# Задание 1. Проект Vehicle. Написать следующие тесты с использованием unittest:

import unittest
from task_1 import Vehicle, Car, Motorcycle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car('Audi', 'Q8', 2023)
        self.motorcycle = Motorcycle('Ducati', 'Superleggera V4', 2023)

    # - Проверить, что экземпляр объекта Car также является экземпляром транспортного средства (используя оператор instanceof).
    def test_car_isinstance_vehicle(self):
        self.assertTrue(isinstance(self.car, Vehicle), 'Тест на принадлежность машины к транспортному средству не пройден')

    # - Проверить, что объект Car создается с 4-мя колесами.
    def test_car_creation_with_its_wheels(self):
        self.assertEqual(self.car.num_wheels, 4, 'Тест на наличие в машине 4-х колес не пройден')

    # - Проверить, что объект Motorcycle создается с 2-мя колесами.
    def test_motorcycle_creation_with_its_wheels(self):
        self.assertEqual(self.motorcycle.num_wheels, 2, 'Тест на наличие в мотоцикле 2-х колес не пройден')

    # - Проверить, что объект Car развивает скорость 60 в режиме тестового вождения (используя метод testDrive()).
    def test_car_in_its_test_drive(self):
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60, 'Тест на соответствие скорости передвижения машины не пройден')

    # - Проверить, что объект Motorcycle развивает скорость 75 в режиме тестового вождения (используя метод testDrive()).
    def test_motorcycle_in_its_test_drive(self):
        self.motorcycle.test_drive()
        self.assertEqual(self.motorcycle.speed, 75, 'Тест на соответствие скорости передвижения мотоцикла не пройден')

    # - Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта) машина останавливается (speed = 0).
    def test_car_test_drive_park(self):
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car.speed, 0, 'Тест на остановку машины после передвижения не пройден')

    # - Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта) мотоцикл останавливается (speed = 0).
    def test_motorcycle_test_drive_park(self):
        self.motorcycle.test_drive()
        self.motorcycle.park()
        self.assertEqual(self.motorcycle.speed, 0, 'Тест на остановку мотоцикла после передвижения не пройден')
