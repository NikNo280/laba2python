import cathed
import unittest

class TestCached(unittest.TestCase):

    def test_cached(self):
        self.assertTrue(cathed.add(1, 2) == 3, "Ошибка в сложении")
        self.assertFalse(cathed.add(1, 2) == 4, "Ошибка в сложении")

if __name__ == '__main__':
    unittest.main()