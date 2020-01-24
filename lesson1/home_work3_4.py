def my_func(a, b):
    return (a ** b)


print(my_func(5, -5))


# вариант
def my_func_1(a, b):
    temp = a
    for i in range(abs(b) - 1):
        temp *= a
        print(temp)
    return (1 / temp)


print(my_func_1(5, -5))
