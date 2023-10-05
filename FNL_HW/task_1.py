class NumeralLists:
    def __init__(self, first_list: list[int | float], second_list: list[int | float]):
        self.first_list = first_list
        self.second_list = second_list

    def get_average(self) -> tuple[float, float]:
        average_1 = 0
        if self.first_list:
            average_1 = sum(self.first_list) / len(self.first_list)
        average_2 = 0
        if self.second_list:
            average_2 = sum(self.second_list) / len(self.second_list)
        return average_1, average_2

    def comparison(self) -> None:
        average_1, average_2 = self.get_average()
        if average_1 > average_2:
            print('Первый список имеет большее среднее значение')
        elif average_1 < average_2:
            print('Второй список имеет большее среднее значение')
        else:
            print('Средние значения равны')