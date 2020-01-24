products = []
while True:
    name = input('наименование товара (пустая строка, чтобы закончить): ')
    if name == "":
        break
    price = float(input('цена: '))
    quantity = int(input('количество: '))
    units = input('еденицы: ')
    n = len(products)
    product = {'название': name, 'цена': price, 'количество': quantity, 'ед.': units}
    products.insert(n, (n+1, product))

print(products)

name_list = set()
price_list = set()
quantity_list = set()
units_list = set()
for el in products:
    name_list.add(el[1].get('название'))
    price_list.add(el[1].get('цена'))
    quantity_list.add(el[1].get('количество'))
    units_list.add(el[1].get('ед.'))
analytic = {"название": list(name_list), "цена": list(price_list), "количество": list(quantity_list), "ед.": list(units_list)}
print("{")
for k, v in analytic.items():
    print(f"{k}: {v}")
print("}")
