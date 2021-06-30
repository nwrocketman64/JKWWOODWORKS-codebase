from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from app import mongo

products_db = mongo.db.products

class Products:
    def add_product(product):
        result = products_db.insert_one(product)
        return result

    def update_product():
        pass

    def delete_product():
        pass

    def get_product(id):
        products = []
        data = products_db.find({'_id': ObjectId(id)})
        for product in data:
            output = {
                'id': str(product['_id']),
                'title': product['title'],
                'imageUrl': product['imageUrl'],
                'description': product['description'],
                'price': product['price']
            }
            products = output
        
        return products

    def get_products():
        products = []
        data = products_db.find()
        for product in data:
            output = {
                'id': str(product['_id']),
                'title': product['title'],
                'imageUrl': product['imageUrl'],
                'description': product['description'],
                'price': product['price']
            }
            products.append(output)

        return products