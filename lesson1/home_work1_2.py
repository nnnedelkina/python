seconds = int(input('введите время в секундах: '))

hour = seconds//3600
minute = (seconds % 3600)//60
second = seconds % 60

print(f'{hour:02d}:{minute:02d}:{second:02d}')