# создаём произвольный список чисел
numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# убираем из списка повторяющиеся значения
new_list = [numbers[i] for i in range(len(numbers)) if numbers.count(numbers[i]) == 1]
print(new_list)


