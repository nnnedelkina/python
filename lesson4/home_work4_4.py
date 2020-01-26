from random import randrange
my_list = [randrange(20) for el in range(15)]
print(my_list)
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)