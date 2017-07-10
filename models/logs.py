from . import MongoModel
from . import timestamp
from datetime import datetime
import time
from flask import current_app as app


class Log(MongoModel):
    @classmethod
    def _fields(cls):
        fields = [
            ('text', str, ''),
            ('platform', str, ''),
            ('browser', str, ''),
            ('version', str, ''),
            ('user_agent', str, ''),
            ('ip', str, ''),
        ]
        fields.extend(super()._fields())
        return fields

    @classmethod
    def history(cls):
        ms = cls.all()
        ms.reverse()
        return ms
