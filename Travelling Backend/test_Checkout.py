import unittest
from Checkout import Checkout

class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.check1 = Checkout({}, {})
        self.check2 = Checkout({1:"apple"}, {2: "banana"})
    
    def test_input(self):
        self.assertRaises(TypeError, Checkout, [], {})
        self.assertRaises(TypeError, Checkout, [], [])
        self.assertRaises(TypeError, Checkout, "apple", "banana")
        self.assertRaises(TypeError, Checkout, 12, 12)

    def test_credit_number(self):
        try:
            self.assertEqual(self.check1.check_validity(6089991803485214), False)
        except AttributeError as e:
            print ('Credit Card Number needs to be valid not just 14 digits long!')

        #     raise 
        
        # self.assertEqual(self.check1.check_validity(6089991803485214), False)

        try:
            self.assertEqual(self.check2.check_validity(47447900118), False)
        except AttributeError:
            print('Enter Valid Credit Card Number!')
    
    
    def test_creditnumber_type(self):
        self.assertRaises(TypeError, Checkout.check_validity, "apple")
        ''' test for more types 
        
        
        
        '''

    
    def test_creditnumber_value(self):
        self.assertRaises(ValueError, self.check1.check_validity, -4916217664216855)
        self.assertRaises(ValueError, self.check1.check_validity, 0)
        ''' test for more values
        
        
        
        '''


if __name__ == "__main__":
    unittest.main(failfast=True)