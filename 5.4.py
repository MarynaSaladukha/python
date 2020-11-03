#будем работать с новым списком
russian = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []

with open('text_5.4.txt', 'r') as file:
    for el in file:
        el = el.split()
        # заменяем слова одно на другое из списка russian
        new_text = russian[el[0]] + ' - ' + el[2]
        new_file.append(new_text) #добавляем в первоначальный пустой список преобразованнеы значения
    print(new_file)

with open('file_5.4_new.txt', 'w') as file: #записываем новый блок строк в новый текстовый файл
    for el in new_file:
        file.writelines(el + '\n')

