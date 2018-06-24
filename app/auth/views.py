from flask import render_template
from . import auth



@auth.route('/login')
def login():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Login | One Min Pitch'
    # form = LoginForm()

    return render_template('auth/login.html', title = title )

@auth.route('/register')
def register():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Register | One Min Pitch'
    # form = RegistrationForm()

    return render_template('auth/login.html', title = title )
