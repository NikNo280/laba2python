import unittest
from merge_sort import algoritm_merge_sort, merge_sort

class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        test_arr = []
        open('test_output_numbers.txt', 'w')
        merge_sort('test_input_numbers.txt', 'test_output_numbers.txt')
        with open('test_output_numbers.txt', "r", encoding='utf-8') as file:
            for _ in range(0, 10):
                test_arr.append(int(file.readline()))
        self.assertTrue(test_arr == [-961016, -710872, -220398, 164854, 299671, 349047, 497601, 539894, 620093, 847587],
                        "Error mergesort")
        self.assertFalse(test_arr == [-961016, -71011872, -220398, 164854, 299671, 349047, 497601, 539894, 620093, 847587],
                        "Error mergesort")

    def test_algoritm_merge_sort(self):
        array = [3, 2, 15, 9, 7]
        self.assertTrue(algoritm_merge_sort(array) == [2, 3, 7, 9, 15],
                        "Error temp file sort")
        self.assertFalse(algoritm_merge_sort(array) == [3, 2, 15, 9, 7],
                        "Error temp file sort")

if __name__ == '__main__':
    unittest.main()
