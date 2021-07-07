# Import the needed libraries.
from flask import Blueprint, render_template, request, redirect

# Create the authentication blueprint.
auth = Blueprint('auth', __name__, template_folder='templates')

from app import User

@auth.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        # Get the information from the request.
        username = request.form['username']
        password = request.form['password']

        user = User.get_user()

        print(user)
        if username == user['username']:
            return redirect('/admin')
        else:
            return redirect('/login')
    else:
        # Gather the needed information.
        kmarge = {
            'title': 'login',
            'path': '/home'
        }

        # Render the page.
        return render_template('login.html', **kmarge)