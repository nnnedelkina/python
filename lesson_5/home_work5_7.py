import json

dict_firm = {}
ave_profit, n = 0, 0

with open('file_7.txt',encoding='utf-8') as f:
    for el in f:
        firm, type, income, costs = el.split()
        profit = int(income) - int(costs.split('.')[0])
        dict_firm[firm] = profit
        if profit > 0:
            ave_profit += profit
            n += 1

try:
    my_list = [dict_firm, {'average_profit': ave_profit/n}]
except ZeroDivisionError:
    print('Прибыли нет или данные не введены')
print(my_list)

with open('j_file_7.json', 'w', encoding='utf-8') as j_f:
    json.dump(my_list, j_f)
