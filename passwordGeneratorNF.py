#Nikole Florence
#SWDV-226
#Password Generator

import random
import string

#generate password gives users different options for character sets
#character set option is then returned
class characterSetOptions:
    def generatePassword(self, length, characterSet):
        characterSets = {
            '1': string.ascii_lowercase,
            '2': string.ascii_uppercase,
            '3': string.ascii_letters,
            '4': string.digits,
            '5': string.punctuation,
            '6': string.ascii_lowercase + string.digits,
            '7': string.ascii_uppercase + string.digits,
            '8': string.ascii_letters + string.digits,
            '9': string.ascii_letters + string.punctuation,
           '10': string.ascii_letters + string.digits + string.punctuation
            }
        
        charSet = characterSets[characterSet]
        return ''.join(random.choice(charSet) for _ in range(length))

#valid length gives users the option to chose a length between 8 and 12
#if a length is not chosen, 10 is the length they are given
#if their input is not valid, an error is thrown
class passwordLengthCustomization:
    def validLength(self, minLength = 8, maxLength = 12, defaultLength = 10):
        while True:
            lengthInput = input(f"Enter password length({minLength}-{maxLength}, default is {defaultLength}): ")
            if not lengthInput:
                return defaultLength
            try:
                length = int(lengthInput)
            except ValueError: 
                print("Invalid input. Enter a number.")
                continue
            if minLength <= length <= maxLength:
                return length
            print(f"Choose a length between {minLength} and {maxLength}.")
            print(lengthInput)
             
#main validates the length, and then has the user choose their length and char set
#once chosen, a password is generated for them with their options
#instances are made of the functions needed 
def main():
    setLength = passwordLengthCustomization()
    length = setLength.validLength()
    print("Choose a character set:\n" + "\n".join(f"{i}: {desc}" for i, desc in enumerate([
        "Lowercase letters",
        "Uppercase letters",
        "Lowercase and Uppercase letters",
        "Digits",
        "Symbols",
        "Lowercase letters and digits",
        "Uppercase letters and digits",
        "Letters and digits",
        "Letters and symbols",
        "All characters (letters, digits, and symbols)"
        ], start=1)))
        
    characterSet = input("Enter the number of your choice: ")
    while characterSet not in map(str, range(1, 11)):
        print("Invalid option. Choose a number between 1 and 10.")
        characterSet = input("Enter the number of your choice: ")
        
    charSetOptions = characterSetOptions()
    password = charSetOptions.generatePassword(length, characterSet)
    print(f"Generated password: {password}")
        
    resetOptions = input("Would you like to restart? (yes/no): ")
    return resetOptions.lower() == 'yes'
    
    
#main is then called, if the user choose to restart then the program runs again
#otherwise, the program stops
if __name__ == "__main__":
    while main():
        pass
                                                                                          
        