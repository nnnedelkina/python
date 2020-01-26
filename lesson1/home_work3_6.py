def int_func(val):
    return val[0].upper() + val[1:] if val != None and val != "" else ''


print(int_func('text'))

text = input('ваш текст: ')
text_1 = text.split(' ')
Text = str()
for el in text_1:
    Text += int_func(el)+' '
print(Text)

#вариант
print(" ".join(map(int_func, text.split(" "))))
