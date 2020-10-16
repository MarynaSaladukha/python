vyr = int(input("Введите сумму выручки "))
izd = int(input("Введите сумму издержек "))
if vyr > izd:
    result1 = int(vyr - izd)
    print ("Прибыль составила " , result1)
    rentab = result1 / vyr
    print("Рентабельность составила " , rentab)
else:
    result2 = ("Убыток")
    print(result2)
staff = int(input("Введите численность сотрудников фирмы "))
staff_profit = result1 / staff
print("Прибыль на одного сотрудника составила" , staff_profit)