class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        return full_name


    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        return total_income

data_user1 = Position('Вася', 'Пупкин', 'программист', 2000, 450)
data_user2 = Position('Ольга', 'Жукова', 'бухгалтер', 1800, 500)
print(data_user1.get_full_name())
print(data_user1.get_total_income())
print(data_user2.get_full_name())
print(data_user2.get_total_income())
