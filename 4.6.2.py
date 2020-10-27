# 2) повторяем элементы некоторого списка
# создаём скрипт
from sys import argv
from itertools import cycle

name_script, rep_number, *my_set = argv
rep_number = int(rep_number)
i = 0
for el in cycle(my_set):
    if i > rep_number:
        break
    print(el)
    i += 1