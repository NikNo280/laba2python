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
        return '[' + end_str + ']'

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
        return '{' + end_str + '}'

    def _class_to_dict(self, obj):
        obj_dict = {obj.__class__.__name__: obj.__dict__}
        return obj_dict

    def _dict_format(self, key, value):
        return "'{key}':{value}".format(key=key, value=value)

    def from_json(self, str):
        if str[0] == '[':
            str = str[1:-1:]
            return self._json_to_list(str, 0)
        else:
            return 0;

    def _json_to_list(self, str, index):
        output_list = []
        items_list = str.split(', ')
        stop = 0
        for item in items_list:
            if stop != 0:
                stop -= 1
                continue
            if self._is_number(item):
                if self._int_or_float(item):
                    output_list.append(int(item))
                    index += 1
                    continue
                else:
                    output_list.append(float(item))
                    index += 1
                    continue
            if item == 'True':
                output_list.append(True)
                index += 1
                continue
            if item == 'False':
                output_list.append(False)
                index += 1
                continue
            if item == 'None':
                output_list.append(None)
                index += 1
                continue
            if item[0] == '[':
                temp_list = []
                temp = items_list[index]
                temp_list.append(temp[1:])
                index += 1

                while True:
                    in_list = items_list[index]
                    if in_list[-1:] == ']':
                        temp_list.append(in_list[:-1])
                        stop += 1
                        break
                    temp_list.append(in_list)
                    index += 1
                    stop += 1
                temp_list = ', '.join(temp_list)
                output_list.append(self._json_to_list(temp_list, 0))
                continue
            else:
                output_list.append(item)
                index += 1
        return output_list

    def _int_or_float(self, number):
        try:
            int(number)
            return True
        except ValueError:
            return False

    def _is_number(self,str):
        try:
            float(str)
            return True
        except ValueError:
            return False

converte = JsonFormat()
c = [3, 2, 1, [True, False, None]]
a = [5, 4, 3.0, 'asdasfs', True, False, None, c]
b = converte.to_json(a)
print(converte.to_json(a))
print(converte.from_json(b))