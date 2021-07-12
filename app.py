# Import the needed libraries.
from flask import Flask, render_template
from flask_session import Session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Create the applications.
app = Flask(__name__)

# Create the database connection.
app.config["MONGO_URI"] = "mongodb://client:altosax12@cluster0-shard-00-00.o3xao.mongodb.net:27017,cluster0-shard-00-01.o3xao.mongodb.net:27017,cluster0-shard-00-02.o3xao.mongodb.net:27017/shop?ssl=true&replicaSet=atlas-10dcip-shard-0&authSource=admin&retryWrites=true&w=majority"
mongo = PyMongo(app)

# Get the shop collection.
user_db = mongo.db.user
products_db = mongo.db.products

class Products:
    def add_product(product):
        result = products_db.insert_one(product)
        return result

    def update_product(id, product):
        filter = {'_id': ObjectId(id)}
        values = {'$set': product}
        result = products_db.update_one(filter, values)
        return result

    def delete_product(id):
        products_db.delete_one({'_id': ObjectId(id)})

    def get_product(id):
        products = []
        data = products_db.find({'_id': ObjectId(id)})
        for product in data:
            output = {
                'id': str(product['_id']),
                'title': product['title'],
                'imageUrl': product['imageUrl'],
                'description': product['description'],
                'options': product['options'],
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
                'options': product['options'],
                'price': product['price']
            }
            products.append(output)

        return products

class User:
    def get_user():
        users = []
        data = user_db.find()
        for user in data:
            output = {
                'id': str(user['_id']),
                'username': user['username'],
                'password': user['password']
            }
            users = output
        
        return users

# Configure the sessions in the web app.
# with app.app_context():
#     app.session_interface = MongoDBSessionInterface(app, mongo.db, 'sessions')
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "mongodb"
# app.config["SESSION_MONGODB_DB"] = "shop"
# app.secret_key = "\xd5$\xa2\xd5\xd8\x06\xab\xa4\xb5\x86\xec\xf1Tn[s"
# Session(app)

# Configure the sessions in the web app.
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "\xd5$\xa2\xd5\xd8\x06\xab\xa4\xb5\x86\xec\xf1Tn[s"
Session(app)

# Import the controllers.
from controllers.admin import admin
from controllers.shop import shop
from controllers.auth import auth

# Call the shop blueprint.
app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(shop)

# The 404 handler.
@app.errorhandler(404)
def not_found(e):
    # Gather the need information.
    kmarge = {
        'title': 'Page Not Found',
        'path': '/home'
    }

    # Render the page and return the 404 code.
    return render_template('404.html', **kmarge), 404

# Start the application.
if __name__ == '__main__':
    app.run(debug=True)