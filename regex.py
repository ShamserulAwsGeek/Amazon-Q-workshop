"""

create a function to use regular expressions to validate emails

""" 
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

email = input("Enter an email address: ")
if validate_email(email):
    print("Valid email address")
else:
    print("Invalid email address")


#phone number regex:

"""

 create a function to use regular expressions to validate phone numbers

"""

def validate_phone_number(phone_number):
    pattern = r'^\+?1?\d{9,15}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False
        
phone_number = input("Enter a phone number: ")
 


 """
create a function to validate international phone numbers
include +1

""" 
def validate_international_phone_number(phone_number):
    pattern = r'^\+1\d{10}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False  