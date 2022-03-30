# -- Import section --
import os
from flask import Flask
from flask import render_template
from flask import request, redirect, session, url_for
from flask_pymongo import PyMongo
from model import Packages


# # -- Initialization section --
app = Flask(__name__)

# # name of database
# app.config['MONGO_DBNAME'] = 'database'

# # URI of database
# # Accessed from CONFIG VARS
# secret_key = os.environ.get('MONGO_URI')
# app.config['MONGO_URI'] = secret_key

# #Initialize PyMongo
# mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
#SIGNUP Route
@app.route('/signup', methods=['GET', 'POST'])
def singup():
    if request.method == "POST":
        username = request.form['username']
        password = (request.form['password'])
        confirm_password = (request.form['confirm password'])
        if password != confirm_password:
            return redirect('/signup')
        else:
            return render_template('login.html')


    
    else:
         return render_template('signup.html')
        
#LOGIN Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        users = mongo.db.users
        #search for username in database
        login_user = users.find_one({'name': request.form['username']})

        #if username in database
        if login_user:
            db_password = login_user['password']
            #encode password
            password = request.form['password'].encode("utf-8")
            #compare username in database to username submitted in form
            if bcrypt.checkpw(password, db_password):
                #store username in session
                session['username'] = request.form['username']
                return redirect(url_for('index'))
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
    if request.method == "GET":
        #render the form, with the packages list 
        return render_template('Booking.html', packages = Packages)
    else:
        #assign form data to variables
        type = request.form['type']
        name = request.form['name']
        price = request.form['price']
        number_of_people=request.form['number_of_people']

        #retrieve username from session data if present
        if session:
            user = session['username']
        else:
            user = None

        collection = mongo.db.library
        
        #insert an entry to the database using the variables declared above
        collection.insert_one({"type":type, "name":name,  "price": price, "number_of_people": number_of_people})

        #redirect to the index route upon form submission
        return redirect('/')
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



       