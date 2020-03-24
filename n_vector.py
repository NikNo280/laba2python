import math

class N_Vector:

    def __init__(self, string):
        self._dimension = []
        self._size = 0;
        for item in string.split(' '):
            self._dimension.append(int(item))
            self._size += 1

    def get_size(self):
        return self._size

    def get_dimension(self):
        return self._dimension

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


class Operations:

    def __init__(self, string1, string2):
        self.vector1 = N_Vector(string1)
        self.vector2 = N_Vector(string2)

    def sum(self):
        return list(map(lambda x, y : x + y, self.vector1._dimension, self.vector2._dimension))

    def subtraction(self):
        return list(map(lambda x, y : x - y, self.vector1._dimension, self.vector2._dimension))

    def multiplication(self):
        return list(map(lambda x, y: x * y, self.vector1._dimension, self.vector2._dimension))

    def division(self):
        return list(map(lambda x, y: x / y, self.vector1._dimension, self.vector2._dimension))

    def scalar_product(self):
        sum = 0
        for item in list(map(lambda x, y: x * y, self.vector1._dimension, self.vector2._dimension)):
           sum += item
        return sum
    def equals(self):
        if self.vector1._dimension == self.vector2._dimension:
            return True
        return False

