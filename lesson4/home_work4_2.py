from random import randrange
my_list = [randrange(300) for el in range(15)]
print(my_list)
new_list = [my_list[i] for i in range(1,len(my_list)) if my_list[i] > my_list[i-1]]
print(new_list)