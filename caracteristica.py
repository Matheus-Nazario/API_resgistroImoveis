from flask_restful import Resource

caracteristica = ['piscina', 'park', 'estacionamento', 'Shopping']
class Caracteristica(Resource):
    def get(self):
        return caracteristica