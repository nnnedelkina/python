class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки:')

class Pen(Stationery):
    def draw(self):
        print('рисует ручка', self.title)

class Pencil(Stationery):
    def draw(self):
        print('рисует карандаш',self.title)

class Handl(Stationery):
    def draw(self):
        print('рисует маркер', self.title)

stationery_1 = Stationery('')
stationery_1.draw()

pen_1 = Pen('pen_1')
pen_1.draw()

pencil_1 = Pencil('pencil_1')
pencil_1.draw()

handle_1 = Handl('handle_1')
handle_1.draw()