class Customer:
    '''I am trying to make a dictionary and store id of customer with his name,age,gender and country. I am giving a customer unique id and 
    the packages keeps track of all the packages of the customer. He can add a new package or remove one.'''
    customers={}
    customer_id=1
    def __init__(self,name,age,gender,country):
        if (type(name) is not str) or (type(age) is not int) or (type(gender) is not str) or (type(country) is not str):
            raise TypeError('Name, gender and country should be in string and age should be a integer.')
        self.name=name
        self.age=age
        self.gender=gender
        self.country=country
        self.cus_id=Customer.customer_id
        self.packages=[]
        Customer.customers[Customer.customer_id]=[self.name,self.age,self.gender,self.country]
        Customer.customer_id+=1
    def addPackages(self,new_package):
        if type(new_package)!=str:
            return 'The package name should be a string'
        self.packages.append(new_package)
    def removePackages(self,remove_package):
        if type(remove_package)!=str:
            return 'The package name should be a string'
        if (self.packages.__contains__(remove_package)):
            self.packages.remove(remove_package)
        
