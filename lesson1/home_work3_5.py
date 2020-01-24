summ = 0
ex = False
while not ex:
    stroka = input('введите число через пробел (Enter - продолжение ввода, #- закончить ввод): ')
    list = stroka.split()
    for el in list:
        if el == '#':
            ex = True
            break
        summ += int(el)
    print(summ)