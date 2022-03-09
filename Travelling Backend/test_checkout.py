import unittest
from Checkout import Checkout

class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.check1 = Checkout({'Pradeep':['Lamichhane', 'Nepali', '21', 'Male']}, {'pradeep.lamichhane@bison.howard.edu' : [('Mount Everest', 'Natural', 12, 50)]})
        self.check2 = Checkout({'Aniruddha':['Pokhrel', 'Nepali', '20', 'Male']}, {'pokhrelaniruddha@gmail.com': [('Trishuli River', 'Natural', 12, 50)]})
    
    
    def test_input(self):
        self.assertRaises(TypeError, Checkout, [], {})
        self.assertRaises(TypeError, Checkout, [], [])
        self.assertRaises(TypeError, Checkout, "apple", "banana")
        self.assertRaises(TypeError, Checkout, 12, 12)
        # self.assertRaises(ValueError, Checkout, {})
    
    def test_credit_number(self):
        try:
            self.assertEqual(self.check1.check_validity(6089991803485214), False)   #testing invalid card number
        except AttributeError:
            print ('Credit Card Number needs to be valid not just 14 digits long!')

        try:
            self.assertEqual(self.check2.check_validity(47447900118), False)        #testing shorter than 16 numbers in credit card
        except AttributeError:
            print('Enter Valid Credit Card Number!')

        try:
            self.assertEqual(self.check1.check_validity(4532976881951339), True)    #testing Visa card
        except AttributeError:
            print('Enter Valid Credit Card Number!')

        try:
            self.assertEqual(self.check2.check_validity(5155396653663538), True)    #testing Mastercard
        except AttributeError:
            print('Enter Valid Credit Card Number!')

        self.assertRaises(ValueError, self.check2.check_validity, 0)
    
    def test_total_sum(self):
        num_to_test_1 = 50
        num_to_test_2 = 100 
        sum_val = num_to_test_2 + num_to_test_1 //  num_to_test_2 - num_to_test_1
        tuple_val = (50, 100)
        
        self.assertRaises(TypeError, self.check2.retun_sum, ("nepal", "cultural"))
        
        try:
            self.assertEqual(self.check2.retun_sum(tuple_val), sum_val)    #testing total sum calculation
        except AttributeError:
            print('Calculation Error!')

    
    def test_creditnumber_value(self):
        self.assertRaises(ValueError, self.check1.check_validity, -4916217664216855)
        self.assertRaises(ValueError, self.check1.check_validity, 0)
        self.assertRaises(ValueError, self.check1.check_validity, 0.00)


if __name__ == "__main__":
    unittest.main(failfast=True)

def retun_sum(self, range_of_money):
        if type(range_of_money[0]) != int and type(range_of_money[1]) != int:
            raise TypeError("The input must be a number") 
        sum_val = range_of_money[1] + range_of_money[0] //  range_of_money[1] - range_of_money[0]
        return sum_val