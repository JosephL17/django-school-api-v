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


def validate_subject(subject):
    error = "Subject must be in title case format."
    if subject == subject.title():
        return subject
    else:
        raise ValidationError(error, params={'subject' : subject})
    
def validate_professor_name(professor_name):
    error = 'Professor name must be in the format "Professor Adam".'
    regex = r'^Professor [A-Z][a-z]+$'

    good_name = re.match(regex, professor_name)

    if good_name:
        return professor_name
    else:
        raise ValidationError(error, params={'professor_name' : professor_name})