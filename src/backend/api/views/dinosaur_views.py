import logging

from flask import request
from flask_restplus import Resource, Namespace, fields

from ..managers import dinosaur_manager
from ..exceptions import HTTP_EXCEPTION


api = Namespace('dinosaurs', description='Dinosaur related operations')

dto = api.model('dinosaur', {
    'id': fields.Integer(readonly=True, example=1),
    'name': fields.String(required=True, example='T-Rex'),

})


@api.route('/')
class DinosaurList(Resource):

    @api.marshal_list_with(dto)
    def get(self):
        """
        List all Dinosaurs
        """
        try:
            return dinosaur_manager.list(), 200
        except HTTP_EXCEPTION as e:
            api.abort(e.code, e.payload)
        except Exception as e:
            logging.exception(e, exc_info=True)
            api.abort(500, str(e))


    @api.expect(dto, validate=True)
    @api.marshal_with(dto, code=201)
    def post(self):
        """
        Create a new Dinosaur
        """
        try:
            return dinosaur_manager.create(request.json), 201
        except HTTP_EXCEPTION as e:
            api.abort(e.code, e.payload)
        except Exception as e:
            logging.exception(e, exc_info=True)
            api.abort(500, str(e))



@api.route('/<id>')
@api.param('id', 'The Dinosaur Identifier')
@api.response(404, 'Dinosaur not found.')
class Dinosaur(Resource):

    @api.marshal_with(dto, code=200)
    def get(self, id):
        """
        Retrieve a specific Dinosaur
        """
        try:
            return dinosaur_manager.retrieve(id), 200
        except HTTP_EXCEPTION as e:
            api.abort(e.code, e.payload)
        except Exception as e:
            logging.exception(e, exc_info=True)
            api.abort(500, str(e))


    @api.expect(dto, validate=True)
    @api.marshal_with(dto, code=202)
    def patch(self, id):
        """
        Update a specific Dinosaur
        """
        try:
            return dinosaur_manager.update(id, request.json), 202
        except HTTP_EXCEPTION as e:
            api.abort(e.code, e.payload)
        except Exception as e:
            logging.exception(e, exc_info=True)
            api.abort(500, str(e))


    @api.marshal_with(dto, code=204)
    def delete(self, id):
        """
        Delete a specific Dinosaur
        """
        try:
            return dinosaur_manager.delete(id), 204
        except HTTP_EXCEPTION as e:
            api.abort(e.code, e.payload)
        except Exception as e:
            logging.exception(e, exc_info=True)
            api.abort(500, str(e))
