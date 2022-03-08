import unittest
from user import User, Useraccount

#data testing for class User
testUser = User("Aniruddha", "Pokhrel", "Nepali", 21, "Male")
testUser2 = User("Pradeep", "Lamichhane", "Nepali", 21, "Male")



#python3 -m unittest main.py
class TestUser(unittest.TestCase):
  def test_argument_types(self):
    # first name must be string
    self.assertRaises(TypeError, User, 0, "Pokhrel", "Nepali", 21, "Male")
    self.assertRaises(TypeError, User, 12.5, "Lamichhane", "Nepali", 21, "Male")

    #second name must be string
    self.assertRaises(TypeError, User, "Aniruddha", 12, "Nepali", 21, "Male")
    self.assertRaises(TypeError, User, "Pradeep", 0, "Nepali", 21, "Male")

    #nationality should also be string
    self.assertRaises(TypeError, User, "Aniruddha", "Pokhrel",0,  21, "Male")
    self.assertRaises(TypeError, User, "Pradeep", "Lamichhane",1800, 21, "Male")

    #age must be integer
    self.assertRaises(TypeError, User, "Aniruddha", "Pokhrel","Nepali", "twentyone", "Male")
    self.assertRaises(TypeError, User, "Pradeep", "Lamichhane","Nepali", "twentytwo", "Male")

    #age must be greater than 10 and less than 70
    self.assertRaises(ValueError, User, "Aniruddha", "Pokhrel","Nepali", 0, "Male")
    self.assertRaises(ValueError, User, "Pradeep", "Lamichhane","Nepali", 82, "Male")

    #gender should be string
    self.assertRaises(TypeError, User, "Aniruddha", "Pokhrel","Nepali", 10, 19)
    self.assertRaises(TypeError, User, "Pradeep", "Lamichhane","Nepali", 18, 0)

  def test_user_list(self):
    # assert that the users were added to the list of users
    self.assertEqual(len(User.users), 4)
    # assert that the users is an instance of User class
    self.assertIsInstance(testUser, User)
    self.assertIsInstance(testUser2, User)
    
    # assert that the usernames are correct and the user ids increment
    self.assertEquals(User.users[0], "Aniruddha Pokhrel")
    self.assertIs(User.users[1], 1)
    self.assertEquals(User.users[2] , "Pradeep Lamichhane")
    self.assertIs(User.users[1], 1)
    


#data testing for class Useraccount
testUseraccount = Useraccount("aniruddha@gmail.com", "iamanirudd123")
testUseraccount2 = Useraccount("pradeep@gmail.com", "iampradeep123")

class TestUseraccount(unittest.TestCase):
  def test_argument_types(self):
    #username should be string
    
    #username should contain valid domain: @gmail.com
    self.assertRaises(TypeError, Useraccount, "aniruddha@mail.com", "iamanirudd123")
    self.assertRaises(TypeError, Useraccount, "pradeep@lamichhane.com", "iampradeep123")

    self.assertRaises(TypeError, Useraccount, 1, "iamanirudd123")
    self.assertRaises(TypeError, Useraccount, 3, "iampradeep123")

    #password should have length of atleast 10 digits or characters
    self.assertRaises(TypeError, Useraccount, "aniruddha@gmail.com", "iamanirud")
    self.assertRaises(TypeError, Useraccount, "pradeep@gmail.com", "iam123")

    #password should atleast be the combination of the digits and alphabets
    self.assertRaises(TypeError, Useraccount, "aniruddha@gmail.com", "iamaniruddhafromNepal")
    self.assertRaises(TypeError, Useraccount, "pradeep@gmail.com", "iampradeeplamichhane")


 

if __name__ == "__main__":
    unittest.main(failfast=True)