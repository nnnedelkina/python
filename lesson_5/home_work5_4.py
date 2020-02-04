
my_diсt = {'1':'Один', '2':'Два', '3':'Три', '4': 'Четыре'}

new_list = []
new_file = open('file_4_d.txt', 'w')
with open('file_4.txt') as f:
    for line in f:
        str = line.split('-')
        key = str[1].rstrip('\r\n')
        word = my_diсt.get(key)
        print(word + '-' + key, file=new_file)

new_file.close()