'''Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата'''


class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        str_rep = str(self.re)
        if self.im >= 0:
            str_rep += '+'
        str_rep += str(self.im) + 'i'
        return str_rep

    def __add__(self, other):
        new_re = self.re + other.re
        new_im = self.im + other.im
        return Complex(new_re, new_im)

    def __mul__(self, other):
        if isinstance(other, Complex):
            new_re = self.re * other.re - self.im * other.im
            new_im = self.re * other.im + self.im * other.re
        elif isinstance(other, int) or isinstance(other, float):
            new_re = self.re * other
            new_im = self.im * other
        return Complex(new_re, new_im)

    __rmul__ = __mul__


a = Complex(1, 2)
b = Complex(3, -5)
print(a * b)
print(a * 2)
