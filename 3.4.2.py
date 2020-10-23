def my_func(x, y):
    i = 1  # текущая степень
    result = 1
    while i <= abs(y) : # перебираем степень, пока она не станет равной числу 'y'
        result *= x
        i += 1
    if y >= 0:
        return result
    else:
        return 1/result


x = 5
y = -1
print(my_func(x, y))
