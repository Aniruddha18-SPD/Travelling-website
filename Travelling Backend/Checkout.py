#Luhn's Algorithm 
from IPython.display import clear_output

class Checkout():
    def __init__(self, signup_dictionary, packages_dictionary): # dictionary from signup with personal information and dictionary from 
                                                                # packages with package selection is necessary. 
        self.signup_dict = signup_dictionary
        self.packages_dict = packages_dictionary  #if dict or not can be tested 
    
    
    ''' 
        Need to compute and showcase packages selected alongside their personal information
        i.e showcase a cart 
        give an option to edit their cart and make amendmends to their selection?
        move costumer towards checkout process
        Waiting on code from teammates '''
    
    
    
    
    
    
    def check_validity(self, num):                                                   # this function adds every digit of the card number to a list and,
        validlist=[]
        credit_check = False
        #while not credit_check:
        for i in num:
            validlist.append(int(i))
        for i in range(0,len(num),2):                                             # applying Luhn Algorithm to check whether resulting sum is divisible by ten
            validlist[i] = validlist[i] * 2
            if validlist[i]  >= 10:
                validlist[i] =  (validlist[i]//10 + validlist[i]%10)
        
        if sum(validlist)% 10 == 0:
            credit_check = True
            print("This is a VALID CARD!")
            return credit_check
        
        else:
            credit_check = False
            print('INVALID CARD NUMBER')
            return credit_check

    def cardnumber(self):                                                                     # accepts card number as a string

        card_num = ''
        while True:
            try:
                card_num = input('Enter your 16 digit credit card number : ')

                if not (len(card_num) == 16) or not type(int(card_num) == int) :
                    raise Exception

            except Exception:    
                print('That is not a valid credit card number. \nMake sure you are entering digits not characters and all the 16 digits.')
                continue

            else:
                break


        return card_num

    def billing(self):
        total_val = 0

        # create a company name and information
        company_name = "Company Name goes Here"
        company_address = 'Company address goes Here'
        company_city = 'city address goes here'

        # declare ending message
        message = 'Thanks for planning a trip with us today! We Welcome you to the footsteps of the Himalayas.'

        # create a top border
        print('*' * 50)

        # print company information first using format
        print('\t\t{}'.format(company_name.title()))
        print('\t\t{}'.format(company_address.title()))
        print('\t\t{}'.format(company_city.title()))

        # print a line between sections
        print('=' * 50)

        # print out header for section of items
        print('\tProduct Name\tProduct Price')
        # create a print statement for each item
        for z in range("len(cart)"):
            print('\t{}\t\t${}'.format("cart[z].title()", "value_cart[z]"))
        #print('\t{}\t${}'.format(p2_name.title(), p2_price))
        #print('\t{}\t\t${}'.format(p3_name.title(), p3_price))

        # print a line between sections
        print('=' * 50)

        # print out header for section of total
        print('\t\t\tTotal')

        # calculate total price and print out
        for j in range(len("value_cart")):
            total_val = total_val + int("value_cart[j]")
        total_val = str(total_val)
        print('\t\t\t${}'.format(total_val))

        # print a line between sections
        print('=' * 50)

        # output thank you message
        print('\n\t{}\n'.format(message))

        # create a bottom border
        print('*' * 50)


    # num = cardnumber()
    # if check_validity(num) == True:
    #     billing()

# checkout = Checkout("apple", "banana")
# hold = checkout.cardnumber()
# print(checkout.check_validity(hold))    to check if cardnumber() and check_validity() work