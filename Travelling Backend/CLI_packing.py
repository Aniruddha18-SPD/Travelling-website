from Packages import Packages
from Customer_rating import Rating
from Packages_available_with_us import packages_available_with_us
from Checkout import Checkout
from user import Useraccount
class CLI_Packing:

    '''This is a class which takes input from the user. It works as a constructor for the class Package which lets the user choose
    the package they want to book for travelling. It runs after taking the information about user from class Signup. This class makes 
    the information of the customer i.e. package name, package type, number of people and price and pass this to store in class 
    Package. There is a function named want_to_add_rating which lets the user rate the package they booked.'''

    def __init__(self,customer_username,customer_id):
        self.customer_username=customer_username
        self.customer_id=customer_id

    def book_package(self,customer_username):

        #This will print some informations about our website to the user and ask for the informations about the package with the user.

        print(f'WELCOME TO THE ADVENTURE NEPAL!!!,{customer_username}'+ '\n'+ 'What kind of packages do you like to get?'+'\n+NATURAL'+'\n+CULTURAL'+'\n+ADVENTUROUS'+'\n'+'Name the place you would love to visit! ')
        user_choice_package_name=input('Enter the name of place you would like to visit in Nepal!!: ')
        user_choice_package_type=input('Enter the package type you want:Natural / Cultural / Adventurous ?')
        user_choice_number_of_people=input('How many people are you travelling? ')
        user_choice_price=input('What is your budget? ')

        #The information of package from the customer is passed to the class Package to store the information for booking and future use.

        package_customer_selected=Packages(customer_username,user_choice_package_name,user_choice_package_type,user_choice_number_of_people,user_choice_price)

        print(f'You have selected this package-, {user_choice_package_name} ')

        #Checking the type of the information taken from the user.

        if type(user_choice_package_name) != str:
            raise TypeError('The package name should be a string.')

        if type(user_choice_package_type) != str:
            raise TypeError('The package type should be a string.')

        if type(user_choice_number_of_people) != int:
            raise TypeError('The number of people should be an integer.')

        if type(user_choice_price) != int:
            raise TypeError('The price can only be in integer.')

        #Checking if the package selected by customer is available with us or not in the packages_available_with_us.

        if package_customer_selected.package_name not in packages_available_with_us.keys():
            raise TypeError('The package is not available.')
        else:
            print(f'We have the package available with us,{package_customer_selected.package_name}')

        #Checking if the price entered by the user is within our price range or not in the dictionary with all the packages.

            if int(package_customer_selected.price)<packages_available_with_us[package_customer_selected.package_name][0] or int(package_customer_selected.price)>packages_available_with_us[package_customer_selected.package_name][1]:
                print(f'We do not have the package available for your price.')

        print(f'Please make a payment and proceed to checkout!')
        #After checking all the informations provided by user with our package this helps the user to proceed towards the checkout and billing.
        Checkout(Useraccount.users_account, Packages.packages_for_customers)
        


