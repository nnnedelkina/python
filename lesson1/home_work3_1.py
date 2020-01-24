def fun_del ():
    try:
        a = float(input('введите число: '))
        b = float(input('введите число: '))
        return (a / b)
    except ValueError:
        return (print('введено не число'))
    except ZeroDivisionError:
        return (print('на ноль делить нельзя'))



print(fun_del())