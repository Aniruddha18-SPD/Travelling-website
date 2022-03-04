from Packages import Packages
class Rating:

    '''This is the class for helping the user rate our packages. The customer books the package and enjoy the trip. Later,
    he can rate the package so that we can improve. Here the customer can add rating to the package that he/she took and give
    the package stars in between 1 to 5'''

    #The rating for packages is the dictionary which keeps track of all the different ratings from different users.

    Rating_for_packages={}

    def __init__(self,package,cus_id,rating):

        #Checking if the cus_id is valid or not. If the user is not our customer, he won't be able to rate our packages.
        if cus_id not in Packages.packages_for_customers:
            raise ValueError('The customer ID should be available.')

        #Checking if the package is the package customer chose which we stored in the list.
        if package not in Packages.packages_available:
            raise ValueError('The package is not available.')

        #Checking if the type of the package is a string.
        if type(package) not in [str]:
            raise TypeError('The package name should be a string')

        #Checking if the rating is in integer. The number given is equal to number of stars for the package.
        if type(rating) not in [int]:
            raise TypeError('The rating should be an integer.')
        
        #The rating should be greater than 0 and smaller than 5. Checking this and giving ValueError if customer does mistakes.
        if rating<0 or rating>5:
            raise ValueError('The rating should be in between 1 and 5.')

        self.package=package
        self.rating=rating
        self.cus_id=cus_id

        #We are storing the name of package in key and customer id and the rating he provided in values of the dictionary.

        Rating.Rating_for_packages[package]=(cus_id,rating)

    #This is the function that will provide the user with a chance to update the rating. If the user is not satisfied with the previous rating he gave the package, he can update it here.
  
    def updateRating(self,newRating):

        #Checking if the newRating user provided is a integer or not.
        if type(newRating) not in [int]:
            raise TypeError('The rating should be an integer.')

        #Rating should be in between 0 and 5.
        if newRating<0 or newRating>5:
            raise ValueError('The rating should be in between 1 and 5.')

        #This will replace the previous rating in dictionary with the new rating.
        self.rating=newRating
        
        Rating.Rating_for_packages[self.package]=(self.cus_id,newRating)
        
