from . import MongoModel
import json
import os

_root = os.path.dirname(os.path.abspath(__file__))
_file = os.path.join(_root, 'word_list.json')


class Words(MongoModel):
    @classmethod
    def _fields(cls):
        fields = [
            ('content', str, ''),

        ]
        fields.extend(super()._fields())
        return fields

    @staticmethod
    def write(data):
        print(data)
        data = data.split(' ')
        print(data)
        with open(_file, 'w+', encoding='utf8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    @staticmethod
    def read():
        with open(_file, 'r+', encoding='utf8') as f:
            data = json.load(f)
        data = ' '.join(data)
        return data

    @staticmethod
    def read_list():
        with open(_file, 'r+', encoding='utf8') as f:
            data = json.load(f)
        return data
