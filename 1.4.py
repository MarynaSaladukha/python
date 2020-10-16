val = int(input('Введите целое положительное число '))
print(val)
max = 0
while val != 0:
    a = val % 10
    print(a)
    val = val // 10
    if a > max:
        max = a
print("Максимальная цифра в числе " , max)





