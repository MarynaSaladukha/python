f = open('text.txt', 'w')
user_name = input('Как тебя зовут? ')
f.write(user_name)
user_city = input('В каком городе ты живёшь? ')
f.write(user_city)
print('Привет',user_name, 'из города ', user_city)

f.close()
