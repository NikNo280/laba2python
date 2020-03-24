import unittest
import merge_sort

class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        test_arr = []
        with open("test_output_ms.txt", "r", encoding='utf-8') as file:
            for _ in range(0, 10):
                test_arr.append(int(file.readline()))
        self.assertTrue(test_arr == [-961016, -710872, -220398, 164854, 299671, 349047, 497601, 539894, 620093, 847587],
                        "Ошибка в сортировке")
        self.assertFalse(test_arr == [-961016, -71011872, -220398, 164854, 299671, 349047, 497601, 539894, 620093, 847587],
                        "Ошибка в сортировке")

if __name__ == '__main__':
    unittest.main()
