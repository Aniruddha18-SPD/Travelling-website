# -- Import section --
import os
from flask import Flask
from flask import render_template
from flask import request, redirect, session, url_for
from flask_pymongo import PyMongo
from model import Packages


# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
# Accessed from CONFIG VARS
secret_key = os.environ.get('MONGO_URI')
app.config['MONGO_URI'] = secret_key

#Initialize PyMongo
mongo = PyMongo(app)



# Package Route
@app.route('/new', methods=['GET', 'POST'])
def new_book():
    if request.method == "GET":
        #render the form, with the genre list to populate the dropdown menu
        return render_template('Booking.html', packages = packages)
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


       