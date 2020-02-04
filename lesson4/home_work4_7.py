def fact(n):
    f = 1
    for el in range(1, n):
        f *= el
        yield f
try:
    print([el for el in fact(int(input('введите число: ')))])
except ValueError:
    print('введено не число!')