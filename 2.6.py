goods = list()
i = 0
print(goods)
while True:
    name = input('Введите название товара ')
    price = int(input('Введите цену товара '))
    quantity = int(input('Ведите количество товара '))
    units = input('Введите единицу измерения количества товара ')
    #print(tuple((name, price, quantity, units)))
    characteristic = {'название': name, 'цена': price, 'количество': quantity, 'ед': units}
    #print(characteristic)
    i += 1
    goods_data = (i, characteristic)
    #print(goods_data)
    goods.append(goods_data)
    print(goods)
    answer = input('Есть ли ещё данные о товарах? (Да/Нет) ')
    if answer != 'Да' :
        break
analitics = {'название': [], 'цена': [], 'количество': [], 'ед': []}
i = 0

while i < len(goods):
    analitics['название'].append(goods[i][1].get('название'))
    analitics['цена'].append(goods[i][1].get('цена'))
    analitics['количество'].append(goods[i][1].get('количество'))
    if goods[i][1].get('ед') not in analitics['ед']:
        analitics['ед'].append(goods[i][1].get('ед'))
    i += 1
print(analitics)
