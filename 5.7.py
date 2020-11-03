import json #в конце задания нужно сохранить данные в виде json-объекта
with open ('text_5.7.txt', 'r') as f:
    text = f.readlines() #будем работать с каждой отдельно взятой строкой
    i = 0
    summary = 0
    data = {}
    for line in text:
        words = line.split() #разбиваем каждую строку на слова, чтобы в дальнейшем за элементы
        income = int(words[2])
        losses = int(words[3])
        profit = income - losses #нашли прибыль по каждой фирме

        if profit >= 0: #по условию задачи для подсчёта средней прибыли берём только положительную
            i += 1
            summary = profit + summary #каждое новое значение прибыли прибавляем к сумме предыдущих (если прибыль отрицательная, то она не считается)

        firms = words[0]
        data[firms] = profit #в созданном ранее списке data добавляем ключ: значение

    average_profit = summary / i #средняя прибыль как сумма всех положительных прибылей, делённая на количество фирм с положительной прибылью. обязательно считаем за циклом
    spisok = [data, {'avarage_profit': average_profit}] #формируем окончательный список
    print(spisok)


    with open('text_5.7.json', 'w') as file_js: #сохраняем итоговый список в виде json-объекта
        json.dump(spisok, file_js)





