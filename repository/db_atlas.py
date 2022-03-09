from repository.db_uri import db_uri
from mongoengine import connect
import certifi

class db_atlas:

    @staticmethod
    def connectDB():
        ca = certifi.where() 
        conexion = connect(host=db_uri, tlsCAFile=ca)
        return conexion["ollivanders"]["ollivanders"]