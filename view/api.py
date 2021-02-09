from flask import Flask
from flask_restful import Api
from resources.stock_resource import StockResource


app = Flask(__name__)
api = Api(app)

api.add_resource(StockResource, '/api/stock', endpoint='stocks')
api.add_resource(StockResource, '/api/stock/<sku>', endpoint='stock')


@app.route('/')
def index():
    return 'Stock API'
