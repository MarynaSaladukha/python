number_list = [10, 20, 3, 4, 5, 6]
number_list.sort(reverse = True) #usable for the entire programm
print(number_list)
user_number = int(input('Введите любое натуральное число '))
i = 0
val = len(number_list)
print(val)
while user_number < number_list[i]:
    i += 1
    if i >= len(number_list):
        break
print(i)
number_list.insert(i, user_number)
print(number_list)



