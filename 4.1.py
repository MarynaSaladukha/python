from sys import argv
# импортируем из модуля script_params_hw функцию расчёта заработной платы zp
from script_params_hw import zp


name_script, hours, rate, bonus = argv
# обязательно приводим показатели к числовым значениям, чтобы впоследствии программа их могла посчитать
hours = int(hours)
rate = int(rate)
bonus = int(bonus)
# производим действия, заданные в функции расчёта заработной платы
salary = zp(hours, rate, bonus)
print(salary)