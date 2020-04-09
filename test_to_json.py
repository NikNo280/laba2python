import unittest
from to_json import JsonFormat

class Student:
    def __init__(self, name, age, average_mark, person_name, person_age):
        self.name = name
        self.age = age
        self.average_mark = average_mark
        self.person = Person(person_name, person_age)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


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
        self.assertTrue(self.converter.to_json(self.student)
                        == "{ 'Student':{ 'name':'Vasia', 'age':18, 'average_mark':7.2, 'person':{ 'Person':{ 'name':'lala', 'age':322 } } } }",
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

    def test__dict_format(self):
        self.assertTrue(self.converter._dict_format("abc", 3)
                        == "'abc':3",
                        "Неверный формат key/value")
        self.assertFalse(self.converter._dict_format("abc", 3)
                        == "'abc' : 4",
                        "Неверный формат key/value")

    def test_normal_type_to_string(self):
        self.assertTrue(self.converter._normal_type_to_string(None)
                        == "None",
                        "Неверный формат normal_type")
        self.assertFalse(self.converter._normal_type_to_string(True)
                        == "true",
                        "Неверный формат normal_type")

    def test_to_json(self):
        self.assertTrue(self.converter.to_json([1, 2.0, '3', True, False, None, self.student])
                        == "[ 1, 2.0, '3', True, False, None, { 'Student':{ 'name':'Vasia', 'age':18, 'average_mark':7.2, 'person':{ 'Person':{ 'name':'lala', 'age':322 } } } } ]",
                        "Неверный формат list")
        self.assertFalse(self.converter.to_json({'1': 2.0, '3': True, 4: None, '5': self.student})
                         == "{ '1':2.0, '3':True, '4':None, '5':{ 'Studensat':{ 'name':'Vasia', 'age':18, 'average_mark':7.2, 'person':{ 'Person':{ 'name':'lala', 'age':322 } } } } }",
                         "Неверный формат dict")

if __name__ == '__main__':
    unittest.main()
