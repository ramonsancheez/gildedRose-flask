from flask_restful import Resource
from services.service  import service

class delete(Resource):
    def get(self, deletedItemName):
        return service.delete_item(deletedItemName)