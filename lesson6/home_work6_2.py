class Road:

    def  __init__(self, length, width):
        self._length = length
        self._width = width

    def mas_asff(self, height):
        return self._length * self._width * height * 25/1000

road_1 = Road(20, 5000)
print(road_1.mas_asff(5),'т')

