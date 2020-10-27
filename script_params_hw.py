# функция расчёта заработной платы
def zp(x, y, z):
    result =  x * y + z
    return result

# из этого модуля будем импортировать файлы
if __name__ == '__main__':
    # выработка в часах
    hours = 40
    # ставка в час
    rate = 12
    # премия
    bonus = 36
    salary = zp(hours, rate, bonus)
    print(salary)

