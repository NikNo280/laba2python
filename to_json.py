class Student:
    def __init__(self, name, age, active, balance, other_names, friends, spouse, person_name, person_age):
        self.name = name
        self.age = age
        self.active = active
        self.balance = balance
        self.other_names = other_names
        self.friends = friends
        self.spouse = spouse
        self.person = Person(person_name, person_age)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class JsonFormat:

    def to_json(self, obj):
        if isinstance(obj, (list, tuple)):
            return self._list_to_string(obj)
        elif isinstance(obj, dict):
            return self._dict_to_string(obj)
        else:
            return self._dict_to_string(self._class_to_dict(obj))

    def _list_to_string(self, obj):
        temp = []
        for i in obj:
            if isinstance(i, (int, float, str, bool, type(None))):
                temp.append(self._normal_type_to_string(i))
            elif isinstance(i, dict):
                temp.append(self._dict_to_string(i))
            elif isinstance(i, (list, tuple)):
                temp.append(self._list_to_string(i))
            else:
                temp.append(self._dict_to_string(self._class_to_dict(i)))
        end_str = ', '.join(temp)
        return '[ ' + end_str + ' ]'

    def _normal_type_to_string(self, obj):
        if isinstance(obj, (int, float)):
            return '{}'.format(obj)
        elif type(obj) == str:
            return "'{}'".format(obj)
        elif type(obj) == bool:
            if obj:
                return 'True'
            return 'False'
        elif type(obj) == type(None):
            return 'None'

    def _dict_to_string(self, Dict):
        temp = []
        for key, value in Dict.items():
            if isinstance(value, (int, float, str, bool, type(None))):
                temp.append(self._dict_format(key, self._normal_type_to_string(value)))
            elif isinstance(value, dict):
                temp.append(self._dict_format(key, self._dict_to_string(value)))
            elif isinstance(value, (list, tuple)):
                temp.append(self._dict_format(key, self._list_to_string(value)))
            else:
                temp.append(self._dict_format(key, self._dict_to_string(self._class_to_dict(value))))
        end_str = ', '.join(temp)
        return '{ ' + end_str + ' }'

    def _class_to_dict(self, obj):
        obj_dict = {obj.__class__.__name__: obj.__dict__}
        return obj_dict

    def _dict_format(self, key, value):
        return "'{key}':{value}".format(key=key, value=value)

new_user = Student(
    name="admin",
    age=19,
    friends=["Jane", "John"],
    balance=345.80,
    other_names=["Doe", "Joe"],
    active=True,
    spouse=None,
    person_name="Nik",
    person_age=18)

json = JsonFormat()
k = list()
k.append(1)
k.append(2)
k.append(3)
b = [k, 5, "sadasd", 6, [45, 65], True, False, None, {"sdf": 34}, new_user]
print(json.to_json(b))
