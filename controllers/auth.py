# Import the needed libraries.
from flask import Blueprint, render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash

# Create the authentication blueprint.
auth = Blueprint('auth', __name__, template_folder='templates')

from app import User

@auth.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        # Get the information from the request.
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.get_user()

        if username != user['username']:
            return redirect('/login')
        # elif not check_password_hash(user['password'], password):
        #     return redirect('/login')
        else:
            return redirect('/admin')
    else:
        # Gather the needed information.
        kmarge = {
            'title': 'login',
            'path': '/home'
        }

        # Render the page.
        return render_template('login.html', **kmarge)

@auth.route('/logout', methods = ['POST'])
def logout():
    pass

@auth.route('/reset-password', methods = ['POST', 'GET'])
def reset_password():
    pass