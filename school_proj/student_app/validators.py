# This will allow us to throw a validation error when interacting with 
# our models.
from django.core.exceptions import ValidationError
# This will allow us to search through our string to match our regex function
import re


# This will allow us to throw a validation error when interacting with 
# our models.
from django.core.exceptions import ValidationError
# This will allow us to search through our string to match our regex function
import re

def validate_name(name):
    error_message = 'Name must be in the format "First Middle Initial. Last"'
    regex = r'^[A-Z][a-z]+(?: [A-Z][a-z]+)* [A-Z]\. [A-Z][a-z]+$'

    good_name = re.match(regex, name)

    if good_name:
        return name
    else:
        raise ValidationError(error_message, params={'name': name})
    
def validate_school_email(email):
    error_message = 'Invalid school email format. Please use an email ending with "@school.com".'
    regex = r'^[a-zA-Z0-9._]+@school\.com$'

    good_email = re.match(regex, email)

    if good_email:
        return email
    else:
        raise ValidationError(error_message, params={'email' : email})
    
def validate_combination_format(locker_combination):
    error_message = 'Combination must be in the format "12-12-12"'
    regex = r'^\d{2}-\d{2}-\d{2}$'

    good_combo = re.match(regex, locker_combination)

    if good_combo:
        return locker_combination
    else:
        raise ValidationError(error_message, params={'locker_combination' : locker_combination})