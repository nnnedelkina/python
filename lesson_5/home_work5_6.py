def hour_1(el):
    if el == "-":
        return 0
    return int(el.split('(')[0])


my_dist = {}
with open('file_6.txt') as f:
       for el in f:
           subject, hours = el.split(':')
           list_hours = hours.split()
           h = 0
           for el_1 in list_hours:
               h += hour_1(el_1)
           my_dist.update({subject: h})

print(my_dist)