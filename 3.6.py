def int_func(word):
    return word.capitalize() #слово начинается с большой буквы


def my_func(text):
    words = text.split() #разбиваем всё предложение по словам
    lenght = len(words) #чтобы можно было брать каждое слово отдельно и выводить их с большой буквы
    i = 0
    while i <= lenght - 1:
        words[i] = words[i].capitalize()
        i += 1

    return (' '.join(words)) #чтобы предложение выводилось строкой, а не списком




text = 'шла саша по шоссе'
print(my_func(text))
word = 'tractor'
print(int_func(word))


