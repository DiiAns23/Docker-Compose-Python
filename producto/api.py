from flask import Flask
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        return {
            'producto': [
                'Helado',
                'Chocolate',
                'Fruta',
                'Caramelo'
            ]
        }

api.add_resource(Product,'/producto')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)