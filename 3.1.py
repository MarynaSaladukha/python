def user_calc(): # создали функцию, при которой нужно делить числа, введённые пользователем
    val_1 = int(input('Введите первое число '))
    print(val_1)
    val_2 = int(input('Введите второе число '))
    print(val_2)
    if val_2 != 0: # ставим условие, что на ноль делить нельзя
        result = round(val_1 / val_2, 2) # округляем итог до 2-го знака после запятой, чтобы было красиво
        return result


result = user_calc()
print(result)