from functools import reduce

# задаём список чётных чисел от 100 до 1000
new_list = [el for el in range(100, 1000) if el % 2 == 0]
print(new_list)

# произведение всех заданных чисел с помощью функции lambda
multiplication = reduce(lambda x,y: x*y, new_list)
print(multiplication)


