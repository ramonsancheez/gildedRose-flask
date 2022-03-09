from flask_restful import Resource
from services.service  import service

class sell_in(Resource):
    def get(self, numSellIn):
        return service.get_sellIn(numSellIn)