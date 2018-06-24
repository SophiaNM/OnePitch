from flask import render_template,request,redirect,url_for,abort
from . import main

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    return render_template('index.html', title = title )


@main.route('/register')
def register():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Register'
    form = RegistrationForm()

    return render_template('register.html', title = title )


@main.route('/login')
def login():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Login'
    form = LoginForm()

    return render_template('login.html', title = title )
