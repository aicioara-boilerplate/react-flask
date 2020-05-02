import logging

from .. import exceptions
from ..application import db
from ..models import Dinosaur


def list(page_size=50, offset=0):
    objs = (Dinosaur.query
        .order_by(Dinosaur.id.desc())
        .limit(page_size)
        .all()
    )
    return objs


def create(data):
    obj = Dinosaur(**{
        'name': data.get('name', None),
    })

    db.session.add(obj)
    db.session.commit()

    return obj


def retrieve(id):
    obj = Dinosaur.query.get(id)

    if obj is None:
        raise exceptions.HTTP_404_NOT_FOUND('Dinosaur with id {} not found'.format(id))

    return obj


def update(id, data):
    obj = retrieve(id)

    for key, value in data.items():
        setattr(obj, key, value)

    db.session.commit()
    return obj


def delete(id):
    obj = retrieve(id)

    db.session.delete(obj)
    db.session.commit()

    return obj
