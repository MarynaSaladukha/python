user = int(input("Введите целое число от 1 до 12 "))
print(user)
month = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
winter = month[:3]
spring = month[3:6]
summer = month[6:9]
if user in winter:
    print("winter")
elif user in spring:
    print("spring")
elif user in summer:
    print("summer")
else:
    print("autumn")

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
month = {'winter':winter, 'spring':spring, 'summer':summer, 'autumn':autumn}
for keys in month.keys():
    if user in month[keys]:
        print(keys)