# -- Import section --
import os
from flask import Flask
from flask import render_template
from flask import request, redirect, session, url_for
from flask_pymongo import PyMongo
from model import packages
import secrets


# # -- Initialization section --
app = Flask(__name__)

# # name of database
app.config['MONGO_DBNAME'] = 'database'

# # URI of database
# # Accessed from CONFIG VARS
secret_key = os.environ.get('MONGO_URI')
app.config['MONGO_URI'] = "mongodb+srv://admin:iamCool100!@cluster0.dhqv0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# #Initialize PyMongo
mongo = PyMongo(app)
app.secret_key = secrets.token_urlsafe(16)

@app.route('/')
#INDEX Route
@app.route('/index')
def index():
    return render_template('index.html')
#SIGNUP Route
@app.route('/signup', methods=['GET', 'POST'])
def singup():
    if request.method == "POST":
        users = mongo.db.users
        #search for username in database
        current_user = users.find_one({'name': request.form['username']})

        #if user not in database
        if not current_user:
            username = request.form['username']
            #encode password for hashing
            password = (request.form['password']).encode("utf-8")
            #add new user to database
            users.insert_one({'name': username, 'password': password})
            #store username in session
            session['username'] = request.form['username']
            return redirect('/login')

        else:
            return 'Username already registered.  Try logging in.'
    
    else:
        return render_template('signup.html')
        
#LOGIN Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        users = mongo.db.users
        #search for username in database
        login_user = users.find_one({'name': request.form['email']})

        #if username in database
        if login_user:
            db_password = login_user['password']
            #encode password
            password = request.form['password'].encode("utf-8")
            #compare username in database to username submitted in form
            if password == db_password:
                session['username'] = request.form['email']
                return redirect(url_for('index2'))
            else:
                return 'Invalid username/password combination.'
        else:
            return 'User not found.'
    else:
        return render_template('login.html')

#LOGOUT Route
@app.route('/logout')
def logout():
    #clear username from session data
    session.clear()
    return redirect('/')




@app.route('/package')
def package():
    return render_template('packages.html')




# Package Route
@app.route('/new', methods=['GET', 'POST'])
def new_package():
    if session:
            user = session['username']
            collection = mongo.db.library
            if request.method == "GET":
            #render the form, with the packages list 
                return render_template('Booking.html', packages = packages)
            else:
                #assign form data to variables
                types = request.form['types']
                price = request.form['price']
                number_of_people=request.form['number_of_people']
        
            #insert an entry to the database using the variables declared above
            collection.insert_one({"type":types, "price": price, "number_of_people": number_of_people})

            #redirect to the index route upon form submission
            #return redirect('/')
            return render_template('index.html', packages = packages)
    else:
        user = None
        return render_template('login.html')
    

        #retrieve username from session data if present
    

        
@app.route('/mypackages')
def my_packages():
    collection = mongo.db.library
    #retrieve username from session data if present
    if session:
        user = session['username']
    else:
        user = None
    #find entries whose user matches the session user
    name = collection.find({"user":user})
    return render_template('index.html', name=name, packages=packages, label="My")

@app.route('/mypackages/<name>/remove_package')
def remove_package(name):
    collection=mongo.db.library
    if session:
        user=session['username']
    else:
        user=None
    name = collection.find({"user":user})
    collection.delete_one(name)
    return redirect('/')



       