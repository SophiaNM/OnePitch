# One Miute Pitch
This is the fifth Independent project for Moringa Core, June 28th 2018.

## Description

One Minute Pitch is a web application that will allow users to post pitches, like, dislike and comment on other pitches.

## Features
- The home page allows users to see various pitches from the following Categories:
    - Interview
    - Promotion
    - Product
    - Business
- User can see all pitches for that category chosen.
- Users create an account and receive a welcome message in their email.
- Once registered a user can log in and have additional capabilities including:
    - A user can like and dislike a pitch but only once.
    - Users can additionally comment more than once on other pitches.
    - Users can as well create their own pitch.

## Behavior Driven Development
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| View All Pitches based on various categories | Default Home Page <br> Click on a category to see pitches | Displays all pitches |
| Register as a user | Click `register` on the navbar | Redirects to registration page to sign up |
| Log in as a user | Click on `log in` | Redirects to log in page |
| Update your Profile | Click on `Profile` | Redirects to profile page where you can update your bio and profile picture |
| Create a pitch | Click on `Add Pitch` on the home page or `Pitch` on the navbar | Redirects to pitches form page where you may create a pitch|
| Like or dislike a Pitch | Click on `Like` or `Dislike` button when logged in | Adds likes and dislikes to a pitch  |
| Comment on a pitch | Click on  `Comment`| Redirects to the Comments page where you can comment on other pitches and see other comments |


## View Live Site here
View the complete site [here](https://oneminpitch-sophia.herokuapp.com/)


## Technologies Used
    - Python 3.6
    - Flask Framework
    - HTML, CSS and Bootstrap
    - JavaScript
    - Postgressql
    - Heroku


## Set-up and Installation
    1. Clone or download the Repo
    2. Create a virtual environment:
        sudo apt-get install python3.6-venv
        python3.6 -m venv virtual source virtual/bin/activate
    3. Read the specs and requirements files and Install all the requirements.
    4. Install dependancies that will create an environment for the app to run:
        pip3 install -r requirements
    5. Edit the start.sh file to prepare your environment variables:
        export DATABASE_URL='postgresql+psycopg2://username:password@localhost/pitchit'
        export SECRET_KEY='Your secret key'
        export MAIL_USERNAME='Your email'
        export MAIL_PASSWORD='Your email password'
    6. Run database migrations:
        python manage.py db init
        python manage.py db migrate -m "initial migration"
        python manage.py db upgrade
    7. Run chmod a+x start.py
    8. Run ./start.py
    9. Access the application through `localhost:5000`

### Contributions
Yet to complete all tests for each model class. If you have ideas you may contribute to this project.

## Known bugs
No known bugs so far. If found drop me an email.


## Contributors
    - Sophia Murage

### Contact Information
njerimurage92@gmail.com | snmurage1@gmail.com
