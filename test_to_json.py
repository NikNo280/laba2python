import unittest
from to_json import JsonFormat
from to_json import Student

class TestToJson(unittest.TestCase):
    def test_to_json(self):
        self.assertTrue(JsonFormat.to_json(self,[5, "sadasd", 6, [45, 65], True, False, None, {"sdf": 34}]) == "[ 5, 'sadasd', 6, [ 45, 65 ], True, False, None, { 'sdf':34 } ]", "Ошибка в переводе json")
        self.assertFalse(JsonFormat.to_json([5, "sadasd", 6, [45, 65], True, False, None, {"sdf": 34}]) == "[ 5, 'sadasd', 6, [ 45, 65 ], Trsdfue, False, None, { 'sdf':34 } ]", "Ошибка в переводе json")

if __name__ == '__main__':
    unittest.main()
