class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

    @classmethod
    def number(cls, s):
        try:
            return int(s)
        except ValueError:
            raise OwnError('вводите числа')


my_list = []
while True:
    try:
        number = input('введите число  (Enter - продолжение ввода, #- закончить ввод): ')
        if number == '#':
           break
        my_list.append(OwnError.number(number))
    except OwnError as err:
        print(err)


print(my_list)
