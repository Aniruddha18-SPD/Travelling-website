# Define user class
class User:
    users = {}
    idCounter = 1

    def __init__(self, first, last, nationality, age, gender):

        if (type(first) is not str):
            raise TypeError("first name must be a string")
        if (type(last) is not str):
            raise TypeError("surname must be a string")
        if (type(nationality) is not str):
            raise TypeError("Nationality must be a string")
        if (type(int(age)) is not int):
            raise TypeError("Age must be an integer")
        if (type(gender) is not str):
            raise TypeError("gender must be a string")

        self.first = first
        self.last = last
        self.nationality = nationality
        self.age = age
        self.gender = gender
        self.userid = User.idCounter
        User.users[self.first+""+self.last] = [self.userid]
        User.idCounter += 1

'''Define Useraccount class'''
class Useraccount:
    users_account = {}
    def __init__(self, username, password):
        if (type(int(password)) is int):
            raise TypeError("Password should not just be integers.")

        if password.isalnum():
            raise TypeError("Password should also contain other characters.")

        self.username = username 
        self.password = password
        Useraccount.users_account[self.username]= self.password
      
       