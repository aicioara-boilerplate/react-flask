import sqlalchemy as sql

from ..application import db
from ..mixins.timestamp_mixin import TimestampMixin


class Dinosaur(db.Model, TimestampMixin):
    __tablename__ = "dinosaur"

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    name = sql.Column(sql.String)

    def __repr__(self):
        return "<Dinosaur {}>".format(self.name)
