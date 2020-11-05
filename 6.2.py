class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width


    def counting_mass(self, mass_1cm, thickness):
        formula = self._length * self._width * mass_1cm * thickness
        return formula


data_l = int(input('Введите значение длины дорожного полотна, (м): '))
data_w = int(input('Введите значение ширины дорожного полотна, (м): '))
data_m = int(input('Введите массу асфальта на 1 кв.м. дороги, толщиной в 1 см., (кг): '))
data_t = int(input('Введите толщину полотна, (см): '))
formula = Road(data_l, data_w)

print(formula.counting_mass(data_m, data_t),  ' кг')



