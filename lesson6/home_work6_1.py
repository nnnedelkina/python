import time
class TrafficLight:
    backgroundEsc = {"reset": "\033[0m", "red": "\033[41m", "green": "\033[42m", "yellow": "\033[43m"}

    def __init__(self):
        self.__color = ''

    def running (self):
        while True:
            self.__color = 'red'
            self.print_color()
            time.sleep(7)
            self.__color = 'yellow'
            self.print_color()
            time.sleep(2)
            self.__color = 'green'
            self.print_color()
            time.sleep(7)
            self.__color = 'yellow'
            self.print_color()
            time.sleep(2)


    def print_color(self, text=" "):
        print(TrafficLight.backgroundEsc[self.__color] + text + TrafficLight.backgroundEsc["reset"], end="")

traffic_light_1 = TrafficLight()
traffic_light_1.running()