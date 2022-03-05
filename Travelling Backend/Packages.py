from user import Useraccount
class Packages:

    '''I am trying to make a dictionary and store id of customer with his package. I am keeping track of all the packages of the customer. Customer can add a new package or remove one.
    The dictionary packages_for_customers keep track of all the package information of the user and the packages for customers are stored in packages available which is a list.'''
    
    packages_for_customers={}
    packages_available=[]

    def __init__(self,customer_username,package_name,package_type,number_of_people,price):
        self.package_name=package_name
        self.customer_username=customer_username
        self.package_type=package_type
        self.number_of_people=number_of_people
        self.price=price
        if customer_username not in Useraccount.users_account:
            print("You have either typed wrong credentials or have not signed up yet!" )
        self.packages=[]

        #Checking the type of the information taken from the user.

        if type(package_name) != str:
            raise TypeError('The package name should be a string.')

        if type(package_type) != str:
            raise TypeError('The package type should be a string.')

        if type(number_of_people) != int:
            raise TypeError('The number of people should be an integer.')

        if type(price) != int:
            raise TypeError('The price can only be in integer.')

        #Storing the customer_username in the key of dictionary packages_for_customers and the package information is the value.

        Packages.packages_for_customers[Useraccount.users_account[0]]=[(package_name,package_type,number_of_people,price)]
        '''
        syntax changed from Packages.packages_for_customers[Useraccount.users_account[customer_username]]=
        [(package_name,package_type,number_of_people,price)]    to the one above ^    
        because of format change on user.py from Sanjay. '''

        Packages.packages_available.append(package_name)
    
    #This adds the package in the list of packages to keep track of packages for the future. The customer can add as much packages as he/she wants.

    def addPackages(self,new_package):
        if type(new_package)!=str:
            return 'The package name should be a string'
        self.packages.append(new_package)

    #Here the customer can remove the package if he/she doesn't like it. He can remove the package and select other packages of his wish.
    
    def removePackages(self,remove_package):
        if type(remove_package)!=str:
            return 'The package name should be a string'
        if (self.packages.__contains__(remove_package)):
            self.packages.remove(remove_package)
    
