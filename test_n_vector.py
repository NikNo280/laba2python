import math
import unittest

from n_vector import N_Vector, Operations

class TestNVector(unittest.TestCase):
    def setUp(self):
        self.test_n_vector = N_Vector("1 2 3")
        self.test_operation1 = Operations("1 2 3", "3 4 5")
        self.test_operation2 = Operations("6 7 8 9 10", "6 7 8 9 10")

    def test_init(self):
        self.assertEqual((self.test_n_vector.get_size(), self.test_n_vector.get_dimension()), (int(3), [1, 2, 3]),
                         "Полученные значения совпадают")

    def test_multiplication_by_constant(self):
        self.assertFalse(self.test_n_vector.multiplication_by_constant(3) == [7, 3, 2],
                         "Ошибка в умножении на константу")
        self.assertTrue(self.test_n_vector.multiplication_by_constant(2) == [6, 12, 18],
                        "Ошибка в умножении на константу")

    def test_size(self):
        self.assertFalse(self.test_n_vector.size() == 13,
                         "Ошибка, неверно найдена длинна")
        self.assertTrue(self.test_n_vector.size() == math.sqrt(14),
                        "Ошибка, неверно найдена длинна")

    def test_get_item(self):
        self.assertFalse(self.test_n_vector.get_item(0) == 2,
                         "Ошибка, неверно найден item по интедксу")
        self.assertTrue(self.test_n_vector.get_item(2) == 3,
                        "Ошибка, неверно найден item по интедксу")

    def test_sum(self):
        self.assertFalse(self.test_operation1.sum() == [1, 13, 125],
                         "Ошибка в сложении")
        self.assertTrue(self.test_operation1.sum() == [4, 6, 8],
                        "Ошибка в сложении")

    def test_subtraction(self):
        self.assertFalse(self.test_operation1.subtraction() == [1, 213, 125],
                         "Ошибка в вычитании")
        self.assertTrue(self.test_operation1.subtraction() == [-2, -2, -2],
                        "Ошибка в вычитании")

    def test_multiplication(self):
        self.assertFalse(self.test_operation1.multiplication() == [1, 213, 125],
                         "Ошибка в умножении")
        self.assertTrue(self.test_operation1.multiplication() == [3, 8, 15],
                        "Ошибка в умножении")

    def test_division(self):
        self.assertFalse(self.test_operation1.division() == [1, 213, 125],
                         "Ошибка в делении")
        self.assertTrue(self.test_operation2.division() == [1, 1, 1, 1, 1],
                        "Ошибка в делении")

    def test_scalar_product(self):
        self.assertFalse(self.test_operation1.scalar_product() == 12,
                         "Ошибка в скалярном произведении")
        self.assertTrue(self.test_operation1.scalar_product() == 26,
                        "Ошибка в скалярном произведении")

    def test_equals(self):
        self.assertFalse(self.test_operation1.equals(),
                         "Ошибка в сравнении")
        self.assertTrue(self.test_operation2.equals(),
                        "Ошибка в сравнении")

if __name__ == '__main__':
    unittest.main()