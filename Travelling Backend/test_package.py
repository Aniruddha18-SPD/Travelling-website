import unittest
from Packages import Packages
from Customer_rating import Rating
from user import Useraccount

#data testing for class Packages
test_customer_username=["Pradeep",1,'Ram',2]
test_package_name="Trishuli River"
test_package_type="Adventure"
test_number_of_people=5
test_price=50
test_customer_id=1
test_rating=2
Useraccount.users_account=["Pradeep",1,'Ram',2]

#python3 -m unittest test_package.py
class TestBook(unittest.TestCase):
  def test_argument_values(self):
    #number of peoples and price should be in integers
    self.assertRaises(TypeError,Packages,test_customer_username[0],test_package_name,test_package_type,"Hari",test_price)
    self.assertRaises(TypeError,Packages,test_customer_username[0],test_package_name,test_package_type,2.2,test_price)
    self.assertRaises(TypeError,Packages,test_customer_username[0],test_package_name,test_package_type,test_number_of_people,'Fifty five')
    self.assertRaises(TypeError,Packages,test_customer_username[0],test_package_name,test_package_type,test_number_of_people,50.5)
    self.assertRaises(TypeError,Packages,test_customer_username[0],test_package_name,test_package_type,test_number_of_people,"55")

  def test_argument_types(self):
    #customers' username, packages' names and packages' types should be strings.
    self.assertRaises(TypeError,Packages,24,test_package_name,test_package_type,test_number_of_people,test_price)
    self.assertRaises(TypeError,Packages,test_customer_username[0],2,test_package_type,test_number_of_people,test_price)
    self.assertRaises(TypeError,Packages,test_customer_username[0],2.5,test_package_type,test_number_of_people,test_price)
    self.assertRaises(TypeError,Packages,2.44,test_package_name,test_package_type,test_number_of_people,test_price)
    self.assertRaises(TypeError,Packages,test_customer_username[0],24,test_package_type,test_number_of_people,test_price)
    self.assertRaises(TypeError,Packages,test_customer_username[0],test_package_name,33,test_number_of_people,test_price)
    self.assertRaises(TypeError,Packages,test_customer_username[0],test_package_name,33.77,test_number_of_people,test_price)
    self.assertRaises(TypeError,Packages,test_customer_username[0],test_package_name,44,test_number_of_people,test_price)

  def test_add_packages(self):
    #new packages must be an instance of the class Packages
    self.assertRaises(TypeError,Packages.addPackages,self,22)
    self.assertRaises(TypeError,Packages.addPackages,self,22.7)
    self.assertRaises(TypeError,Packages.addPackages,self,-9)
    
  def test_remove_packages(self):
    #packages to be removed should be also the instance of class Packages
    self.assertRaises(TypeError,Packages.removePackages,self,22)
    self.assertRaises(TypeError,Packages.removePackages,self,22.7)
    self.assertRaises(TypeError,Packages.removePackages,self,-9)
    testAddPackage=Packages(test_customer_username[0],test_package_name,test_package_type,test_number_of_people,test_price)
    testAddPackage.removePackages(test_package_name)
    testAddPackage.addPackages('Kathmandu Durbar Square')
    
  def test_updateRating(self):
        # rating must be an int
        self.assertRaises(TypeError, Rating,self,test_package_name,test_customer_id, 2.5)
        self.assertRaises(TypeError, Rating,self,test_package_name,test_customer_id,25)
        self.assertRaises(TypeError, Rating,self,test_package_name,test_customer_id,5)
        # rating must be an int between 0 and 5
        self.assertRaises(ValueError, Rating.updateRating, self, -1)
        self.assertRaises(ValueError, Rating.updateRating, self, 6)

if __name__ == "__main__":
    unittest.main(failfast=True)