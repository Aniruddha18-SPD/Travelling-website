''' importing local files'''
from user import User
from user import Useraccount
from CLI_packing import CLI_Packing



'''Define Sign Up class'''
'''class variables: customers_information- to store customers' name, age, nationality and gender so that we can use the data for demographic calculation in the future
                  : customers_account- to store customers' account information i.e. their username and password for the authentication
    instance method: create_account() to either sign up for a new account or login.
'''

class Signup:
    customers_information = {}
    customers_account = {}
    
    def __init__(self):
        #takes user's first name
        current_user_first = input("Enter your first name: ")
        #takes user's second/last name
        current_user_second = input("Enter your second name: ")
        #stores user's full name
        self.full_name = current_user_first +" "+ current_user_second
        print(f'Welcome to the Lap of Himalayas, {self.full_name}!')
        #takes user's nationality
        current_user_nationality = input("Enter your nationality: ")
        #takes user's age
        current_user_age = input("Enter you age: ")
        #takes user's gender
        current_user_gender = input("Enter your gender: ")
        #creates a new user that consists of all of the information of the user
        self.current_user = User(current_user_first, current_user_second, current_user_nationality, current_user_age, current_user_gender)
        #stores full name as key in dictionay with the other information as value
        Signup.customers_information[self.full_name] = [current_user_nationality, current_user_age, current_user_gender]



    
    def create_account(self):
        #gather username and password for the accounts
        self.user_account = input("Have you created your account yet? Type 'Y' for Yes or 'N' for No! ")
        if self.user_account == 'Y':
            print("You can go and find the best packages after submitting your credentials!")
            customer_username = input("Enter your username: ")
            customer_password = input("Enter your password: ")
            if self.customers_account[customer_username] == customer_password:
                print("You successfully logged in. Let's go and find the best packages.")
                #pass username and password to the current user account to store the credentials.
                self.current_user_account = Useraccount(customer_username, customer_password) 
                #pass username and password to package booking               
                customer_package= CLI_Packing(customer_username,customer_password)
                customer_package.book_package(customer_username)
               
            else:
                print("You have either typed wrong credentials or have not signed up yet!")
                          
        else:
            username = True
            while username:
                customer_username = input("Enter your email: ")
                if customer_username in self.customers_account:
                    print("This email already exists.")
                    username = True
                else:
                    username = False
            customer_password = input("Enter your password: ")
            print("You successfully created your account")
            #pass username and password to the current user account & store them in dictionary and pass it to booking package
            self.current_user_account = Useraccount(customer_username, customer_password)
            Signup.customers_account[customer_username]= customer_password
            k=CLI_Packing(customer_username,customer_password)
            k.book_package(customer_username)
        
#create a sign up instance            
signup1 = Signup()
#prompts to create new account or use login user credentials to instance 
signup1.create_account()

