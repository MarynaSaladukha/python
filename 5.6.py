subj = {}

with open('text_5.6.txt') as f:
    for line in f:
        words = line.split() # разбиваем каждую строку по словам(элементам), в дальнейнем вводим обозначения для этих элементов
        subjects = words[0][:-1]
        lectures = int(words[1][:-3]) if len(words[1])>3 else 0
        practice = int(words[2][:-4]) if len(words[2])>4 else 0
        laboratory = int(words[3][:-5]) if len(words[3])>5 else 0
        summ = lectures + practice + laboratory
        subj[subjects] = summ #добавляем в словарь ключ: значение
        result = {subjects: summ} #формируем окончательный словарь (название предмета: общее количество часов по нему)

print(subj)



