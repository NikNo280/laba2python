import cached
import unittest

class TestCached(unittest.TestCase):

    def test_cached(self):
        self.assertTrue(cached.add(1, 2) == 3, "Ошибка в сложении")
        self.assertFalse(cached.add(1, 2) == 4, "Ошибка в сложении")

if __name__ == '__main__':
    unittest.main()