from flask_restful import Resource
from services.service  import service

class quality(Resource):
    def get(self, numQuality):
        return service.get_quality(numQuality)