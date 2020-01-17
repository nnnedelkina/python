number = int(input('введите целое положительное число: '))

max_digit = 0
while number != 0:
    digit = number % 10
    number = number//10
    if max_digit < digit:
        max_digit = digit

print(max_digit)