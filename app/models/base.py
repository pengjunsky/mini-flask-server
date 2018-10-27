from datetime import datetime

from flask import current_app
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, Integer, SmallInteger, inspect, orm
from contextlib import contextmanager

from app.libs.error_code import NotFound


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    @contextmanager
    def auto_check_empty(self, e):
        try:
            yield
        except Exception:
            raise e


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident):
        rv = self.get(ident)
        if rv is None:
            raise NotFound()
        return rv

    def first_or_404(self):
        rv = self.first()
        if rv is None:
            raise NotFound()
        return rv


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    delete_time = Column(Integer)
    update_time = Column(Integer)
    status = Column(SmallInteger, default=1)  # 软删除

    @orm.reconstructor
    def init_on_load(self):
        self.exclude = ['create_time', 'update_time', 'delete_time', 'status']
        all_columns = inspect(self.__class__).columns.keys()
        self.fields = list(set(all_columns) - set(self.exclude))

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def __getitem__(self, item):
        return getattr(self, item)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def get_url(self, url):
        if (self._from == 1):
            return current_app.config['IMG_PREFIX'] + url
        else:
            return url

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    def delete(self):
        self.status = 0
        self.delete_time = int(datetime.now().timestamp())

    def update(self):
        self.update_time = int(datetime.now().timestamp())

    def keys(self):
        return self.fields

    def hide(self, *keys):
        for key in keys:
            self.fields.remove(key)
        return self

    def append(self, *keys):
        for key in keys:
            self.fields.append(key)
        return self
