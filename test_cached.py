from cathed import cached
import math
import unittest
from time import time, sleep

class TestCached(unittest.TestCase):

    def test_cached(self):

        @cached
        def factorial(n):
            if n < 0:
                return 0
            elif n < 2:
                return 1
            else:
                result = 1
                for value in range(2, int(n) + 1):
                    result *= value
            return result

        start = time()
        factorial(1736)
        first_time = time() - start
        start = time()
        factorial(1736)
        second_time = time() - start
        self.assertGreater(first_time, second_time, "Cached execution error")

if __name__ == '__main__':
    unittest.main()
