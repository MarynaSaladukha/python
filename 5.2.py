# самый простой способ нахождения кол-ва строк в файле
with open('text_5.2.txt') as file:
    text = file.readlines()
    lines = len(text)
    print('Количество строк: ', lines)
    i = 0
    for line in text:
        i += 1
        words = line.split()
        characters = len(words)
        print(f'Количество слов в {i} строкe: ', characters)
