from Packages import Packages
class Rating:
    '''Here the customer can add rating to the package that he/she took and give the package stars in between 1 to 5'''
    def __init__(self,package,cus_id,rating):
        if cus_id not in Packages.packages_for_customers:
            raise ValueError('The customer ID should be available.')
        if package not in Packages.packages_available:
            raise ValueError('The package is not available.')
        if type(package) not in [str]:
            raise TypeError('The package name should be a string')
        if type(rating) not in [int]:
            raise TypeError('The rating should be an integer.')
        if rating<0 or rating>5:
            raise ValueError('The rating should be in between 1 and 5.')
        self.package=package
        self.rating=rating
        self.cus_id=cus_id
    def updateRating(self,newRating):
        if type(newRating) not in [int]:
            raise TypeError('The rating should be an integer.')
        if newRating<0 or newRating>5:
            raise ValueError('The rating should be in between 1 and 5.')
        self.rating=newRating
        
