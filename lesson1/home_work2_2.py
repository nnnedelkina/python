my_list = []
n = int(input('введите количество элементов: '))

while n > 0:
    el = input('введите элемент списка: ' )
    my_list.append(el)
    n -= 1
print(my_list)

m = 1
for val in my_list[ 1: : 2]:
    my_list.insert(m-1, val)
    my_list.pop(m+1)
    m +=2

print(my_list)

