class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки. ')

class Pen(Stationary):
    def draw(self):
        print('Запуск отрисовки ручкой. ')

class Pencil(Stationary):
    def draw(self):
        print('Запуск отрисовки карандашом. ')

class Handle(Stationary):
    def draw(self):
        print('Запуск отрисовки маркером. ')

pen_work = Pen('Синий')
pencil_work = Pencil('Жёлтый')
handle_work = Handle('Розовый')
pen_work.draw()
pencil_work.draw()
handle_work.draw()