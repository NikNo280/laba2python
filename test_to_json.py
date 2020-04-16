import unittest
from to_json import JsonFormat
import json


class TestJson(unittest.TestCase):

    def setUp(self):
        self.converter = JsonFormat()

    def test_int(self):
        data = 10
        self.assertEqual(json.dumps(data), self.converter.to_json(data))

    def test_float(self):
        data = 9.9
        self.assertEqual(json.dumps(data), self.converter.to_json(data))

    def test_none(self):
        data = None
        self.assertEqual(json.dumps(data), self.converter.to_json(data))

    def test_str(self):
        data = 'hello'
        self.assertEqual(json.dumps(data), self.converter.to_json(data))

    def test_tuple(self):
        data = (10, 10)
        self.assertEqual(json.dumps(data), self.converter.to_json(data))

    def test_tuple_diff(self):
        data = ('10', 10, 9.9, (9, 10), None, 110)
        self.assertEqual(json.dumps(data), self.converter.to_json(data))

    def test_list(self):
        data = [10, 9]
        self.assertEqual(json.dumps(data), self.converter.to_json(data))

    def test_list_diff(self):
        data = ['10', 9, 9.9, (9, 9)]
        self.assertEqual(json.dumps(data), self.converter.to_json(data))

    def test_dict(self):
        data = {10: 10, 9: 9}
        self.assertEqual(json.dumps(data), self.converter.to_json(data))

    def test_dict_str(self):
        data = {'10': '10', '10': '9'}
        self.assertEqual(json.dumps(data), self.converter.to_json(data))

    def test_dict_diff(self):
        data = {'10': '10', 2: '2', 3: None}
        self.assertEqual(json.dumps(data), self.converter.to_json(data))

    def test_dict_adn_list(self):
        data = {'10': [3, 2, None], 2: '2', 3: False}
        self.assertEqual(json.dumps(data), self.converter.to_json(data))

    def test_list_adn_dict(self):
        data = [{'10': '10', 2: '2', 3: True}]
        self.assertEqual(json.dumps(data), self.converter.to_json(data))


if __name__ == '__main__':
    unittest.main()
