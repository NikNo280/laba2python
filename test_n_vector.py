import math
import unittest

from n_vector import N_Vector


class Test_N_Vector(unittest.TestCase):
    def setUp(self):
        self.test_n_vector1 = N_Vector("1 2 3")
        self.test_n_vector2 = N_Vector("3 4 5")

    def test_multiplication_by_constant(self):
        self.assertTrue(self.test_n_vector1.multiplication_by_constant(3) == [3, 6, 9],
                        "Error in constant multiplication")
        self.assertFalse(self.test_n_vector1.multiplication_by_constant(2) == [6, 13, 18],
                         "Error in constant multiplication")

    def test_size(self):
        self.assertFalse(self.test_n_vector1.size() == 13,
                         "Length error")
        self.assertTrue(self.test_n_vector1.size() == math.sqrt(14),
                        "Length error")

    def test_get_item(self):
        self.assertFalse(self.test_n_vector1.get_item(0) == 2,
                         "Invalid item by index")
        self.assertTrue(self.test_n_vector1.get_item(2) == 3,
                        "Invalid item by index")

    def test_sum(self):
        self.assertFalse(self.test_n_vector1 + self.test_n_vector2 == [1, 13, 125],
                         "Addition error")
        self.assertTrue(self.test_n_vector1 + self.test_n_vector2 == [4, 6, 8],
                        "Addition error")

    def test_subtraction(self):
        self.assertFalse(self.test_n_vector1 - self.test_n_vector2 == [1, 213, 125],
                         "Subtraction error")
        self.assertTrue(self.test_n_vector1 - self.test_n_vector2 == [-2, -2, -2],
                        "Subtraction error")

    def test_multiplication(self):
        self.assertFalse(self.test_n_vector1 * self.test_n_vector2 == [1, 213, 125],
                         "Multiplication error")
        self.assertTrue(self.test_n_vector1 * self.test_n_vector2 == [3, 8, 15],
                        "Multiplication error")

    def test_division(self):
        self.assertFalse(self.test_n_vector2 / self.test_n_vector1 == [1, 213, 125],
                         "Division error")
        self.assertTrue(self.test_n_vector2 / self.test_n_vector1 == [3.0, 2.0, 1.6666666666666667],
                        "Division error")

    def test_scalar_product(self):
        self.assertFalse(self.test_n_vector1.scalar_product(self.test_n_vector2) == 12,
                         "Error in scalar product")
        self.assertTrue(self.test_n_vector1.scalar_product(self.test_n_vector2) == 26,
                        "Error in scalar product")

    def test_equals(self):
        self.assertFalse(self.test_n_vector1 == self.test_n_vector2,
                         "Equals error")
        self.assertTrue(self.test_n_vector1 == self.test_n_vector1,
                        "Equals error")

    def test_to_str(self):
        self.assertTrue(self.test_n_vector1.__str__() == "[1, 2, 3]",
                        "To str error")


if __name__ == '__main__':
    unittest.main()
