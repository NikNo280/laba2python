import math

class N_Vector:

    def __init__(self, string):
        self._dimension = []
        self._size = 0
        try:
            for item in string.split(' '):
                self._dimension.append(int(item))
                self._size = self._size + 1
        except ValueError:
            self._dimension = []


    def multiplication_by_constant(self, const):
        self._dimension = list(map(lambda x : x * const, self._dimension))
        return self._dimension

    def size(self):
        sum = 0
        for item in list(map(lambda x : x * x, self._dimension)):
            sum += item
        return math.sqrt(sum)

    def get_item(self, index):
        return self._dimension[index]

    def __add__(self, vector2):
        return list(map(lambda x, y : x + y, self._dimension, vector2._dimension))

    def __sub__(self, vector2):
        return list(map(lambda x, y : x - y, self._dimension, vector2._dimension))

    def __mul__(self, vector2):
        return list(map(lambda x, y: x * y, self._dimension, vector2._dimension))

    def __truediv__(self, vector2):
        return list(map(lambda x, y: x / y, self._dimension, vector2._dimension))

    def __str__(self):
        return '{}'.format(self._dimension)

    def __eq__(self, vector2):
        return True if self._dimension == vector2._dimension else False

    def scalar_product(self, vector2):
        sum = 0
        for item in list(map(lambda x, y: x * y, self._dimension, vector2._dimension)):
           sum += item
        return sum
