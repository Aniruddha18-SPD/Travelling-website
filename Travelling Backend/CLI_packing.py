from Packages import Packages

from Customer_rating import Rating
from Packages_available_with_us import packages_available_with_us
from Checkout import Checkout
from user import User
class CLI_packing:
    def __init__(self,customer_username,customer_id):
        self.customer_username=customer_username
        self.customer_id=customer_id

    def book_package(self,customer_username):
        print(f'WELCOME TO THE ADVENTURE NEPAL!!!,{customer_username}'+ '\n'+ 'What kind of packages do you like to get?'+'\n+NATURAL'+'\n+CULTURAL'+'\n+ADVENTUROUS'+'\n'+'Name the place you would love to visit!')
        user_choice_package_name=input('Enter the name of place you would like to visit in Nepal: ')
        user_choice_package_type=input('Enter the package type you want:Natural/Cultural/Adventurous')
        user_choice_number_of_people=input('How many people are you travelling?')
        user_choice_price=input('What is your budget?')
        this_package=Packages(customer_username,user_choice_package_name,user_choice_package_type,user_choice_number_of_people,user_choice_price)
        print(f'You have selected this package-,{this_package}')
        if this_package.package_name not in packages_available_with_us.keys():
            raise TypeError('The package is not available.')
        else:
            print(f'We have the package available with us,{this_package.package_name}')
            if this_package.price<packages_available_with_us[this_package.package_name][0] or this_package.price>packages_available_with_us[this_package.package_name][1]:
                print(f'We do not have the package available for your price.')
        print(f'Please make a payment and proceed to checkout!')
        Checkout(User.users[customer_username], Packages.packages_for_customers[User.users[customer_username]])
        
        
    def want_to_add_rating(self,customer_id):
        pack=input('Which package do you want to rate? ')
        rate=input('How many stars do you want to give to the package? ')
        rating=Rating(pack,customer_id,rate)
        print(f'Thanks for rating,{pack} {rating}')


#CLI_packing_for_user=CLI_packing(customer_username,customer_password)