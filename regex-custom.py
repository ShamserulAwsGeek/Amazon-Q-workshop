"""
Create a function called validate_string using regular expressions to validate a string with the following conditions:
    - There is one letter that is capitalized
    - next a hyphen
    - and rest numbers
    example: A-123456
""" 
import re

def validate_string(string):
    pattern = r'^[A-Z]-\d{6}$'
    return bool(re.match(pattern, string))

