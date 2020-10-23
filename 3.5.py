summ = 0 #пока не начали считать значения
while True:
    user_numbers = input('Введите несколько чисел ')
    user_numbers = (user_numbers.split(' ')) #разбиваем строку на отдельный элементы
    if user_numbers[len(user_numbers)-1] == '!': # считаем сумму, включая каждый новый элемент, кроме знака !
        user_numbers = user_numbers[:len(user_numbers)-1]
        for element in user_numbers:
            element = int(element)
            summ += element
        print(summ)
        break
    for element in user_numbers: #повторяем действия до тех пор, пока пользователь не введёт !
        element = int(element)
        summ += element
    print(summ)
    print('Введите ! для завершения счёта ')











