''' define Signup class'''
from packages_available_with_us import CLI_packing
class Signup:
    customers_information = {}
    customers_account = {}
    
    def __init__(self):
        self.current_user_first = input("Enter your first name: ")
        self.current_user_second = input("Enter your second name: ")
        self.full_name = self.current_user_first +" "+ self.current_user_second
        print(f'Welcome to the Lap of Himalayas, {self.full_name}!')
        self.current_user_nationality = input("Enter your nationality: ")
        self.current_user_age = input("Enter you age: ")
        self.current_user_gender = input("Enter your gender: ")
        self.customers_information[self.full_name] = [self.current_user_nationality, self.current_user_age, self.current_user_gender]

        # print(self.customers_information)

    
    def create_account(self):
        self.user_account = input("Have you created your account yet? Type 'Y' for Yes or 'N' for No!")
        if self.user_account == 'Y':
            print("You can go and find the best packages after submitting your credentials!")
            customer_username = input("Enter your username: ")
            customer_password = input("Enter your password: ")
            if self.customers_account[customer_username] == customer_password:
                print("You successfully logged in. Let's go and find the best packages.")
                # find_package()
                CLI_packing(customer_username)
            else:
                print("You have either typed wrong credentials or have not signed up yet!" )

           
        else:
            username = True
            while username:
                customer_new_username = input("Enter your email: ")
                if customer_new_username in self.customers_account:
                    print("This email already exists.")
                    username = True
                else:
                    username = False
            customer_new_password = input("Enter your password: ")
            print("You successfully created your account")
          
            self.customers_account[customer_new_username]= customer_new_password
            print(self.customers_account)
            # find_package()
signup1 = Signup()
# print(signup1.customers_account)
signup1.create_account()

            
