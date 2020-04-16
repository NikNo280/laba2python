import json
class JsonFormat:

    def to_json(self, obj):
        if isinstance(obj, (list, tuple)):
            return self._list_to_string(obj)
        elif isinstance(obj, dict):
            return self._dict_to_string(obj)
        else:
            return self._normal_type_to_string(obj)

    def _list_to_string(self, obj):
        temp = []
        for i in obj:
            if isinstance(i, (int, float, str, bool, type(None))):
                temp.append(self._normal_type_to_string(i))
            elif isinstance(i, dict):
                temp.append(self._dict_to_string(i))
            elif isinstance(i, (list, tuple)):
                temp.append(self._list_to_string(i))
        end_str = ', '.join(temp)
        return '[' + end_str + ']'

    def _normal_type_to_string(self, obj):
        if type(obj) == bool:
            if obj:
                return 'true'
            return 'false'
        elif isinstance(obj, (int, float)):
            return '{}'.format(obj)
        elif type(obj) == str:
            return '"{}"'.format(obj)
        elif type(obj) == type(None):
            return 'null'

    def _dict_to_string(self, Dict):
        temp = []
        for key, value in Dict.items():
            if isinstance(value, (int, float, str, bool, type(None))):
                temp.append(self._dict_format(key, self._normal_type_to_string(value)))
            elif isinstance(value, dict):
                temp.append(self._dict_format(key, self._dict_to_string(value)))
            elif isinstance(value, (list, tuple)):
                temp.append(self._dict_format(key, self._list_to_string(value)))
        end_str = ', '.join(temp)
        return '{' + end_str + '}'


    def _dict_format(self, key, value):
        return '"{key}": {value}'.format(key=key, value=value)
