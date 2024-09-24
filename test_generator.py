#Nikole Florence
#SWDV-226
#Password Generator Unit Test

#import unit test, mock, string, and classes from passwordGeneratorNF
import unittest
from unittest import mock
import random
import string

#setUp sets up length and char set options from the functions
#tests 1-4 test different password lengths
#tests 5-9 test the password generator options
from passwordGeneratorNF import characterSetOptions, passwordLengthCustomization

class TestPasswordGenerator(unittest.TestCase):
    def setUp (self):
        self.customLength = passwordLengthCustomization()
        self.charSetOptions = characterSetOptions()
        
    def test_valid_length_default(self):
        with mock.patch('builtins.input', side_effect=['']):
            self.assertEqual(self.customLength.validLength(), 10)
            
    def test_valid_length_custom(self):
        with mock.patch('builtins.input', side_effect=['9']):
            self.assertEqual(self.customLength.validLength(), 9)
            
    def test_valid_length_invalid(self):
        with mock.patch('builtins.input', side_effect=['2', '20', '10']):
            self.assertEqual(self.customLength.validLength(), 10)
            
    def test_valid_length_edge_cases(self):
        with mock.patch('builtins.input', side_effect=['8', '12']):
            self.assertEqual(self.customLength.validLength(), 8)
            
    #length and character set are set for all generator cases
    #password is generated each time to test results
    #for loops are used to get characters for the passwords
    def test_generate_password_lower(self):
        length = 10
        characterSet = '1'
        password = self.charSetOptions.generatePassword(length, characterSet)
        
        print(f"Generated password (lowercase): {password}")
        
        self.assertEqual(len(password), length)
        self.assertTrue(all(c in string.ascii_lowercase for c in password))
        
    def test_generate_password_upper(self):
        length = 10
        characterSet = '2'
        password = self.charSetOptions.generatePassword(length, characterSet)
        
        print(f"Generated password (uppercase): {password}")
        
        self.assertEqual(len(password), length)
        self.assertTrue(all(c in string.ascii_uppercase for c in password))
        
    def test_generate_password_digits(self):
        length = 10
        characterSet = '4'
        password = self.charSetOptions.generatePassword(length, characterSet)
        
        print(f"Generated password (digits): {password}")
        
        self.assertEqual(len(password), length)
        self.assertTrue(all(c in string.digits for c in password))
        
    def test_generate_password_symbols(self):
        length = 10
        characterSet = '5'
        password = self.charSetOptions.generatePassword(length, characterSet)
        
        self.assertEqual(len(password), length)
        
        print(f"Generated password (symbols): {password}")
        
        self.assertTrue(all(c in string.punctuation for c in password))
        
    def test_generate_password_combo(self):
        length = 10
        characterSet = '10'
        password = self.charSetOptions.generatePassword(length, characterSet)
        
        self.assertEqual(len(password), length)
        
        print(f"Generated password (combo): {password}")
        
        has_letter = any(c in string.ascii_letters for c in password)
        has_digit = any(c in string.digits for c in password)
        has_symbol = any(c in string.punctuation for c in password)
        
        self.assertTrue(has_letter)
        self.assertTrue(has_digit)
        self.assertTrue(has_symbol)
        
if __name__ == "__main__":
    unittest.main()
            