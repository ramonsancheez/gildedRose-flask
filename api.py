from flask import Flask
from flask_restful import Api
from resources.index import index
from resources.inventario import inventario
from resources.nombre import nombre
from resources.quality import quality

app = Flask(__name__)
api = Api(app, catch_all_404s=True)


api.add_resource(index, "/")
api.add_resource(inventario, "/inventario")
api.add_resource(nombre, "/nombre/<itemNombre>")
api.add_resource(quality, "/quality/<numQuality>")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)