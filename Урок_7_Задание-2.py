'''Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.'''

class Textile:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_my_coat(self):
        return self.width / 6.5 + 0.5

    def get_my_suit(self):
        return self.height * 2 + 0.3

    @property
    def get_full(self):
        return str(f'Общий расход ткани \n'
                   f' {round(self.width / 6.5 + 0.5, 1) + round(self.height * 2 + 0.3, 1)}')


class Coat(Textile):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.my_coat = round(self.width / 6.5 + 0.5, 1)

    def __str__(self):
        return f'Расход ткани на пальто - {self.my_coat}'


class Suit(Textile):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.my_suit = round(self.height * 2 + 0.3, 1)

    def __str__(self):
        return f'Расход ткани на костюм {self.my_suit}'

coat = Coat(500, 150)
suit = Suit(40, 40)
print(coat)
print(suit)
print(coat.get_full)
print(suit.get_full)
