def summ_number(arg_one, arg_two, arg_three):
    # создаём функцию для трёх чисел, из которых нужно вычислить сумму двух наибольших
    min_number = min(arg_one, arg_two, arg_three) #находим минимальное значение, чтобы его исключить
    return arg_one + arg_two + arg_three - min_number


arg_one = 5
arg_two = 19
arg_three = 15
print(summ_number(arg_one, arg_two, arg_three))







