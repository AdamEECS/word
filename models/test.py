from . import MongoModel
from flask import current_app as app


class Test(MongoModel):
    @classmethod
    def _fields(cls):
        fields = [
            ('content', str, ''),
            ('created_at', str, ''),
            ('long', int, 0),
            ('revise', str, ''),
            ('reviseId', str, ''),
            ('time_humans', str, ''),
            ('time_show', str, ''),
            ('title', str, ''),
            ('title_content', str, ''),
            ('type', str, ''),
            ('url', str, ''),
            ('news_id', str, ''),
        ]
        fields.extend(super()._fields())
        return fields

    @classmethod
    def new(cls, form):
        news_id = form.pop('id', -1)
        print(form)
        m = super().new(form)
        m.news_id = news_id
        m.save()
        return m

    @classmethod
    def insert_db(cls, form):
        id = form.get('id')
        print('id', id)
        m = cls.find_one(news_id=id)
        if m is None:
            cls.new(form)
        else:
            m.update(form)
        return m
