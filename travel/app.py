from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.4,
        'diaria': 420.31,
        'cidade': 'São Paulo'
    },
    {
        'hotel_id': 'bravo',
        'nome': 'Bravo Hotel',
        'estrelas': 4.3,
        'diaria': 380.34,
        'Cidade': 'Ilhéus'
    },
    {
        'hotel_id': 'charlie',
        'nome': 'Charlie Hotel',
        'estrelas': 3.9,
        'diaria': 250.34,
        'cidade': 'Itacaré'
    },
]


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}

api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':
    app.run(debug=True)
