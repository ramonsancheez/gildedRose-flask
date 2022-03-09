from flask_restful import Resource
from services.service import service

class index(Resource):

    def get(self):
        return "BIENVENIDO A LA API DE OLLIVANDERS"