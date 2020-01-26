
from functools import reduce
print(reduce(lambda a, b: a * b, [el for el in range(100, 1001, 2)]))


