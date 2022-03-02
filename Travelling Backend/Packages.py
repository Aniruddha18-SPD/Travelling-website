from signup import Signup
from user import User
class Packages:
    '''I am trying to make a dictionary and store id of customer with his package. I am keeping track of all the packages of the customer. Customer can add a new package or remove one.'''
    packages_for_customers={}
    packages_available=[]
    def __init__(self,customer_username,package_name,package_type,number_of_people,price):
        if (type(package_name) is not str) or (type(package_type) is not str) or (type(number_of_people) is not int) or (type(price) is not int):
            raise TypeError('Name and type of packages should be in string and number of people and price should be a integer.')
        self.package_name=package_name
        self.customer_username=customer_username
        self.package_type=package_type
        self.number_of_people=number_of_people
        self.price=price
        if customer_username not in User.users.keys():
            print("You have either typed wrong credentials or have not signed up yet!" )
        self.packages=[]
        Packages.packages_for_customers[User.users[customer_username]]=[(package_name,package_type,number_of_people,price)]
        Packages.packages_available.append(package_name)
        
    def addPackages(self,new_package):
        if type(new_package)!=str:
            return 'The package name should be a string'
        self.packages.append(new_package)
    def removePackages(self,remove_package):
        if type(remove_package)!=str:
            return 'The package name should be a string'
        if (self.packages.__contains__(remove_package)):
            self.packages.remove(remove_package)
    
