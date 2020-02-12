class Complex_number:

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Complex_number(self.number + other.number)

    def __mul__(self, other):
        return Complex_number(self.number * other.number)

c_1 = Complex_number(1+2j)
c_2 = Complex_number(2+1j)
print(c_1.number, c_2.number)
c_3 = c_1 + c_2
c_4 = c_1 * c_2
print(c_3.number)
print(c_4.number)
