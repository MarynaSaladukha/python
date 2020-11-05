import time
class Trafficlight:

    def __init__(self):
        self.__colour = 'red'


    def running(self):
        if self.__colour == 'red':
            time.sleep(7)
            self.__colour = 'yellow'
        elif self.__colour == 'yellow':
            time.sleep(2)
            self.__colour = 'green'
        else:
            time.sleep(5)
            self.__colour = 'red'
        return self.__colour


    def get(self):
        return self.__colour


my_trafficlights = Trafficlight()
print(my_trafficlights.get())
print(my_trafficlights.running())
print(my_trafficlights.running())
print(my_trafficlights.running())

