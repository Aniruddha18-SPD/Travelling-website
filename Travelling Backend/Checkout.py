#Luhn's Algorithm 
from IPython.display import clear_output
from Packages_available_with_us import packages_available_with_us
from user import User
class Checkout():
    def __init__(self, signup_dictionary, packages_dictionary): # dictionary from signup with personal information and dictionary from 
                                                                # packages with package selection is necessary. 
        self.signup_dict = signup_dictionary
        self.packages_dict = packages_dictionary  #if dict or not can be tested 
        
        self.new_arr = []
        self.signup_arr = []
        self.pack_selected = []
        if type(self.signup_dict) != dict:
            raise TypeError("The input must be a dictionary")

        for j in self.packages_dict.values():
            self.new_arr.append(j)
        for k in self.signup_dict.keys():
            self.signup_arr.append(k)
        
        self.pack_selected = self.new_arr[0][0]
        self.pack_selected = list(self.pack_selected)
        print(self.pack_selected) 
        print(self.signup_arr)
            
    
    def return_total(self):
        range_of_money = packages_available_with_us[self.new_arr[0][0][0]] 
        total_charge_with_taxes = range_of_money[1] + range_of_money[0] //  range_of_money[1] - range_of_money[0]
        if total_charge_with_taxes > 0:
            trigger = self.check_validity(self.cardnumber())
        else:
            print("Total is equal to zero")
        
        if trigger == True:
            self.billing(total_charge_with_taxes)
        # print(signup_arr)
        # print(h)
    
    
    ''' 
        Need to compute and showcase packages selected alongside their personal information
        i.e showcase a cart 
        give an option to edit their cart and make amendmends to their selection?
        move costumer towards checkout process
        Waiting on code from teammates '''
    
    
    
    
    
    def check_validity(self, num):                                                   # this function adds every digit of the card number to a list and,
        validlist=[]
        credit_check = False
        num =  int(num)
        if type(num) != int:
            raise TypeError("The input must be a number")

        if num <= 0 or len(str(num)) > 16:
            raise ValueError("Number can't be negative and the length can't be greater than 16")         
        
        num =  str(num)
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

    def billing(self, total_val):
        ''' waiting on code to print receipt '''        
        
        group_total = total_val * (int(self.pack_selected[2]))

        # create a company name and information
        company_name = "The Adventure Nepal"
        company_address = "Koteshwor"
        company_city = 'Kathmandu'

        # declare ending message
        first_message = '  Thanks for planning a trip with us today!' 
        second_message = '  We Welcome you to the footsteps of the Himalayas.'

        # create a top border
        print('*' * 50)

        # print company information first using format
        print('\t\t{}'.format(company_name.title()))
        print('\t\t{}'.format(company_address.title()))
        print('\t\t{}'.format(company_city.title()))

        # print a line between sections
        print('=' * 50)

        # print out header for section of items
        print('\tProduct Name\t\t Type')
        # create a print statement for each item
        # for z in range("len(cart)"):
        print('\t{}\t\t${}'.format(self.pack_selected[0].title(),self.pack_selected[1]))
        #print('\t{}\t${}'.format(p2_name.title(), p2_price))
        #print('\t{}\t\t${}'.format(p3_name.title(), p3_price))

        # print a line between sections
        print('=' * 50)

        # print out header for section of total
        print("\tIndividual Total \t Total For the Group ")

        # calculate total price and print out
        # for j in range(len("value_cart")):
        #     total_val = total_val + int("value_cart[j]")
        # total_val = str(total_val)
        print('\t\t${}\t\t\t${}'.format(total_val,group_total))

        # print a line between sections
        print('=' * 50)

        # output thank you message
        print('\n{}\n'.format(first_message))
        print('\n{}\n'.format(second_message))

        # create a bottom border
        print('*' * 50)


    # num = cardnumber()
    # if check_validity(num) == True:
    # billing()

# checkout = Checkout({20 : ["apple", "banana"]}, {'abcuiaa': [('Trishuli River', 'Natural', 12, 50)]})
# # hold = checkout.cardnumber()
# checkout.return_total()
# # checkout.billing()
# print(checkout.check_validity(hold))    # to check if cardnumber() and check_validity() work