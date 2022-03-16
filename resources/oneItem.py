from flask_restful import Resource
from services.service  import service

class oneItem(Resource):
    def get(self, name, quality, sell_in):
        return service.get_oneItem(name, quality, sell_in)