from flask_restful import Resource
from services.service import service

class nombre(Resource):
    def get(self, itemNombre):
        return service.get_nombre(itemNombre)