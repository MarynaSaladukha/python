
class Car:
    is_police = False
    def __init__(self, name, colour, speed):
        self.name = name
        self.speed = speed
        self.colour = colour


    def go(self):
        print('Машина ', self.name, ', ', self.colour, 'цвет: поехала')


    def stop(self):
        print('Машина ', self.name, ', ', self.colour, 'цвет: остановилась')


    def turn(self, direction):
        print('Машина ', self.name, ', ', self.colour, 'цвет: повернула ', str(direction))


    def show_speed(self):
        print('Машина ', self.name, ', ', self.colour, 'цвет: Двигается со скоростью ', str(self.speed))


class TownCar(Car):
    is_police = False
    def show_speed(self):
        print('Машина ', self.name, ', ', self.colour, 'цвет: Двигается со скоростью ', str(self.speed))
        if self.speed > 60:
            print('Вы превысили скорость!')

class SportCar(Car):
    is_police = False

class WorkCar(Car):
    is_police = False
    def show_speed(self):
        print('Машина ', self.name, ', ', self.colour, 'цвет: Двигается со скоростью ', str(self.speed))
        if self.speed > 40:
            print('Вы превысили скорость!')

class PoliceCar(Car):
    is_police = True

car_1 = TownCar('Mazda', 'Red', 50)
car_2 = SportCar('Ferrary', 'Red', 250)
car_3 = WorkCar('Nissan', 'White', 70)
car_4 = PoliceCar('Ford', 'Navy', 180)
car_1.go()
car_2.stop()
car_3.show_speed()
car_4.turn('направо')



