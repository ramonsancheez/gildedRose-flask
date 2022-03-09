from repository.db_uri import db_uri
from mongoengine import connect

class db_atlas:

    @staticmethod
    def connectDB():
        # ca = certifi.where(), tlsCAFile=ca
        conexion = connect(host=db_uri)
        return conexion["ollivanders"]["ollivanders"]