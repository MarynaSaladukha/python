time = int(input('Введите время в секундах: '))
print(time)
hours = time // 3600
minutes = time % 3600 // 60
seconds = time % 3600 % 60
print(f'Введённое время будет равно {hours}:{minutes}:{seconds} (чч:мм:сс)')

