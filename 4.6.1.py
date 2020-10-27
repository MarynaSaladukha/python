# 1) генерируем целые числа, начиная с указанного
# создаём скрипт
from sys import argv
from itertools import count

name_script, start_number, end_number = argv
start_number = int(start_number)
end_number = int(end_number)

for el in count(start_number):
    if el > end_number:
        break
    else:
        print(el)

