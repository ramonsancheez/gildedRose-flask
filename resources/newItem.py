from flask_restful import Resource
from services.service  import service

class newItem(Resource):
    def get(self, name, quality, sell_in):
        return service.newItem(name, quality, sell_in)