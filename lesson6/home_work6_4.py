class Car:

    def __init__(self, color, name):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def go(self, speed):
        self.speed = speed
        print('машина едет со скоростью:', speed)

    def stop(self):
        print('машина остановилась')
        self.speed = 0

    def turn(self, direction):
        print('машина повернула', direction)

    def show_speed(self):
        print('скорость:', self.speed)


class TownCar(Car):
    def show_sped(self):
        Car.show_speed(self)
        if self.speed > 60:
            print('скорость превышина:', self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_sped(self):
        Car.show_speed(self)
        if self.speed > 60:
            print('скорость превышина:', self.speed)


class PoliceCar(Car):
    def __init__(self, color, name):
        Car.__init__(self, color, name)
        self.is_police = True


def test_car(car, speed, direction):
    print(car.color, car.name, car.is_police)
    car.go(speed)
    car.show_speed()
    car.turn(direction)
    car.stop()
    car.show_speed()


car_1 = TownCar('красная', 'Honda')
test_car(car_1, 65, 'налево')


car_2 = WorkCar('синяя', 'Jeep')
test_car(car_2, 75, 'направо')

car_3 = SportCar('желтая', 'Ferrary')
test_car(car_3, 65, 'лево')

car_4 = PoliceCar('белая','Lada')
test_car(car_4, 100, 'назад')