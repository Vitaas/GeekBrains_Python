'''Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой'''

class OwnError(Exception):
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    @staticmethod
    def incorrect(param_1, param_2):
        try:
            return (param_1 / param_2)
        except ZeroDivisionError:
            print("На ноль делить нельзя")

res = OwnError(10, 0)
print(OwnError.incorrect(10, 5))
print(OwnError.incorrect(10, 3.2))
print(res.incorrect(100, 0))
