from Packages import Packages
from Customer.rating.py import Rating
from places_to_visit import places
class CLI_packing:
    def __init__(self):
        print('WELCOME TO THE ADVENTURE NEPAL!!!'+ '\n'+ 'What kind of packages do you like to get?'+'\n+NATURAL'+'\n+CULTURAL'+'\n+ADVENTUROUS'+'\n'+'Name the place you would love to visit!')
        user_choice_package_name=input('Enter the name of place you would like to visit in Nepal: ')
        if user_choice_package_name in places.keys():
            print('You can see the different packages along with their price range available!!')
            print(places[user_choice_package_name])
        user_choice_package_type=input('Enter the package type you want:Natural/Cultural/Adventurous')
        user_choice_number_of_people=input('How many people are you travelling?')
        user_choice_price=input('What is your budget?')
        this_package=Packages(user_choice_package_name,user_choice_package_type,user_choice_number_of_people,user_choice_price)
