from flask_restful import Resource, reqparse
from models.hotel import HotelModel


class Hoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be left blank")
    argumentos.add_argument('estrelas', type=float, required=True, help="The field 'estrelas' cannot be left black" )
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'message': 'Hotel not found.'}, 404 #not found

    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message": "Hotel id '{}' already exists.".format(hotel_id)}, 400

        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'An internal error occured to save hotel.'}, 500
        return hotel.json()


    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotel_encontado = HotelModel.find_hotel(hotel_id)
        if hotel_encontado:
            hotel_encontado.update_hotel(**dados)
            hotel_encontado.save_hotel()
            return hotel_encontado.json(), 200
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'An internal error occured to save hotel.'}, 500
        return hotel.json(), 201

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message:' 'An error ocurred trying to delete hotel.'}, 500
            return {'message': 'Hotel deleted.'}
        return {'message': 'Hotel not found.'}, 404
