import cached
import unittest
from to_json import JsonFormat, Student


class TestJson(unittest.TestCase):

    def setUp(self):
        self.converter = JsonFormat()
        self.student = Student(
            name="Vasia",
            age=18,
            average_mark=7.2,
            person_name="lala",
            person_age=322
        )

    def test_list_to_string(self):
        self.assertTrue(self.converter.to_json([1, 2.0, '3', True, False, None, self.student])
                        == "[ 1, 2.0, '3', True, False, None, { 'Student':{ 'name':'Vasia', 'age':18, 'average_mark':7.2, 'person':{ 'Person':{ 'name':'lala', 'age':322 } } } } ]",
                        "Неверный формат list")
        self.assertFalse(self.converter.to_json([1, 2.0, '3', True, False, None, self.student])
                        == "[ 1, 2.0, '3', True, False, None, { 'Stsdfdudent':{ 'name':'Vasia', 'age':18, 'average_mark':7.2, 'person':{ 'Person':{ 'name':'lala', 'age':322 } } } } ]",
                        "Неверный формат list")

    def test_dict_to_string(self):
        self.assertTrue(self.converter.to_json({'1' : 2.0, '3' : True, 4 : None, '5' :self.student})
                        == "{ '1':2.0, '3':True, '4':None, '5':{ 'Student':{ 'name':'Vasia', 'age':18, 'average_mark':7.2, 'person':{ 'Person':{ 'name':'lala', 'age':322 } } } } }",
                        "Неверный формат dict")
        self.assertFalse(self.converter.to_json({'1' : 2.0, '3' : True, 4 : None, '5' :self.student})
                         == "{ '1':2.0, '3':True, '4':None, '5':{ 'Studensat':{ 'name':'Vasia', 'age':18, 'average_mark':7.2, 'person':{ 'Person':{ 'name':'lala', 'age':322 } } } } }",
                         "Неверный формат dict")

    def test_class_to_dict(self):
        self.assertTrue(self.converter.to_json(self.student)
                        == "{ 'Student':{ 'name':'Vasia', 'age':18, 'average_mark':7.2, 'person':{ 'Person':{ 'name':'lala', 'age':322 } } } }",
                        "Неверный формат class")
        self.assertFalse(self.converter.to_json(self.student)
                         == "{ 'Student':{ 'nafsame':'Vasia', 'age':18, 'average_mark':7.2, 'person':{ 'Person':{ 'name':'lala', 'age':322 } } } }",
                         "Неверный формаsaт class")


if __name__ == '__main__':
    unittest.main()
