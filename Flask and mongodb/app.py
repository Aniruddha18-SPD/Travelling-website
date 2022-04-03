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
        current_user = users.find_one({'email': request.form['username']})

        #if user not in database
        if not current_user:
            username = request.form['username']
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            gender = request.form['gender']
            nationality = request.form['nationality']
            #encode password for hashing
            password = (request.form['password']).encode("utf-8")
            confirm_password = (request.form['confirm password']).encode("utf-8")
            if password != confirm_password:
                return render_template('signup.html', error = 'Re-enter the same password!' )
            #add new user to database
            users.insert_one({'firstname':firstname, 'lastname':lastname, 'email': username, 'password': password, 'gender': gender, 'nationality': nationality})
            #store username in session
            session['username'] = request.form['firstname']
            return redirect('/login')

        else:
            return render_template('signup.html', registration= 'User already exists!' )
            
    
    else:
        return render_template('signup.html')
        
#LOGIN Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        users = mongo.db.users
        #search for username in database
        login_user = users.find_one({'email': request.form['email']})

        #if username in database
        if login_user:
            db_password = login_user['password']
            #encode password
            password = request.form['password'].encode("utf-8")
            #compare password in database to password submitted in form
            if password == db_password:
                session['username'] = login_user['firstname']
                return render_template('index.html')
            else:
                return render_template('login.html', error1 = 'Invalid username or password combination.')
        else:
            return render_template('login.html', error2 = 'User not found!')
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
    
@app.route('/people_exp')
def people_exp():
    return render_template('people_exp.html')




# Package Route
@app.route('/new', methods=['GET', 'POST'])
def new_package():
    if session:
        if request.method == "GET":
        #render the form, with the packages list 
            return render_template('Booking.html', packages = packages)
        else:
        #assign form data to variables
            type = request.form['type']
            name = request.form['name']
            price = request.form['price']
            number_of_people=request.form['number_of_people']

        #retrieve username from session data if present
        

            collection = mongo.db.library
        
        #insert an entry to the database using the variables declared above
            collection.insert_one({"type":type, "name":name,  "price": price, "number_of_people": number_of_people})

        #redirect to the index route upon form submission
        #return redirect('/')
            return render_template('Booking.html', packages = packages)
    else:
        return render_template('login.html')            
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




@app.route('/Checkout' , methods = ['GET', 'POST'])
def experiences():
    if request.method == 'GET':
        return render_template('Checkout.html')
    elif request.method == 'POST':
        cardnumber = request.form['cardnumber']
        num = cardnumber                                     # this function adds every digit of the card number to a list and,
        validlist=[]
        credit_check = False
        num =  int(num)
        if type(num) != int:
            raise TypeError("The input must be a number")

        if num <= 0 or len(str(num)) > 16:
            raise ValueError("Number can't be negative and the length can't be greater than 16")         
        
        num =  str(num)
        #while not credit_check:
        for i in num:
            validlist.append(int(i))
        for i in range(0,len(num),2):                                             # applying Luhn Algorithm to check whether resulting sum is divisible by ten
            validlist[i] = validlist[i] * 2
            if validlist[i]  >= 10:
                validlist[i] =  (validlist[i]//10 + validlist[i]%10)
        
        if sum(validlist)% 10 == 0:
            credit_check = True
            print("This is a VALID CARD!")
            return render_template('popup.html')
        
        else:
            credit_check = False
            print('INVALID CARD NUMBER')
            return render_template('repeat_transaction.html')



       
