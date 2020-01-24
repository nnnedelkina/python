st = input('ваша строка: ')
st = st.split()
print(st)
i=1
for val in st:
    print(f' {i} {val[ : 10]}')
    i +=1

#вариант
for ind, el in enumerate(st, 1):
    print(ind, el[:10])
