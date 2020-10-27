
def fact(n):
    # функция-генератор, в которой создаются факториалы чисел до заданного, то есть до n
    i = 1 # итерация цикла генератора
    result = 1
    while i <= n:
        result *= i
        i += 1
        yield result
n = int(input('Введите число '))
print([el for el in fact(n)])

