# Import the needed libraries.
from flask import Blueprint, render_template

# Create the shop blueprint.
shop = Blueprint('shop', __name__, template_folder='templates')

# GET / aka the homepage.
@shop.route('/')
def index():
    # Gather the needed information.
    kmarge = {
        'title': 'Home',
        'path': '/home'
    }

    # Render the page.
    return render_template('index.html', **kmarge)

# GET /products
# The routes gives the list of products.
@shop.route('/products')
def products():
    # Gather the needed information.
    kmarge = {
        'title': 'Products',
        'path': '/products'
    }

    # Render the page.
    return render_template('products.html', **kmarge)

# GET /order
# The routes gives the order form.
@shop.route('/order')
def order():
    # Gather the needed information.
    kmarge = {
        'title': 'Order',
        'path': '/order'
    }

    # Render the page.
    return render_template('order.html', **kmarge)

# GET /contact
# The route gives the contact form.
@shop.route('/contact')
def contact_us():
    # Gather the needed information.
    kmarge = {
        'title': 'Contact Us',
        'path': '/contact'
    }

    # Render the page.
    return render_template('contact.html', **kmarge)

# GET /about
# The route give the about information.
@shop.route('/about')
def about_us():
    # Gather the needed information.
    kmarge = {
        'title': 'About Us',
        'path': '/about'
    }

    # Render the page.
    return render_template('about.html', **kmarge)