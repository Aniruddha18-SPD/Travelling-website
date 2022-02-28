from user import User
class Packages:
    '''I am trying to make a dictionary and store id of customer with his name,age,gender and country. I am giving a customer unique id and 
    the packages keeps track of all the packages of the customer. He can add a new package or remove one.'''
    packages_for_customers={}
    def __init__(self,package_name,package_type,number_of_people,price):
        if (type(package_name) is not str) or (type(package_type) is not str) or (type(number_of_people) is not int) or (type(price) is not int):
            raise TypeError('Name and type of packages should be in string and number of people and price should be a integer.')
        self.package_name=package_name
        self.package_type=package_type
        self.number_of_people=number_of_people
        self.price=price
        self.cus_id=User.customer_id
        self.packages=[]
        Packages.packages_for_customers[self.cus_id]=[(package_name,package_type,number_of_people,price)]
        
    def addPackages(self,new_package):
        if type(new_package)!=str:
            return 'The package name should be a string'
        self.packages.append(new_package)
    def removePackages(self,remove_package):
        if type(remove_package)!=str:
            return 'The package name should be a string'
        if (self.packages.__contains__(remove_package)):
            self.packages.remove(remove_package)
        
