import unittest
from singletone import HeirSingleton, Singleton

class TestSingleton(unittest.TestCase):
    def test_ref_Heir(self):
        first_object = HeirSingleton()
        second_object = HeirSingleton()
        self.assertIs(first_object, second_object)

    def test_ref_Singleton(self):
        first_object = Singleton()
        second_object = Singleton()
        self.assertIs(first_object, second_object)


if __name__ == '__main__':
    unittest.main()