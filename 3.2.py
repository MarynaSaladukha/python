name = input('Введите имя ')
surname = input('Введите фамилию ')
dob = input('Введите дату рождения ')
city = input('Введите город проживания ')
email = input('Введите email ')
phone = input('Введите номер телефона ')

# создаём функцию, при которой данные, введённые пользователем, будут отображаться одной строкой через пробел
my_func = lambda name, surname, dob, city, email, phone: name + ' ' + surname + ' '+ dob + ' '+ city + ' '+ email + ' '+ phone
print(my_func(name=name, surname=surname, dob=dob, city=city, email=email, phone=phone))