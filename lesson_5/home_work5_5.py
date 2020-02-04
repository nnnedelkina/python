from random import randrange
my_list_number = [randrange(300) for el in range(15)]
print(my_list_number)
str = (' '.join([str(i) for i in my_list_number]))
new_file = open('file_5.txt', 'w')
new_file.write(str)
new_file.close()

with open('file_5.txt', 'r') as f:
    content = f.read(1024)

summ = sum(map(int, content.split(' ')))
print(summ)
with open('file_5.txt', 'a') as fa:
    fa.write(f'\nсумма чисел: {summ}')

#использую разные способы открытия файлов, чтобы просто попрактиковаться


