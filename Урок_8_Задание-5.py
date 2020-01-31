'''Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.'''

class Warehouse:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_warehouse = []
        self.my_equipment = {'Наименование': self.name, 'Стоимость': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def new_division(self, name, price, quantity):
        list_equipment = {'Наименование': name, 'Стоимость': price, 'Количество': quantity}
        self.my_equipment(list_equipment)
        self.my_equipment.update(list_equipment)
        self.my_warehouse.append(self.my_equipment)
        print(f'Список перемещения -\n {self.my_warehouse}')

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
print(equip_1.new_division())
print(equip_2.new_division())
print(equip_1.to_print())
