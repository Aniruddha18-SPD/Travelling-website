from Packages import Packages
from signup import Signup
from Customer_rating import Rating
class CLI_packing:
    def __init__(self,customer_username):
        print(f'WELCOME TO THE ADVENTURE NEPAL!!!,{customer_username}'+ '\n'+ 'What kind of packages do you like to get?'+'\n+NATURAL'+'\n+CULTURAL'+'\n+ADVENTUROUS'+'\n'+'Name the place you would love to visit!')
        user_choice_package_name=input('Enter the name of place you would like to visit in Nepal: ')
        user_choice_package_type=input('Enter the package type you want:Natural/Cultural/Adventurous')
        user_choice_number_of_people=input('How many people are you travelling?')
        user_choice_price=input('What is your budget?')
        this_package=Packages(customer_username,user_choice_package_name,user_choice_package_type,user_choice_number_of_people,user_choice_price)
        print(f'You have selected this package-,{this_package}')
        print(f'Please make a payment and proceed to checkout!')
        
    def want_to_add_rating(self,customer_id):
        pack=input('Which package do you want to rate? ')
        rate=input('How many stars do you want to give to the package? ')
        rating=Rating(pack,customer_id,rate)
        print(f'Thanks for rating,{pack} {rating}')


