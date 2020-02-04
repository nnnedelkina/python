from itertools import count, cycle

my_list = []
while True:
    try:
        start = int(input('c какого числа начать список: '))
        end = int(input("каким числом окончить список: "))
        rep = int(input('количество повторений: '))
        break
    except ValueError:
        print("вводите число!")


for el in count(start):
    if el > end:
        break
    else:
        my_list.append(el)
print(my_list)


c = 1
for el in cycle(my_list):
    if c > rep * len(my_list):
        break
    print(el)
    c += 1


