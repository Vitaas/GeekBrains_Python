'''Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.'''

class Warehouse:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Equipment:
    def __init__(self, name, model, serial_number):
        self.name = name
        self.model = model
        self.serial_number = serial_number

    def __str__(self):
        print(f'наименование: {self.name}, модель: {self.model}, серийный номер: {self.serial_number}')

class Printer(Equipment):
    def to_print(self):
        return 'Печатать документы'

class Scanner(Equipment):
    def to_scan(self):
        return 'Сканировать документы'

class Xerox(Equipment):
    def to_xerox(self):
        return 'Делать ксерокопии'

equip_1 = Printer('HP', 2200, 123456)
equip_2 = Scanner('Canon', 5760, 654321)
equip_3 = Xerox('Xerox', 7564, 264910001)
# print(equip_1.Warehouse())
# print(equip_2.Warehouse())
# print(equip_3.Equipment())
print(equip_1.to_print())
