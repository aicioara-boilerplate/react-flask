from ..application import db
from ..mixins.timestamp_mixin import TimestampMixin


class Dinosaur(db.Model, TimestampMixin):
    __tablename__ = "dinosaur"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

    def __repr__(self):
        return "<Dinosaur {}>".format(self.name)
