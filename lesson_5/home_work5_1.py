new_file = open('file_1.txt', 'w')

my_list = []
while True:
    str = input('введите строку (пустая строка, чтобы закончить): ')
    if str == "":
        break
    str += '\n'
    my_list.append(str)
print(my_list)

new_file.writelines(my_list)

new_file.close()