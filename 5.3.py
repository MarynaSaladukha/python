with open('text_5.3.txt', 'r') as file:
    text = file.readlines()
    
print('Менее 20 тыс. получает: ')
i = 0
limit = 20 # будем выводить фамилии сотрудников, имеющих оклады менее этой суммы, тыс.
salary = []

for el in text:
    i += 1
    #print(f'Данные {i} сотрудника (фамилия, оклад): ', el)
    words = el.split()
    #print('Фамилия - ', words[0])
    #print('Оклад = ', words[1])
    words[1] = int(words[1])
    if words[1] < limit:
        print(words[0])

    salary.append(words[1])

medium_salary = sum(salary) / len(salary)
print('Средний оклад работников = ', medium_salary, 'тыс.')



