from flask_restful import Resource
from services.service  import service

class updateItem(Resource):
    def get(self, item, quality, sell_in):
        return service.updateItem(item, quality, sell_in)